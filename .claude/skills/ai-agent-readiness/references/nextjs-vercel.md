# Implementation — Next.js App Router and Vercel

Recipes for actually shipping the three layers. Adapt idioms if the project uses Pages Router, Astro, SvelteKit, or a CMS — the shapes carry over.

## robots.txt

Static file at `public/robots.txt` is fine and simplest. Prefer `app/robots.ts` when the policy needs to vary by environment (block everything on preview deployments — a genuinely common leak).

```ts
// app/robots.ts
import type { MetadataRoute } from 'next'

const SITE = process.env.NEXT_PUBLIC_SITE_URL ?? 'https://example.com'
const isProd = process.env.VERCEL_ENV === 'production'

export default function robots(): MetadataRoute.Robots {
  if (!isProd) return { rules: [{ userAgent: '*', disallow: '/' }] }

  return {
    rules: [
      // Retrieval — these produce citations
      { userAgent: ['OAI-SearchBot', 'Claude-SearchBot', 'PerplexityBot'], allow: '/' },
      // Training — opt out (delete this group for the Open posture)
      {
        userAgent: ['GPTBot', 'ClaudeBot', 'CCBot', 'Google-Extended', 'Applebot-Extended', 'Bytespider'],
        disallow: '/',
      },
      { userAgent: '*', allow: '/', disallow: ['/api/', '/admin/'] },
    ],
    sitemap: `${SITE}/sitemap.xml`,
  }
}
```

Next's `MetadataRoute.Robots` type has no field for `Content-Usage` or `Crawl-delay`. If those are needed, use a static `public/robots.txt` instead, or a route handler returning `text/plain`.

## llms.txt

There's no built-in metadata route. Two options:

**Static** — `public/llms.txt`. Correct for a marketing site with a stable page set. Hand-curated, which is what you want.

**Generated** — a route handler for docs sites where content comes from MDX or a CMS:

```ts
// app/llms.txt/route.ts
export const dynamic = 'force-static'

export async function GET() {
  const docs = await getAllDocs() // your MDX/CMS loader
  const body = [
    '# Product Name',
    '',
    '> One or two sentences of essential context.',
    '',
    '## Docs',
    '',
    ...docs.map((d) => `- [${d.title}](${SITE}${d.slug}.md): ${d.summary}`),
  ].join('\n')

  return new Response(body, {
    headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
  })
}
```

Keep the generated list curated — filter to docs that matter, don't emit every route. If the list runs past ~50 entries, split by path (`/docs/llms.txt`, `/api/llms.txt`) rather than growing one file.

## Markdown mirrors

Serve the raw source at `<path>.md`:

```ts
// app/docs/[slug]/md/route.ts  — or a catch-all rewrite to <path>.md
export async function GET(_: Request, { params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params
  const doc = await getDoc(slug)
  if (!doc) return new Response('Not found', { status: 404 })
  return new Response(doc.raw, {
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      'Cache-Control': 'public, s-maxage=3600, stale-while-revalidate=86400',
    },
  })
}
```

Advertise them without touching pages, via `vercel.json` headers:

```json
{
  "headers": [
    {
      "source": "/docs/:slug",
      "headers": [
        {
          "key": "Link",
          "value": "</docs/:slug.md>; rel=\"alternate\"; type=\"text/markdown\", </docs/llms.txt>; rel=\"describedby\""
        }
      ]
    }
  ]
}
```

Or per-page in the App Router with a `<link rel="alternate" type="text/markdown" href="...">` in the layout head. The header form is preferable at scale — it's one config change instead of a change per template.

## Rendering

The failure mode to grep for: a page component with `"use client"` at the top, or content fetched in a `useEffect`. Either means the content is absent from the initial HTML.

```bash
grep -rl '^["'\'']use client' app/**/page.tsx
```

Fixes: keep pages as server components and push interactivity into leaf client components; use `generateStaticParams` for known routes; use ISR (`export const revalidate = 3600`) for content that changes. `dynamic = 'force-dynamic'` still server-renders — it's client-only rendering that's the problem, not dynamism.

Verify with a JS-free fetch, not with devtools:

```bash
curl -s https://example.com/pricing | grep -c "Distinctive phrase from the page"
```

## JSON-LD

Inline in a server component. Keep it derived from the same data the page renders, so the two can't drift:

```tsx
export default async function Page({ params }) {
  const post = await getPost(params.slug)
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Article',
    headline: post.title,
    datePublished: post.publishedAt,
    dateModified: post.updatedAt,
    author: { '@type': 'Person', name: post.author, sameAs: post.authorUrl },
  }
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      <article>{/* the same facts, visibly */}</article>
    </>
  )
}
```

Never inject JSON-LD from a client component — it may not be in the initial HTML, which defeats the point.

## Vercel and CDN specifics

- **Preview deployments** are indexable unless blocked. Vercel sets `X-Robots-Tag: noindex` on preview URLs by default on some plans — verify rather than assume, and pair with the env-aware `robots.ts` above.
- **Vercel Firewall / Bot Management** rules sit above robots.txt. If the project also runs Cloudflare in front of Vercel, that's a second gate — check both.
- **Attack Challenge Mode** blocks legitimate crawlers wholesale. Fine as an incident response, disastrous if left on.
- Verify per-bot reachability from outside the network:

```bash
for ua in GPTBot OAI-SearchBot ClaudeBot Claude-SearchBot PerplexityBot; do
  printf '%-18s ' "$ua"
  curl -s -o /dev/null -w '%{http_code}\n' -A "$ua" https://example.com/
done
```

Anything other than 200 for the retrieval bots is the finding that outranks everything else in the audit.
