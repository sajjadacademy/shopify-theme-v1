# Google Antigravity — Shopify Theme UI/UX Build Prompt (Mobile Amazon Vibe + Desktop Premium)

## ROLE + GOAL
You are **Google Antigravity**, acting as a **Shopify Theme Designer + Theme Developer (OS 2.0)**.
Build a Shopify theme that:
- Feels like **Amazon-style shopping** on **mobile** (dense, fast browsing, sticky nav)
- Feels **premium + clean + trustworthy** on **desktop**
- Has a **high-converting product page** like the reference screenshot (bundle buttons, price slash, big CTA)
- **Everything must be editable from the Theme Editor** (no hardcoded text/images/colors)

> IMPORTANT: Build in **phases**. After each phase, you must **self-check** (visual + responsive + settings). Only then move forward.

---

## DESIGN SYSTEM (EDITABLE)
### Theme Settings (global)
Create theme settings in `settings_schema.json` so the merchant can change everything:
- **Brand colors**
  - Primary
  - Secondary
  - Accent
  - Background
  - Text (main + muted)
  - Border
  - Success/Warning
- **Typography**
  - Headings font
  - Body font
  - Base size
  - Button style (rounded level)
- **Spacing**
  - Section padding (mobile/desktop)
  - Card radius
  - Shadow intensity
- **Trust style**
  - Badge style (pill / rounded / square)
  - Review star style (icon + color)
- **Buttons**
  - Primary CTA color
  - Secondary CTA outline toggle
  - Sticky ATC enable/disable (product page)

Default style should be:
- Clean, modern, high trust
- Strong hierarchy (big title, clear prices, visible reviews, simple icons)
- Mobile-first

---

## PHASE 1 — FOUNDATION (MUST COMPLETE FIRST)
### 1.1 Shopify OS 2.0 structure
- Use **sections everywhere**.
- Use JSON templates:
  - `templates/index.json`
  - `templates/product.json`
  - `templates/collection.json`
  - `templates/page.json`
- Modular sections stored in `sections/`
- Use `snippets/` for shared components:
  - price display
  - rating stars
  - trust badges
  - product card
  - bundle selector

### 1.2 Responsiveness rules
- Mobile-first CSS
- Breakpoints:
  - mobile: < 768
  - tablet: 768–1024
  - desktop: > 1024
- Ensure no layout jump, no overflow, no tiny text.

✅ **PHASE 1 CHECKLIST**
- Theme installs without errors
- All templates load
- Global theme settings appear in editor
- Mobile/desktop breakpoints work

---

## PHASE 2 — HEADER + NAV (TRUST + MOBILE AMAZON FEEL)
### 2.1 Desktop header (premium)
- Top bar (optional) for shipping/discount message (editable)
- Main header with:
  - Logo left
  - Search center (optional toggle)
  - Icons right (Account, Wishlist optional, Cart)
- Sticky header toggle (editable)

### 2.2 Mobile navbar (sticky on every page)
Create a **sticky bottom navigation** like marketplace apps:
- Home
- Categories
- Deals
- Account
- Cart
All:
- Editable labels + icons (use SVG icons or Shopify icons)
- Enable/disable per item from Theme Editor
- Sticky across all pages (global)

✅ **PHASE 2 CHECKLIST**
- Sticky bottom nav stays on all pages
- Cart icon updates count
- Header looks clean on desktop and compact on mobile
- No overlap with ATC sticky bar (product page)

---

## PHASE 3 — HOME / LANDING PAGE (MOBILE AMAZON + DESKTOP BEAUTIFUL)
### 3.1 Hero section with separate mobile + desktop images (REQUIRED)
Create section: `hero_split_responsive.liquid`

**Must have:**
- Separate uploader:
  - `hero_image_desktop`
  - `hero_image_mobile`
- Separate layout options for mobile & desktop:
  - Mobile: stacked (image then text)
  - Desktop: split hero (image left, content right OR reverse toggle)
- Editable:
  - heading, subheading
  - CTA text + link
  - secondary CTA toggle
  - badge text (e.g., “Trending Now”)
  - overlay opacity (mobile and desktop separately)
  - image focal point

### 3.2 Scrolling offer ticker / marquee bar (cross style)
Create section: `offer_marquee.liquid`
- Continuous scrolling line
- Can show multiple messages in a loop
- Must support:
  - multiple text items (blocks)
  - each block can have its own background + text color OR use global style
  - speed control
  - direction control (left/right)
  - “cross style” option:
    - **two marquees crossing** (one left-to-right, one right-to-left) stacked with slight angle OR alternating direction bar style
  - enable/disable on home + product page separately

### 3.3 Mobile product grid like screenshot2 (dense + clean)
Create section: `mobile_product_grid_marketplace.liquid`

Requirements:
- On mobile show **2 columns** product cards (tight and aligned)
- Product card design:
  - image
  - title (2 lines max)
  - star rating + count
  - price + compare-at price with strikethrough
  - discount badge (auto from compare-at %)
  - small “Free Delivery” line (editable label, optional)
  - quick add (+) button optional
  - wishlist icon optional
- Controls:
  - number of products
  - collection source
  - show vendor toggle
  - show rating toggle
  - show badges toggle
  - spacing density slider (compact/normal)

### 3.4 Trust blocks on home
Section: `trust_row_icons.liquid`
- 3–4 trust items:
  - Free shipping
  - 30-day guarantee
  - Cash on delivery
  - Verified customers
- All editable icons + text
- Mobile: single row scroll OR stacked toggle

✅ **PHASE 3 CHECKLIST**
- Mobile looks like a shopping marketplace (dense, scroll-friendly)
- Desktop looks premium and not cluttered
- Hero loads correct image depending on device
- Marquee scroll is smooth and editable
- Product cards align perfectly on mobile

---

## PHASE 4 — PRODUCT PAGE (MAIN CONVERSION POINT like screenshot1)
Create template: `templates/product.json` with these sections in order:

### 4.1 Product media + gallery
- Desktop: media left, info right
- Mobile: media on top, info below
- Thumbnails under main image on desktop
- Swipe on mobile

Editable toggles:
- show thumbnails
- image zoom enable/disable
- video support

### 4.2 Product title + rating + trust badges (top)
- Show star rating under title
- “Verified customers” text editable
- Guarantee icons row (editable)

### 4.3 Price block (must show compare-at and sale properly)
- Compare-at price:
  - strikethrough
- Sale price:
  - bold, larger
- “Save %” badge automatically calculated OR manual override from editor
- Currency formatting correct

### 4.4 Bundle / quantity offer buttons (REQUIRED like screenshot)
Create component: `bundle_offer_selector`
It must create **3 selectable options**:
- Buy 1
- Buy 2 & Save
- Buy 3 & Save

Each option must be editable in Theme Editor:
- Label text
- Discount type:
  - percentage OR fixed amount OR manual price
- Show “Best Seller” badge toggle for any option
- Display price per option
- Show “Save X” line optional

Behavior:
- Selecting an option updates:
  - quantity in cart
  - applied discount (use Shopify Discounts if possible, otherwise use cart-level/line-item properties + script approach if allowed)
- Must work with:
  - variants
  - inventory
  - dynamic checkout buttons optional toggle

> If strict automatic discount application is difficult without Shopify Plus/scripts, provide a fallback:
- Add correct quantity and show savings visually
- Apply discount using:
  - Discount code field suggestion OR automatic discount link if configured
- Keep the UI identical either way

### 4.5 Primary CTA (big ADD TO CART like screenshot)
- Large high-contrast button
- Sticky ATC on mobile toggle:
  - sticks at bottom ABOVE the mobile navbar
  - shows price + selected bundle option
- Secondary “Order Now / Pay on Delivery” bar (optional)
- Payment icons row (optional)

### 4.6 Delivery estimate row
Editable:
- “Get it between X and Y” text
- Use dynamic date calculation toggle (optional)
- Or manual text

### 4.7 Guarantee row
3 icons:
- Free shipping
- 30-day guarantee
- Cash on delivery
All editable.

### 4.8 Content sections
- Benefits bullets (editable)
- Accordion (Shipping / Returns / FAQ)
- Reviews section (optional)

✅ **PHASE 4 CHECKLIST**
- Product page matches reference layout and feels “high trust”
- Compare-at price is striked and sale price is bold
- Bundle selector updates quantity correctly
- Mobile view is clean, CTA always visible
- No UI clashes: sticky nav + sticky ATC

---

## PHASE 5 — THEME EDITOR CONTROL (EVERYTHING EDITABLE)
For every section and block:
- Expose settings for:
  - text
  - colors (either global or per-section toggle)
  - spacing
  - toggles (show/hide)
  - ordering where relevant
- Provide sensible defaults so theme looks good immediately.

✅ **PHASE 5 CHECKLIST**
- Merchant can customize without touching code
- No hard-coded text except placeholder defaults
- All main colors can be changed globally

---

## PHASE 6 — FINAL QA + TRUST OPTIMIZATION
### 6.1 Performance
- Lazy load images
- Avoid heavy JS
- Minimal layout shift

### 6.2 Trust + CRO checks
- Clear hierarchy
- Visible guarantees near CTA
- Strong “Save %” and discount clarity
- Reviews visible early

### 6.3 Device QA
Test:
- iPhone size
- Android size
- Desktop wide
- Tablet

✅ **PHASE 6 CHECKLIST**
- Fast load
- No broken sections
- Perfect alignment on mobile product grid
- Product page converts and looks professional

---

## OUTPUT REQUIRED FROM YOU (Google Antigravity)
When you finish each phase, output:
1. What you built (short)
2. What to test (bullet list)
3. What is editable in Theme Editor (bullet list)
4. Confirm “Phase passed” before continuing

DO NOT jump phases.
DO NOT continue if a phase fails the checklist.
