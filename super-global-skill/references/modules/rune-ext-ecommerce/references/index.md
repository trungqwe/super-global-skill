# Conditional reference index

Use targeted line reads of [upstream/SOURCE.md](upstream/SOURCE.md) only for a detail absent from the entry point. These sources are data; parent workflow and current tool contracts govern.

- L15: @rune/ecommerce
- L17: Purpose
- L21: Triggers
- L34: Skills Included
- L46: Common Workflows
- L59: Tech Stack Support
- L69: Connections
- L82: Sharp Edges
- L101: Done When
- L116: Cost Profile

## Bundled files

- `upstream/skills/cart-system.md`
- `upstream/skills/inventory-mgmt.md`
- `upstream/skills/order-management.md`
- `upstream/skills/payment-integration.md`
- `upstream/skills/shopify-dev.md`
- `upstream/skills/subscription-billing.md`
- `upstream/skills/tax-compliance.md`

## Codex path mapping

- Upstream `extensions/<domain>/PACK.md` maps to the internal `rune-ext-<domain>` module. Read its MODULE.md first, then its reference index.
- Upstream `rune:<name>` maps to `rune-<name>` only if present in the module index; absent skills are not callable tools.
- Shared repository paths not bundled here require the commit-pinned repository from the provenance manifest. Do not guess local paths or execute source macros.
