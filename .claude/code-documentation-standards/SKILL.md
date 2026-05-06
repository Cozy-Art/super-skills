---
name: code-documentation-standards
description: Enforce file header and inline documentation standards for this project. Use when creating new files, modifying existing files, or reviewing code. Ensures consistency, context preservation, and token efficiency for AI-assisted development.
allowed-tools: Read, Edit, Write, Glob, Grep
---

# Code Documentation Standards

## Overview

This skill ensures all code files in the [this project] follow consistent documentation standards that:

1. **Preserve context** - Help Claude and developers understand files quickly
2. **Save tokens** - Provide navigation aids to jump to relevant sections
3. **Prevent duplication** - Show what's already implemented
4. **Document gotchas** - Capture "why" decisions and edge cases
5. **Enable knowledge transfer** - Help future developers (and Claude) understand the codebase

## When to Apply This Skill

Use this skill automatically when:

- Creating ANY new code file
- Modifying existing files (update `@lastUpdated` and relevant sections)
- Discovering gotchas or edge cases (document immediately)
- Refactoring code (update CONNECTED FILES if relationships change)
- Reviewing code for consistency

## File Header Checklist

### For ALL Code Files (if they support comments)

Before writing or modifying any code file, ensure it has:

```typescript
/**
 * @fileoverview [ComponentName/FunctionName] - Brief description
 * @lastUpdated YYYY-MM-DD - What changed in last update
 * @status Complete | In Progress | Needs Review | Deprecated
 * @dependencies Key dependencies (optional but helpful)
 *
 * [File-type-specific sections - see templates below]
 */
```

### Status Indicators

- **Complete** - Fully implemented, tested, production-ready
- **In Progress** - Actively being developed
- **Needs Review** - Awaiting code review or testing
- **Needs Testing** - Implementation done, testing pending
- **Deprecated** - Being phased out
- **Experimental** - Testing approach, may change

## Section Markers (Use Consistently)

All code files should use these greppable section markers:

```typescript
// ========== IMPORTS ==========

// ========== TYPES & INTERFACES ==========

// ========== CONSTANTS & CONFIG ==========

// ========== HELPER FUNCTIONS ==========

// ========== MAIN COMPONENT/LOGIC ==========

// ========== EXPORTS ==========
```

**Why:** Claude can grep for these and jump directly to relevant sections.

## File-Type-Specific Requirements

### React Components (.tsx, .jsx)

**Required Sections in Header:**
- SECTIONS: List of major code blocks
- KEY NOTES: Implementation details, gotchas, limitations
- CONNECTED FILES: Related components and utilities
- USAGE EXAMPLE: How to use this component

**Example:**
```typescript
/**
 * @fileoverview ProductCard - Displays product with strain info and price
 * @lastUpdated 2025-01-06 - Added hover animations
 * @status Complete
 * @dependencies StrainBadge, lib/utils/formatting
 *
 * SECTIONS:
 * - Types & Interfaces: ProductCardProps
 * - Helper Functions: formatPrice
 * - Main Component: ProductCard with animations
 *
 * KEY NOTES:
 * - Uses Framer Motion for hover effects
 * - Strain badge color logic in getStrainColor()
 * - Mobile: stacks at <768px breakpoint
 *
 * CONNECTED FILES:
 * - components/strain/StrainBadge.tsx (strain type display)
 * - components/product/ProductGrid.tsx (parent)
 *
 * USAGE EXAMPLE:
 * <ProductCard product={productData} strain={strainData} />
 */
```

### API Routes (app/api/**/route.ts)

**Required Sections in Header:**
- FLOW: Step-by-step request processing
- REQUEST: Method, body structure, headers
- RESPONSE: Status codes and response shapes
- ERROR HANDLING: What errors are caught
- SECURITY: Validation and auth checks
- GOTCHAS: Third-party API quirks, timing issues

**Example:**
```typescript
/**
 * @fileoverview POST /api/stripe/checkout - Create checkout session
 * @lastUpdated 2025-01-15 - Added shipping calculation
 * @status Complete
 * @external Stripe API, Printful shipping API
 *
 * FLOW:
 * 1. Validate cart items
 * 2. Calculate shipping via Printful
 * 3. Create Stripe session
 * 4. Return session URL
 *
 * REQUEST:
 * - Method: POST
 * - Body: { items: CartItem[], shippingAddress: Address }
 *
 * RESPONSE:
 * - 200: { sessionUrl: string }
 * - 400: { error: string } - Invalid cart data
 * - 500: { error: string } - API failure
 *
 * SECURITY:
 * - Validates cart items against product catalog
 * - Sanitizes shipping address inputs
 *
 * GOTCHAS:
 * - Stripe requires amounts in cents (multiply by 100)
 * - Printful shipping has 15min cache TTL
 */
```

### Utility Functions (lib/utils/*.ts)

**Required Sections in Header:**
- CONTENTS: List of exported functions
- USED BY: Components/files that depend on this
- DEPENDENCIES: External libraries

**Function Documentation:**
Every exported function needs:
```typescript
/**
 * Brief description of what function does
 *
 * @param param1 - Description and valid values
 * @param param2 - Optional param explanation
 * @returns What this returns and format
 *
 * @example
 * const result = functionName('input');
 * // result: 'expected output'
 *
 * NOTE: Why this function exists
 */
```

### Sanity Schemas (sanity/schemas/*.ts)

**Required Sections in Header:**
- RELATIONSHIPS: → (this to other), ← (other to this), ↔ (bidirectional)
- REQUIRED FIELDS: What's mandatory and why
- OPTIONAL BUT RECOMMENDED: Best practices
- VALIDATION RULES: Field validation logic
- USAGE NOTES: How editors should use this in Studio

### Zustand Stores (store/*.ts)

**Required Sections in Header:**
- STATE SHAPE: What state is tracked
- ACTIONS: Available actions and when to use them
- PERSISTENCE: LocalStorage/SessionStorage/None
- USED BY: Components consuming this store

### Type Definitions (types/*.d.ts)

**Required Sections in Header:**
- TYPES DEFINED: List of exported types
- USED BY: Files importing these types
- REFERENCES: External API docs or schema sources

**Inline Type Documentation:**
```typescript
/**
 * Description of what type represents
 *
 * Used for: Specific use cases
 *
 * NOTE: Important validation or constraint details
 */
export interface TypeName {
  /** Field description with valid values */
  field1: string;

  /** Optional field with default behavior if omitted */
  field2?: number;
}
```

## Inline Comment Standards

### DO Comment:

✅ Complex algorithms or business logic
✅ Non-obvious "why" decisions
✅ Performance optimizations
✅ Accessibility implementations
✅ Security considerations
✅ Workarounds for bugs/limitations
✅ Edge cases being handled
✅ Future TODOs or known issues

### DON'T Comment:

❌ Obvious code (`// Set state to true`)
❌ Self-documenting code with clear naming
❌ Repeated explanations (DRY applies to comments)

### Comment Keywords (Use Consistently)

```typescript
// TODO: Description of what needs to be done
// FIXME: Description of bug and why it happens
// NOTE: Important context or gotcha
// OPTIMIZE: Performance improvement opportunity
// SECURITY: Security-related note
// ACCESSIBILITY: A11y implementation detail
```

### Good vs Bad Examples

**GOOD - Explains WHY:**
```typescript
// We use setTimeout to batch updates and prevent layout thrashing
setTimeout(() => updateDOM(), 0);

// Calculate shipping based on Printful weight tiers
// Tier 1 (0-1lb): $5, Tier 2 (1-5lb): $8, Tier 3 (5+lb): $12
const shippingCost = weight < 1 ? 5 : weight < 5 ? 8 : 12;

// ACCESSIBILITY: aria-live announces cart updates to screen readers
// without interrupting current navigation
<div aria-live="polite">{cartMessage}</div>
```

**BAD - Explains WHAT (code already shows this):**
```typescript
// Call setTimeout with updateDOM
setTimeout(() => updateDOM(), 0);

// Check if weight is less than 1
const shippingCost = weight < 1 ? 5 : weight < 5 ? 8 : 12;
```

## File Types Without Comment Support

### JSON Files

**Cannot use comments.** Create adjacent documentation file instead.

Example: For `package.json`, create `package.README.md`

### .env Files

**Use comments in `.env.example` only**, not in `.env.local`

### Other Non-Comment Files

- **Markdown** - Use headers and lists for structure
- **CSS** - Use `/* comments */` sparingly

## Progressive Implementation

**DO NOT refactor all files at once.** Apply headers:

1. ✅ When creating new files (always start with header)
2. ✅ When modifying existing files (add header + update @lastUpdated)
3. ✅ When debugging (document what was fixed)
4. ✅ When discovering gotchas (document immediately)

## Workflow Integration

### Before Creating a New File

1. Pick the right template from "File-Type-Specific Requirements" above
2. Start file with complete header
3. Add section markers
4. Write code with inline comments for complex logic

### When Modifying an Existing File

1. Check if file has header - if not, add it
2. Update `@lastUpdated` field with current date
3. Update relevant header sections (KEY NOTES, CONNECTED FILES, etc.)
4. Add inline comments for new complex logic
5. Update TODO/FIXME comments if addressed

### When Discovering a Gotcha

Document immediately:

```typescript
// GOTCHA: Safari doesn't support scrollend (iOS 16)
// Using scroll + debounce fallback until Safari 17+ adoption
element.addEventListener('scroll', debounce(handler, 150));
```

Update file header KEY NOTES or GOTCHAS section if significant.

## Quality Checks

Before considering a file "complete", verify:

- [ ] File header present with all required sections
- [ ] `@lastUpdated` is current date
- [ ] `@status` reflects actual state
- [ ] Section markers present and used correctly
- [ ] Complex logic has inline comments explaining WHY
- [ ] CONNECTED FILES section is accurate
- [ ] No obvious code without comments (avoid over-commenting)
- [ ] TODOs/FIXMEs are actionable

## Benefits of This System

### For Claude (You):
- Quick context without reading entire file
- Jump to relevant sections using greppable markers
- Understand relationships and dependencies
- Learn from past decisions and gotchas
- Avoid re-implementing existing functionality

### For Developers:
- Onboard to codebase faster
- Understand "why" behind code decisions
- Avoid repeating past mistakes
- Find related code quickly
- Maintain consistency across team

### For Project:
- Knowledge preservation across sessions
- Reduced redundant code
- Better collaboration
- Easier long-term maintenance
- Token efficiency in Claude sessions

## Integration with Other Systems

This skill works alongside:

- **CLAUDE.md** - Project-level instructions and architecture
- **Resources/core-planning/CORE-PLAN.md** - Active phase index + phase files
- **Resources/decisions/** - Architectural Decision Records for significant choices
- **.cursor/rules/** - Cursor-specific development rules
- **TaskCreate / TaskUpdate tools** - Session-level task tracking

## Examples in This Project

Look at these files as reference examples:

- `components/product/ProductCard.tsx` - Component example (when updated)
- `lib/sanity/queries.ts` - Utility function example (when updated)
- `sanity/schemas/strain.ts` - Schema example (when updated)
- `app/api/printful/products/route.ts` - API route example (when created)

## Common Mistakes to Avoid

❌ **Don't** add headers to all files at once (progressive only)
❌ **Don't** over-comment obvious code
❌ **Don't** forget to update `@lastUpdated` when modifying files
❌ **Don't** copy-paste headers without customizing sections
❌ **Don't** add comments to JSON files (create adjacent .md instead)

✅ **Do** explain WHY, not WHAT
✅ **Do** update headers when modifying files
✅ **Do** document gotchas immediately when discovered
✅ **Do** keep CONNECTED FILES section accurate
✅ **Do** use consistent section markers

## Quick Reference

### New File Checklist
1. Choose appropriate template from "File-Type-Specific Requirements" above
2. Add complete file header
3. Add section markers
4. Write code with inline comments
5. Verify all sections are filled out

### Existing File Modification Checklist
1. Add header if missing
2. Update `@lastUpdated` to today's date
3. Update changed sections in header
4. Add inline comments for new logic
5. Update CONNECTED FILES if relationships changed

---

## Summary

**Always:**
- Start new files with appropriate header template
- Update `@lastUpdated` when modifying files
- Use section markers consistently
- Comment complex logic with WHY
- Document gotchas immediately
- Keep CONNECTED FILES accurate

**Never:**
- Comment obvious code
- Forget to update headers when editing
- Add comments to JSON files
- Refactor all files at once (progressive only)

**Reference:** "File-Type-Specific Requirements" section above for complete templates

---

**This skill is critical to project success. Apply it consistently.**
