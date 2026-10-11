# Thomas Web Group — Content Inventory

Inventory date: 2026-10-10

> **Implementation note (2026-10-10):** This inventory is the pre-implementation baseline. Copy fields and route counts have since changed; use `content-implementation-report.md` and the current templates as the authoritative record of implemented copy. `content-needs-owner-review.md` lists unresolved facts.

## Scope and method

This inventory covers all 16 routes written by the current Eleventy build, including utility/legal pages that are not in the main navigation. It records user-facing copy and page metadata, including form labels, select options, image alternative text, accessible names, and copy inside collapsed FAQ answers. Identical shared text is documented once in the shared-components section, not counted again for every route.

“Status” describes the state evidenced by the source, not whether the statement is true. No item is marked approved/verified: no explicit approval record was found. “Existing copy—verify” means authored copy exists but should be fact-checked and approved before publication. “Technical/system” means UI, legal, validation, or accessibility text rather than promotional copy.

Source paths are relative to the repository root. Locations identify front matter fields, markup blocks, or exact data properties. Recommended lengths are editorial targets, not current length limits. For repeated placeholders, each numbered instance is separately identified.

## Active routes

| Page | Route | Source |
|---|---|---|
| Home | `/` | `strategy/index.njk` |
| Websites | `/websites/` | `strategy/websites.njk` |
| Work index | `/work/` | `strategy/work.njk` |
| Dad Cuts Grass project | `/work/dad-cuts-grass/` | `strategy/work/dad-cuts-grass.njk` |
| Smoky Mountain Acres project | `/work/smoky-mountain-acres/` | `strategy/work/smoky-mountain-acres.njk` |
| About | `/about/` | `strategy/about.njk` |
| Contact | `/contact/` | `strategy/contact.njk` |
| CRM & Business Systems | `/crm-business-systems/` | `strategy/crm-business-systems.njk` + `strategy/_includes/service-page.njk` |
| Growth & Automation | `/growth-automation/` | `strategy/growth-automation.njk` + `strategy/_includes/service-page.njk` |
| Social Media | `/social-media/` | `strategy/social-media.njk` + `strategy/_includes/service-page.njk` |
| FAQ | `/faq/` | `strategy/faq.njk` |
| Pricing / ongoing services | `/pricing/` | `strategy/pricing.njk` + `strategy/_includes/pricing.njk` |
| Privacy Policy | `/privacy-policy/` | `strategy/privacy-policy.njk` |
| Terms | `/terms/` | `strategy/terms.njk` |
| Thank you | `/thank-you/` | `strategy/thank-you.njk` |
| Not found | `/404.html` | `strategy/404.njk` |

## Shared components and metadata rules

| Content ID | Page / URL | Source and location | Type / current content | Purpose, length, context | Status |
|---|---|---|---|---|---|
| GLOBAL.BRAND | All 15 routes using the shared base layout | `strategy/_includes/header.njk` `.brand-wordmark`; footer `.brand-wordmark`; CSS adds a trailing period to the header wordmark | Brand name: `Thomas Web Group`; header renders `Thomas Web Group.` | Consistent brand identifier; keep spelling and punctuation intentional. | Existing copy—verify approved brand styling |
| GLOBAL.HEADER.NAV.HOME | All 15 base-layout routes; mobile menu too | `strategy/_includes/header.njk` first nav link | `01 Home` | Global route label; 1 word plus number. | Technical/system |
| GLOBAL.HEADER.NAV.WEBSITES | All 15 base-layout routes; mobile menu too | Same, second nav link | `02 Websites` | Global route label; 1 word plus number. | Technical/system |
| GLOBAL.HEADER.NAV.WORK | All 15 base-layout routes; mobile menu too | Same, third nav link | `03 Work` | Global route label; 1 word plus number. | Technical/system |
| GLOBAL.HEADER.NAV.ABOUT | All 15 base-layout routes; mobile menu too | Same, fourth nav link | `04 About` | Global route label; 1 word plus number. | Technical/system |
| GLOBAL.HEADER.NAV.CONTACT | All 15 base-layout routes; mobile menu too | Same, fifth nav link | `05 Contact` | Global route label; 1 word plus number. | Technical/system |
| GLOBAL.HEADER.QUOTE_CTA | All 15 base-layout routes; desktop button and mobile-menu entry | `strategy/_includes/header.njk` both `.btn-getstarted` links | `Get a Project Quote` | Primary site-wide conversion action to `/contact/`; 4 words. One source supplies both responsive variants. | Existing copy—verify |
| GLOBAL.HEADER.BRAND_ACCESSIBLE_NAME | All 15 base-layout routes | `strategy/_includes/header.njk` brand link `aria-label` | `Thomas Web Group home` | Accessible name for logo link; 4 words. | Technical/system |
| GLOBAL.HEADER.MENU_OPEN | Routes at mobile widths | `strategy/_includes/header.njk` button initial `aria-label`; state updated in `strategy/assets/js/main.js` | `Open navigation` | Name for collapsed menu control; 2 words. | Technical/system |
| GLOBAL.HEADER.MENU_CLOSE | Routes at mobile widths, when expanded | `strategy/assets/js/main.js` `mobileNavToogle()` | `Close navigation` | State-dependent accessible name; 2 words. | Technical/system |
| GLOBAL.FOOTER.INTRO | All 15 base-layout routes | `strategy/_includes/footer.njk`, `.footer-brand p` | `Thomas Web Group helps small businesses improve their websites, online visibility, customer management, and everyday operations through practical digital solutions.` | Short company positioning text beside the wordmark; 20 words. | Existing copy—review (Homepage Copy v1) |
| GLOBAL.FOOTER.EXPLORE | All 15 base-layout routes | `strategy/_includes/footer.njk`, first footer-links heading | `Explore` | Heading for the Home, Websites, Work links; 1 word. | Existing copy—verify |
| GLOBAL.FOOTER.COMPANY | All 15 base-layout routes | Same, second footer-links heading | `Company` | Heading for About, Contact, and quote links; 1 word. | Existing copy—verify |
| GLOBAL.FOOTER.CONTACT_HEADING | All 15 base-layout routes | `strategy/_includes/footer.njk`, `.footer-contact h4` | `Contact` | Heading for email, phone, and location; 1 word. | Existing copy—verify |
| GLOBAL.FOOTER.EMAIL | All 15 base-layout routes | Same, mailto link | `raymond@thomaswebgroup.com` | Contact method; verify spelling and monitored inbox. | Existing copy—verify factual |
| GLOBAL.FOOTER.PHONE | All 15 base-layout routes | Same, tel link | `(423) 225-8787` | Contact method; verify public number and telephone link. | Existing copy—verify factual |
| GLOBAL.FOOTER.LOCATION | All 15 base-layout routes | Same, final list item | `East Tennessee` | Service-area/location signal; verify intended wording. | Existing copy—verify factual |
| GLOBAL.FOOTER.QUOTE_LINK | All 15 base-layout routes | `strategy/_includes/footer.njk`, Company list | `Get a Project Quote` | Repeated footer CTA to `/contact/`; 4 words. | Existing copy—verify |
| GLOBAL.FOOTER.YEAR | All 15 base-layout routes | `strategy/_includes/footer.njk`, `.footer-meta` | `© 2024 Thomas Web Group` | Copyright line; confirm whether the year should be dynamic/current and confirm legal ownership. | Existing copy—verify factual |
| GLOBAL.FOOTER.LEGAL | All 15 base-layout routes | Same, second `.footer-meta` span | `[LEGAL FOOTER TEXT]` | Short legal/company footer note; confirm content and destination if it links elsewhere. | Placeholder |
| GLOBAL.SCROLL_TOP | All 15 base-layout routes | `strategy/_includes/footer.njk`, `#scroll-top` | Up-arrow icon only; no visible text or accessible label | Back-to-top control; accessibility wording is not supplied in source. | Technical/system; missing accessible name |
| GLOBAL.META.TITLE | All routes using `strategy/_includes/base.njk` | `<title>{{ title }}</title>` | Outputs each route’s `title` front matter verbatim. | Browser/tab title; page-specific values are recorded below. | Existing metadata—verify |
| GLOBAL.META.DESCRIPTION | All routes using the base layout | `strategy/_includes/base.njk`, description meta | Outputs page `description`; fallback is `Thomas Web Group helps small businesses attract customers and simplify day-to-day work with websites, social media, CRM, and automation.` | Search/social summary; all 15 base-layout routes define descriptions, so fallback is not rendered. | Existing metadata—verify |
| GLOBAL.META.OG_TITLE | All routes using the base layout | `strategy/_includes/base.njk`, `og:title` | Same value as page `title`. | Open Graph title is inherited, not separately authored. | Existing metadata—verify |
| GLOBAL.META.OG_DESCRIPTION | All routes using the base layout | Same, `og:description` | Same value as page `description` (fallback as above). | Social-sharing description is inherited, not separately authored. | Existing metadata—verify |
| GLOBAL.META.CANONICAL | Base-layout routes | `strategy/_includes/base.njk`, conditional `canonical` link | Not rendered: no active page defines `canonical`. | Canonical URL per route; needs a decision whether canonical links should be added. | Missing SEO field |
| GLOBAL.META.OG_IMAGE | All 16 routes | No `og:image` field in base or active route front matter | Not present. | Social preview image; determine whether a site-wide or page-specific image is wanted. | Missing SEO field |
| GLOBAL.META.ROBOTS | Thank-you route | Base layout conditional; `noindex: true` in `strategy/thank-you.njk` | `noindex, nofollow` is rendered on `/thank-you/`. Other base-layout routes do not set a robots directive. | Indexing instruction; technical SEO. | Technical/system |

## Home — `/`

Source: `strategy/index.njk`; shared metadata/layout from `strategy/_includes/base.njk`.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| HOME.META.TITLE | Front matter `title` | `Thomas Web Group \| Websites & Business Growth Solutions` | Browser/search title; 55 characters. | Existing metadata—review (Homepage Copy v1) |
| HOME.META.DESCRIPTION | Front matter `description` | `Websites, Google and AI search visibility, social media, and business automation for small businesses ready to attract more customers and improve operations.` | Search/social summary; 157 characters. | Existing metadata—review (Homepage Copy v1) |
| HOME.HERO.EYEBROW | Hero `.hero-kicker` | `Digital Growth & Business Systems` | Name the agency/category before the headline; 5 words. | Existing copy—review (Homepage Copy v1) |
| HOME.HERO.HEADING | Hero H1 | `Get Found. Win More Customers. Run Your Business Better.` | Core customer benefit/value proposition; 9 words, designed for a large hero heading. | Existing copy—review (Homepage Copy v1) |
| HOME.HERO.DESCRIPTION | Hero paragraph | `We help small businesses build a stronger online presence, turn more inquiries into customers, and spend less time on repetitive work through better websites, marketing, and connected systems.` | Explain audience, services, and outcome; 28 words, one short paragraph beneath H1. | Existing copy—review (Homepage Copy v1) |
| HOME.HERO.CTA_WORK | Hero primary button | `View Our Work` → `/work/` | Invite proof browsing; 3 words. | Existing copy—review (Homepage Copy v1) |
| HOME.HERO.CTA_SERVICES | Hero secondary button | `Explore Websites` → `/websites/` | Introduce website services; 2 words. | Existing copy—review (Homepage Copy v1) |
| HOME.HERO.IMAGE_ALT | Hero `.hero-visual` `aria-label` | `Laptop showcase image placeholder. Add an approved Thomas Web Group project screenshot.` | Accessible description of the hero visual; replace only when approved project artwork is supplied. | Placeholder / factual asset needed |
| HOME.HERO.SCREEN | Visible laptop-screen text | `[APPROVED PROJECT SCREENSHOT NEEDED]` | Internal-facing placeholder appears inside the laptop device; replace with approved project screenshot/artwork, not marketing copy. | Placeholder / factual asset needed |
| HOME.PROJECTS.KICKER | Featured projects section kicker | `Our Work` | Section eyebrow; 2 words. | Existing copy—review (Homepage Copy v1) |
| HOME.PROJECTS.HEADING | Section H2 | `Real Businesses. Practical Solutions.` | Introduce project examples; 4 words. | Existing copy—review (Homepage Copy v1) |
| HOME.PROJECTS.01.TITLE | Card 1 H3 | `Smoky Mountain Acres` | Identify project/client; 3 words. | Existing copy—review (Homepage Copy v1) |
| HOME.PROJECTS.01.SUMMARY | Card 1 paragraph | `A custom farm website with livestock listings, availability tracking, and a simple content management system that makes keeping the website updated easier.` | Describe project scope; 22 words. | Existing copy—review (Homepage Copy v1) |
| HOME.PROJECTS.01.TECH.1 | Card 1 first tag | `Eleventy` | Project platform/technology; 1 word. | Existing copy—verify technology |
| HOME.PROJECTS.01.TECH.2 | Card 1 second tag | `Decap CMS` | Project platform/technology; 2 words. | Existing copy—verify technology |
| HOME.PROJECTS.01.TECH.3 | Card 1 third tag | `Netlify` | Project platform/technology; 1 word. | Existing copy—verify technology |
| HOME.PROJECTS.01.CTA | Card 1 link | `View Project` → `/work/` | Project navigation; 2 words. | Existing copy—review (Homepage Copy v1) |
| HOME.PROJECTS.02.TITLE | Card 2 H3 | `Dad Cuts Grass` | Identify project/client; 3 words. | Existing copy—review (Homepage Copy v1) |
| HOME.PROJECTS.02.SUMMARY | Card 2 paragraph | `A lawn care website designed to make it easier for customers to explore services and request quotes online.` | Describe project purpose; 18 words. | Existing copy—pending verification |
| HOME.PROJECTS.02.CTA | Card 2 link | `View Project` → `/work/` | Project navigation; 2 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.KICKER | Additional services section kicker | `Beyond Websites` | Short service category eyebrow; 2 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.HEADING | Section H2 | `More Ways to Grow Your Business` | Introduces three offering cards; 6 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.01.TITLE | Service card 1 H3 | `Social Media & Online Visibility` | Name a service; 5 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.01.DESCRIPTION | Service card 1 paragraph | `Stay visible to potential customers with consistent social media activity and a stronger presence where people search for businesses.` | Explain deliverable/outcome; 18 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.02.TITLE | Service card 2 H3 | `Customer & Lead Management` | Name a service; 4 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.02.DESCRIPTION | Service card 2 paragraph | `Keep customer information organized, track potential jobs, and follow up with leads before opportunities slip through the cracks.` | Explain deliverable/outcome; 18 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.03.TITLE | Service card 3 H3 | `Business Automation & Reporting` | Name a service; 4 words. | Existing copy—review (Homepage Copy v1) |
| HOME.SERVICES.03.DESCRIPTION | Service card 3 paragraph | `Connect your existing tools, reduce repetitive administrative work, and get clearer information about how your business is performing.` | Explain deliverable/outcome; 18 words. | Existing copy—review (Homepage Copy v1) |
| HOME.CTA.EYEBROW | Closing CTA `.page-kicker` | `Let's Talk Business` | Set up final conversion prompt; 3 words. | Existing copy—review (Homepage Copy v1) |
| HOME.CTA.HEADING | Closing CTA H2 | `What's Holding Your Business Back?` | Short, specific invitation; 5 words. | Existing copy—review (Homepage Copy v1) |
| HOME.CTA.BUTTON | Closing CTA button | `Get a Project Quote` → `/contact/` | Conversion action; 4 words. | Existing copy—review (Homepage Copy v1) |

## Websites — `/websites/`

Source: `strategy/websites.njk`. Project cards and FAQ rows are page-specific markup, not shared data.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| WEBSITES.META.TITLE | Front matter `title` | `Websites \| Thomas Web Group` | Browser/search title; about 50–60 characters. | Existing metadata—verify |
| WEBSITES.META.DESCRIPTION | Front matter `description` | `Placeholder service page for website design and development.` | Search/social summary; about 140–160 characters. | Placeholder |
| WEBSITES.INTRO.KICKER | Page intro kicker | `[SERVICE PAGE TITLE]` | Service/category eyebrow; 2–6 words. | Placeholder |
| WEBSITES.INTRO.HEADING | H1 | `[WEBSITE SERVICE INTRO]` | Main website-design benefit; about 5–12 words. | Placeholder |
| WEBSITES.INTRO.DESCRIPTION | Intro paragraph | `[WEBSTIES PAGE DESCRIPTION]` | Explain service scope, audience, and outcome; about 25–45 words. Preserve that the current source spelling is `WEBSTIES`. | Placeholder |
| WEBSITES.CAPABILITIES.KICKER | Capabilities kicker | `[CAPABILITIES]` | Eyebrow; 1–3 words. | Placeholder |
| WEBSITES.CAPABILITIES.HEADING | H2 | `Website capabilities` | Introduces three capability cards; 2 words. | Existing copy—verify |
| WEBSITES.CAPABILITY.01.TITLE | Card 1 H3 | `[CAPABILITY TITLE]` | Name a deliverable; 2–5 words. | Placeholder |
| WEBSITES.CAPABILITY.01.DESCRIPTION | Card 1 paragraph | `[CAPABILITY DESCRIPTION]` | Define deliverable and value; 12–25 words. | Placeholder |
| WEBSITES.CAPABILITY.02.TITLE | Card 2 H3 | `[CAPABILITY TITLE]` | Name a deliverable; 2–5 words. | Placeholder |
| WEBSITES.CAPABILITY.02.DESCRIPTION | Card 2 paragraph | `[CAPABILITY DESCRIPTION]` | Define deliverable and value; 12–25 words. | Placeholder |
| WEBSITES.CAPABILITY.03.TITLE | Card 3 H3 | `[CAPABILITY TITLE]` | Name a deliverable; 2–5 words. | Placeholder |
| WEBSITES.CAPABILITY.03.DESCRIPTION | Card 3 paragraph | `[CAPABILITY DESCRIPTION]` | Define deliverable and value; 12–25 words. | Placeholder |
| WEBSITES.PROCESS.KICKER | Process kicker | `[PROCESS]` | Eyebrow; 1–3 words. | Placeholder |
| WEBSITES.PROCESS.HEADING | H2 | `Process overview` | Introduces four numbered steps; 2 words. | Existing copy—verify |
| WEBSITES.PROCESS.01.TITLE | Step 1 H3 | `[DISCOVERY]` | Name first confirmed process stage; 1–4 words. | Placeholder / factual |
| WEBSITES.PROCESS.01.DESCRIPTION | Step 1 paragraph | `[DISCOVERY DESCRIPTION]` | State what happens and what client supplies; 12–25 words. | Placeholder / factual |
| WEBSITES.PROCESS.02.TITLE | Step 2 H3 | `[PLANNING]` | Name second confirmed process stage; 1–4 words. | Placeholder / factual |
| WEBSITES.PROCESS.02.DESCRIPTION | Step 2 paragraph | `[PLANNING DESCRIPTION]` | Explain planning/deliverables; 12–25 words. | Placeholder / factual |
| WEBSITES.PROCESS.03.TITLE | Step 3 H3 | `[BUILD]` | Name third confirmed process stage; 1–4 words. | Placeholder / factual |
| WEBSITES.PROCESS.03.DESCRIPTION | Step 3 paragraph | `[BUILD DESCRIPTION]` | Explain implementation and review; 12–25 words. | Placeholder / factual |
| WEBSITES.PROCESS.04.TITLE | Step 4 H3 | `[LAUNCH]` | Name fourth confirmed process stage; 1–4 words. | Placeholder / factual |
| WEBSITES.PROCESS.04.DESCRIPTION | Step 4 paragraph | `[LAUNCH DESCRIPTION]` | Explain launch and handoff; 12–25 words. | Placeholder / factual |
| WEBSITES.WORK.KICKER | Selected work kicker | `[SELECTED WORK]` | Eyebrow; 1–3 words. | Placeholder |
| WEBSITES.WORK.HEADING | H2 | `Selected website projects` | Introduces project cards; 2–4 words. | Existing copy—verify |
| WEBSITES.WORK.01.STATUS | Card 1 badge | `[PROJECT STATUS]` | Verified project status; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.01.TITLE | Card 1 H3 | `[PROJECT TITLE]` | Project/client name; 2–6 words. | Placeholder / factual |
| WEBSITES.WORK.01.SUMMARY | Card 1 paragraph | `[PROJECT SUMMARY]` | Project challenge and delivered result; 15–30 words. | Placeholder / factual |
| WEBSITES.WORK.01.TECH.1 | Card 1 first tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.01.TECH.2 | Card 1 second tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.01.TECH.3 | Card 1 third tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.01.CTA | Card 1 link | `View project` → `/work/` | Project navigation; 1–3 words. | Existing copy—verify |
| WEBSITES.WORK.02.STATUS | Card 2 badge | `[PROJECT STATUS]` | Verified project status; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.02.TITLE | Card 2 H3 | `[PROJECT TITLE]` | Project/client name; 2–6 words. | Placeholder / factual |
| WEBSITES.WORK.02.SUMMARY | Card 2 paragraph | `[PROJECT SUMMARY]` | Challenge and delivered result; 15–30 words. | Placeholder / factual |
| WEBSITES.WORK.02.TECH.1 | Card 2 first tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.02.TECH.2 | Card 2 second tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.02.TECH.3 | Card 2 third tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.02.CTA | Card 2 link | `View project` → `/work/` | Project navigation; 1–3 words. | Existing copy—verify |
| WEBSITES.WORK.03.STATUS | Card 3 badge | `[PROJECT STATUS]` | Verified project status; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.03.TITLE | Card 3 H3 | `[PROJECT TITLE]` | Project/client name; 2–6 words. | Placeholder / factual |
| WEBSITES.WORK.03.SUMMARY | Card 3 paragraph | `[PROJECT SUMMARY]` | Challenge and delivered result; 15–30 words. | Placeholder / factual |
| WEBSITES.WORK.03.TECH.1 | Card 3 first tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.03.TECH.2 | Card 3 second tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.03.TECH.3 | Card 3 third tag | `[TECH]` | Name a verified platform/technology; 1–3 words. | Placeholder / factual |
| WEBSITES.WORK.03.CTA | Card 3 link | `View project` → `/work/` | Project navigation; 1–3 words. | Existing copy—verify |
| WEBSITES.FAQ.KICKER | FAQ kicker | `[FAQ]` | Eyebrow; 1–3 words. | Placeholder |
| WEBSITES.FAQ.HEADING | H2 | `Frequently asked questions` | Introduces three visible static FAQ pairs; 3 words. | Existing copy—verify |
| WEBSITES.FAQ.01.QUESTION | FAQ 1 H3 | `[QUESTION]` | Specific website-service concern; 5–12 words. | Placeholder |
| WEBSITES.FAQ.01.ANSWER | FAQ 1 paragraph | `[ANSWER]` | Direct, factual answer; 25–60 words. | Placeholder / factual |
| WEBSITES.FAQ.02.QUESTION | FAQ 2 H3 | `[QUESTION]` | Specific website-service concern; 5–12 words. | Placeholder |
| WEBSITES.FAQ.02.ANSWER | FAQ 2 paragraph | `[ANSWER]` | Direct, factual answer; 25–60 words. | Placeholder / factual |
| WEBSITES.FAQ.03.QUESTION | FAQ 3 H3 | `[QUESTION]` | Specific website-service concern; 5–12 words. | Placeholder |
| WEBSITES.FAQ.03.ANSWER | FAQ 3 paragraph | `[ANSWER]` | Direct, factual answer; 25–60 words. | Placeholder / factual |
| WEBSITES.CTA.EYEBROW | Closing CTA kicker | `[PROJECT QUOTE]` | Short lead-in; 1–4 words. | Placeholder |
| WEBSITES.CTA.HEADING | Closing CTA H2 | `Get a Project Quote` | Conversion prompt; 4 words. | Existing copy—verify |
| WEBSITES.CTA.BUTTON | Closing CTA button | `Get a Project Quote` → `/contact/` | Conversion action; 4 words. | Shared existing copy—verify |

## Work index — `/work/`

Source: `strategy/work.njk`. Four project cards are static markup. The `[IMAGE]` text is currently displayed inside a styled thumbnail; these are not actual image elements.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| WORK.META.TITLE | Front matter `title` | `Work \| Thomas Web Group` | Browser/search title; about 50–60 characters. | Existing metadata—verify |
| WORK.META.DESCRIPTION | Front matter `description` | `Placeholder portfolio page for selected Thomas Web Group work.` | Search/social summary; about 140–160 characters. | Placeholder |
| WORK.INTRO.KICKER | Page intro kicker | `[WORK INDEX]` | Eyebrow; 1–3 words. | Placeholder |
| WORK.INTRO.HEADING | H1 | `[WORK PAGE HEADING]` | Explain what portfolio contains; 3–8 words. | Placeholder |
| WORK.INTRO.DESCRIPTION | Intro paragraph | `[WORK PAGE DESCRIPTION]` | Frame the work and its scope; 20–40 words. | Placeholder |
| WORK.CARD.01.IMAGE | Card 1 `.thumb` text | `[IMAGE]` | Supply/identify approved project thumbnail; no image alt exists because this is a text div. | Placeholder / asset needed |
| WORK.CARD.01.STATUS | Card 1 badge | `[STATUS]` | Accurate status; 1–3 words. | Placeholder / factual |
| WORK.CARD.01.TITLE | Card 1 H3 | `[PROJECT TITLE]` | Project/client; 2–6 words. | Placeholder / factual |
| WORK.CARD.01.SUMMARY | Card 1 paragraph | `[PROJECT SUMMARY]` | Challenge, work, and evidence-based outcome; 15–30 words. | Placeholder / factual |
| WORK.CARD.01.TECH.1 | Card 1 first tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.01.TECH.2 | Card 1 second tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.01.TECH.3 | Card 1 third tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.01.CTA | Card 1 link | `Request details` → `/contact/` | Contact action; 2 words. | Existing copy—verify |
| WORK.CARD.02.IMAGE | Card 2 thumbnail | `[IMAGE]` | Approved project image/identity; no actual `<img>` is currently rendered. | Placeholder / asset needed |
| WORK.CARD.02.STATUS | Card 2 badge | `[STATUS]` | Accurate status; 1–3 words. | Placeholder / factual |
| WORK.CARD.02.TITLE | Card 2 H3 | `[PROJECT TITLE]` | Project/client; 2–6 words. | Placeholder / factual |
| WORK.CARD.02.SUMMARY | Card 2 paragraph | `[PROJECT SUMMARY]` | Challenge, work, evidence-based outcome; 15–30 words. | Placeholder / factual |
| WORK.CARD.02.TECH.1 | Card 2 first tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.02.TECH.2 | Card 2 second tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.02.TECH.3 | Card 2 third tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.02.CTA | Card 2 link | `Request details` → `/contact/` | Contact action; 2 words. | Existing copy—verify |
| WORK.CARD.03.IMAGE | Card 3 thumbnail | `[IMAGE]` | Approved project image/identity; currently a text div. | Placeholder / asset needed |
| WORK.CARD.03.STATUS | Card 3 badge | `[STATUS]` | Accurate status; 1–3 words. | Placeholder / factual |
| WORK.CARD.03.TITLE | Card 3 H3 | `[PROJECT TITLE]` | Project/client; 2–6 words. | Placeholder / factual |
| WORK.CARD.03.SUMMARY | Card 3 paragraph | `[PROJECT SUMMARY]` | Challenge, work, evidence-based outcome; 15–30 words. | Placeholder / factual |
| WORK.CARD.03.TECH.1 | Card 3 first tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.03.TECH.2 | Card 3 second tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.03.TECH.3 | Card 3 third tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.03.CTA | Card 3 link | `Request details` → `/contact/` | Contact action; 2 words. | Existing copy—verify |
| WORK.CARD.04.IMAGE | Card 4 thumbnail | `[IMAGE]` | Approved project image/identity; currently a text div. | Placeholder / asset needed |
| WORK.CARD.04.STATUS | Card 4 badge | `[STATUS]` | Accurate status; 1–3 words. | Placeholder / factual |
| WORK.CARD.04.TITLE | Card 4 H3 | `[PROJECT TITLE]` | Project/client; 2–6 words. | Placeholder / factual |
| WORK.CARD.04.SUMMARY | Card 4 paragraph | `[PROJECT SUMMARY]` | Challenge, work, evidence-based outcome; 15–30 words. | Placeholder / factual |
| WORK.CARD.04.TECH.1 | Card 4 first tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.04.TECH.2 | Card 4 second tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.04.TECH.3 | Card 4 third tag | `[TECH]` | Verified platform/technology; 1–3 words. | Placeholder / factual |
| WORK.CARD.04.CTA | Card 4 link | `Request details` → `/contact/` | Contact action; 2 words. | Existing copy—verify |
| WORK.CTA.EYEBROW | Closing CTA kicker | `[WORK CTA]` | Lead-in; 1–4 words. | Placeholder |
| WORK.CTA.HEADING | Closing CTA H2 | `Get a Project Quote` | Conversion heading; 4 words. | Shared existing copy—verify |
| WORK.CTA.BUTTON | Closing CTA button | `Get a Project Quote` → `/contact/` | Conversion action; 4 words. | Shared existing copy—verify |

## Project detail pages

These project pages have real named-project copy, image alternative text, feature lists, quotes, and contact CTAs. Treat claims, publication permissions, names, and attributions as unverified until the owner confirms them.

### Dad Cuts Grass — `/work/dad-cuts-grass/`

Source: `strategy/work/dad-cuts-grass.njk`.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| PROJECT.DAD.META.TITLE | Front matter `title` | `Dad Cuts Grass Website Project \| Thomas Web Group` | Browser/search title; 50–60 characters. | Existing metadata—verify |
| PROJECT.DAD.META.DESCRIPTION | Front matter `description` | `A lawn-care website with service details and a custom online quote form for Dad Cuts Grass.` | Search/social summary; 140–160 characters. | Existing metadata—verify factual |
| PROJECT.DAD.SECTION_LABEL | `.section-title h2` | `Website Project` | Project type; 2 words. | Existing copy—verify |
| PROJECT.DAD.CATEGORY | `.section-title span` | `Local Service Business` | Client category; 3 words. | Existing copy—verify factual |
| PROJECT.DAD.CLIENT_LABEL | `.description-title` | `Dad Cuts Grass` | Project/client identity; 3 words. | Existing copy—verify |
| PROJECT.DAD.IMAGE_ALT | Logo image `alt` | `Dad Cuts Grass website project` | Describe logo/project image; 5 words. Confirm alt matches actual asset. | Existing copy—verify |
| PROJECT.DAD.H1 | Main project H1 | `Dad Cuts Grass` | Identify project; 3 words. | Existing copy—verify |
| PROJECT.DAD.INTRO | Lead paragraph | `Dad Cuts Grass needed a website where local customers could review lawn-care services and request an instant quote.` | Summarize client need; 10–25 words. Verify instant-quote capability. | Existing copy—verify factual |
| PROJECT.DAD.BUILD.HEADING | Section H2 | `What We Built` | Introduce delivered work; 3 words. | Existing copy—verify |
| PROJECT.DAD.BUILD.01 | First list item | `Mobile-friendly lawn-care service pages` | Concrete deliverable; 3–8 words. | Existing copy—verify factual |
| PROJECT.DAD.BUILD.02 | Second list item | `Custom online quote form` | Concrete deliverable; 3–8 words. | Existing copy—verify factual |
| PROJECT.DAD.BUILD.03 | Third list item | `Contact options for prospective customers` | Concrete deliverable; 3–8 words. | Existing copy—verify factual |
| PROJECT.DAD.TESTIMONIAL.HEADING | Section H2 | `Client Feedback` | Introduce testimonial; 2 words. | Existing copy—verify |
| PROJECT.DAD.TESTIMONIAL.TEXT | Blockquote | `Everything changed after I got the new website going. They helped implement instant online quotes for my customers and I was shocked at how well that has converted for us.` followed by `Really great people. Thanks Thomas Web Group!` | Client voice/testimonial; 2 sentences plus closing endorsement. Verify exact quote, attribution, permission, and conversion claim. | Existing copy—verify testimonial |
| PROJECT.DAD.TESTIMONIAL.ATTRIBUTION | Bold text | `Ray T, Owner` | Identify speaker; verify preferred public name/title and consent. | Existing copy—verify factual |
| PROJECT.DAD.CTA.HEADING | CTA H2 | `Need online quote requests for your service business?` | Connect project capability to prospective client; 8 words. Verify claims. | Existing copy—verify |
| PROJECT.DAD.CTA.BUTTON | CTA link | `Let's Talk` → `/contact/` | Contact action; 2 words. | Shared existing copy—verify |

### Smoky Mountain Acres — `/work/smoky-mountain-acres/`

Source: `strategy/work/smoky-mountain-acres.njk`.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| PROJECT.SMA.META.TITLE | Front matter `title` | `Smoky Mountain Acres Website Project \| Thomas Web Group` | Browser/search title; 50–60 characters. | Existing metadata—verify |
| PROJECT.SMA.META.DESCRIPTION | Front matter `description` | `A farm website for Smoky Mountain Acres, with pages for farm tours, livestock, local products, and educational articles.` | Search/social summary; 140–160 characters. | Existing metadata—verify factual |
| PROJECT.SMA.SECTION_LABEL | `.section-title h2` | `Website Project` | Project type; 2 words. | Existing copy—verify |
| PROJECT.SMA.CATEGORY | `.section-title span` | `Farm & Local Business` | Client category; 4 words. | Existing copy—verify factual |
| PROJECT.SMA.CLIENT_LABEL | `.description-title` | `Smoky Mountain Acres` | Project/client identity; 3 words. | Existing copy—verify |
| PROJECT.SMA.IMAGE_ALT | Logo image `alt` | `Smoky Mountain Acres website project` | Describe project image; 5 words. Confirm asset/alt suitability. | Existing copy—verify |
| PROJECT.SMA.H1 | Main project H1 | `Smoky Mountain Acres` | Identify project; 3 words. | Existing copy—verify |
| PROJECT.SMA.INTRO | Lead paragraph | `The farm needed pages for its livestock, farm tours, local products, and educational content.` | Summarize client need; 10–25 words. Verify delivered scope. | Existing copy—verify factual |
| PROJECT.SMA.LIVE_LINK | Link to external site | `View Live Website` → `https://smokymountainacres.com` | Show published project; verify destination/current availability. | Existing copy—verify factual |
| PROJECT.SMA.BUILD.HEADING | Section H2 | `What We Built` | Introduce work; 3 words. | Existing copy—verify |
| PROJECT.SMA.BUILD.01 | First list item | `Pages for livestock, farm tours, and local products` | Concrete deliverable; 3–10 words. | Existing copy—verify factual |
| PROJECT.SMA.BUILD.02 | Second list item | `Blog for farm updates and educational articles` | Concrete deliverable; 3–10 words. | Existing copy—verify factual |
| PROJECT.SMA.BUILD.03 | Third list item | `Optimized farm photography` | Concrete deliverable; 2–5 words. | Existing copy—verify factual |
| PROJECT.SMA.TESTIMONIAL.HEADING | Section H2 | `Client Feedback` | Introduce testimonial; 2 words. | Existing copy—verify |
| PROJECT.SMA.TESTIMONIAL.TEXT | Blockquote | `We are a local farm in East TN who needed a website that reflected our family's values and mission. One challenge was trying to figure out what sort of design we wanted and what we wanted the website to say. Thomas Web Group worked patiently with us to give us exactly what we were looking for!` followed by `I can't recommend them enough and am so excited with our new website!` | Client voice/testimonial; verify exact quote, permissions, client relationship, and whether minor copyediting is allowed. | Existing copy—verify testimonial |
| PROJECT.SMA.TESTIMONIAL.ATTRIBUTION | Bold text | `Kristen Lee, Client` | Identify speaker; verify preferred public name/title and consent. | Existing copy—verify factual |
| PROJECT.SMA.CTA.HEADING | CTA H2 | `Need a website with room for multiple services and content?` | Relate project to a prospect need; 9 words. | Existing copy—verify |
| PROJECT.SMA.CTA.BUTTON | CTA link | `Let's Talk` → `/contact/` | Contact action; 2 words. | Shared existing copy—verify |

## About — `/about/`

Source: `strategy/about.njk`.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| ABOUT.META.TITLE | Front matter `title` | `About \| Thomas Web Group` | Search title; 50–60 characters. | Existing metadata—verify |
| ABOUT.META.DESCRIPTION | Front matter `description` | `Placeholder about page for the Thomas Web Group redesign.` | Search/social summary; 140–160 characters. | Placeholder |
| ABOUT.INTRO.KICKER | Page intro kicker | `[ABOUT PAGE]` | About eyebrow; 1–3 words. | Placeholder |
| ABOUT.INTRO.HEADING | H1 | `[ABOUT PAGE TITLE]` | Introduce company; 3–8 words. | Placeholder |
| ABOUT.INTRO.DESCRIPTION | Intro paragraph | `[ABOUT CONTENT]` | Explain who the company serves and what it does; 30–60 words. | Placeholder |
| ABOUT.EXPERTISE.KICKER | Section kicker | `[AREAS OF EXPERTISE]` | Eyebrow; 2–5 words. | Placeholder |
| ABOUT.EXPERTISE.HEADING | H2 | `Areas of expertise` | Introduces three cards; 3 words. | Existing copy—verify |
| ABOUT.EXPERTISE.01.TITLE | Card 1 H3 | `[EXPERTISE AREA]` | Specific verified competency; 2–5 words. | Placeholder / factual |
| ABOUT.EXPERTISE.01.DESCRIPTION | Card 1 paragraph | `[EXPERTISE DESCRIPTION]` | Supporting explanation; 12–25 words. | Placeholder / factual |
| ABOUT.EXPERTISE.02.TITLE | Card 2 H3 | `[EXPERTISE AREA]` | Specific verified competency; 2–5 words. | Placeholder / factual |
| ABOUT.EXPERTISE.02.DESCRIPTION | Card 2 paragraph | `[EXPERTISE DESCRIPTION]` | Supporting explanation; 12–25 words. | Placeholder / factual |
| ABOUT.EXPERTISE.03.TITLE | Card 3 H3 | `[EXPERTISE AREA]` | Specific verified competency; 2–5 words. | Placeholder / factual |
| ABOUT.EXPERTISE.03.DESCRIPTION | Card 3 paragraph | `[EXPERTISE DESCRIPTION]` | Supporting explanation; 12–25 words. | Placeholder / factual |
| ABOUT.APPROACH.KICKER | Section kicker | `[APPROACH]` | Eyebrow; 1–3 words. | Placeholder |
| ABOUT.APPROACH.HEADING | H2 | `Approach to client work` | Introduces work-principles paragraph; 4 words. | Existing copy—verify |
| ABOUT.APPROACH.BODY | Detail-card paragraph | `[CLIENT WORK APPROACH]` | Explain actual collaboration/process; about 40–80 words. | Placeholder / factual |
| ABOUT.BACKGROUND.KICKER | Section kicker | `[BACKGROUND]` | Eyebrow; 1–3 words. | Placeholder |
| ABOUT.BACKGROUND.HEADING | H2 | `Background and team` | Introduces company/team facts; 3 words. | Existing copy—verify |
| ABOUT.BACKGROUND.01.TITLE | First card H3 | `[BACKGROUND SUMMARY]` | Verifiable company/history topic; 2–6 words. | Placeholder / factual |
| ABOUT.BACKGROUND.01.DESCRIPTION | First card paragraph | `[BACKGROUND DESCRIPTION]` | Company history/credentials; 15–35 words. | Placeholder / factual |
| ABOUT.BACKGROUND.02.TITLE | Second card H3 | `[TEAM SUMMARY]` | Accurate team description; 2–6 words. | Placeholder / factual |
| ABOUT.BACKGROUND.02.DESCRIPTION | Second card paragraph | `[TEAM DESCRIPTION]` | Team roles/experience; 15–35 words. | Placeholder / factual |
| ABOUT.BACKGROUND.03.TITLE | Third card H3 | `[WORK STYLE]` | Accurate working style; 2–5 words. | Placeholder / factual |
| ABOUT.BACKGROUND.03.DESCRIPTION | Third card paragraph | `[WORK STYLE DESCRIPTION]` | Explain how engagements are handled; 15–35 words. | Placeholder / factual |
| ABOUT.CTA.EYEBROW | Closing CTA kicker | `[CTA]` | Lead-in; 1–4 words. | Placeholder |
| ABOUT.CTA.HEADING | Closing CTA H2 | `Get a Project Quote` | Conversion heading; 4 words. | Shared existing copy—verify |
| ABOUT.CTA.BUTTON | Closing CTA | `Get a Project Quote` → `/contact/` | Conversion action; 4 words. | Shared existing copy—verify |

## Contact — `/contact/`

Source: `strategy/contact.njk`. The form is Netlify-enabled (`name="contact"`, POST to `/thank-you/`, hidden `form-name=contact`). Native required/type validation appears in the browser; there are no authored inline validation/error messages in this template.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| CONTACT.META.TITLE | Front matter `title` | `Contact \| Thomas Web Group` | Search title; 50–60 characters. | Existing metadata—verify |
| CONTACT.META.DESCRIPTION | Front matter `description` | `Placeholder contact page for project inquiries.` | Search/social summary; 140–160 characters. | Placeholder |
| CONTACT.INTRO.KICKER | Intro kicker | `[CONTACT PAGE]` | Eyebrow; 1–3 words. | Placeholder |
| CONTACT.INTRO.HEADING | H1 | `[CONTACT PAGE TITLE]` | Invite contact; 3–8 words. | Placeholder |
| CONTACT.INTRO.DESCRIPTION | Intro paragraph | `[CONTACT PAGE INTRODUCTION]` | Explain how to get in touch/what to send; about 20–40 words. | Placeholder |
| CONTACT.INFO.KICKER | Contact panel kicker | `[INQUIRY OPTIONS]` | Eyebrow; 1–3 words. | Placeholder |
| CONTACT.INFO.HEADING | Panel H3 | `Project inquiry` | Name contact route; 2 words. | Existing copy—verify |
| CONTACT.INFO.DESCRIPTION | Panel paragraph | `[CONTACT INTRODUCTION]` | Set response expectations; about 15–30 words. | Placeholder |
| CONTACT.INFO.EMAIL | Contact list item | `Email: raymond@thomaswebgroup.com` | Contact channel; verify address and monitored mailbox. | Existing copy—verify factual |
| CONTACT.INFO.PHONE | Contact list item | `Phone: (423) 225-8787` | Contact channel; verify number. | Existing copy—verify factual |
| CONTACT.INFO.LOCATION | Contact list item | `Location: East Tennessee` | Location; verify public wording. | Existing copy—verify factual |
| CONTACT.FORM.KICKER | Form panel kicker | `[FORM]` | Eyebrow; 1–3 words. | Placeholder |
| CONTACT.FORM.HEADING | Form panel H3 | `Project inquiry form` | Identify form; 3 words. | Existing copy—verify |
| CONTACT.FORM.NAME.LABEL | Label `for=name` | `Name` | Identify required field; 1 word. | Technical/system |
| CONTACT.FORM.NAME.PLACEHOLDER | Input placeholder | `[YOUR NAME]` | Example/input prompt; 2 words. | Placeholder |
| CONTACT.FORM.BUSINESS.LABEL | Label | `Business name` | Identify required field; 2 words. | Technical/system |
| CONTACT.FORM.BUSINESS.PLACEHOLDER | Input placeholder | `[BUSINESS NAME]` | Prompt; 2 words. | Placeholder |
| CONTACT.FORM.EMAIL.LABEL | Label | `Email` | Identify required email field; 1 word. | Technical/system |
| CONTACT.FORM.EMAIL.PLACEHOLDER | Input placeholder | `[EMAIL ADDRESS]` | Prompt; 2 words. | Placeholder |
| CONTACT.FORM.WEBSITE.LABEL | Label | `Website (optional)` | Identify optional website field; 2 words plus qualifier. | Technical/system |
| CONTACT.FORM.WEBSITE.PLACEHOLDER | Input placeholder | `[WEBSITE URL]` | Prompt; 2 words. | Placeholder |
| CONTACT.FORM.SERVICE.LABEL | Label | `Service interest` | Identify required service selector; 2 words. | Technical/system |
| CONTACT.FORM.SERVICE.EMPTY | Disabled selected option | `[SELECT A SERVICE]` | Select prompt; 3 words. | Placeholder |
| CONTACT.FORM.SERVICE.OPTION.WEBSITE | Select option value `website` | `Website Design` | Existing category; verify consistency with offering. | Existing copy—verify |
| CONTACT.FORM.SERVICE.OPTION.CRM | Select option value `crm` | `CRM and Business Systems` | Existing category; verify consistency with page naming. | Existing copy—verify |
| CONTACT.FORM.SERVICE.OPTION.AUTOMATION | Select option value `automation` | `Automation` | Existing category; verify scope. | Existing copy—verify |
| CONTACT.FORM.SERVICE.OPTION.SEO | Select option value `seo` | `SEO and Search Visibility` | Existing category; verify whether this is an active deliverable/page. | Existing copy—verify factual |
| CONTACT.FORM.SERVICE.OPTION.SOCIAL | Select option value `social-media` | `Social Media` | Existing category; verify consistency with service scope. | Existing copy—verify |
| CONTACT.FORM.PROJECT.LABEL | Textarea label | `Project description` | Identify required free-text field; 2 words. | Technical/system |
| CONTACT.FORM.PROJECT.PLACEHOLDER | Textarea placeholder | `[PROJECT DESCRIPTION]` | Explain what details are useful; 2 words currently. | Placeholder |
| CONTACT.FORM.SUBMIT | Submit button | `Submit inquiry` | Submit action; 2 words. | Technical/system |
| CONTACT.FORM.HELPER | Below-form paragraph | `[FORM HELPER TEXT]` | Set expectations about response/privacy; about 10–25 words. | Placeholder |

## Service-detail pages (shared template)

The following page copy is held in YAML front matter on each page and rendered by `strategy/_includes/service-page.njk`. Changing the named front-matter property updates that page’s corresponding shared-template location. The “Included” heading, “Let's Talk” button, and layout are shared template text. No FAQ is rendered on these three pages.

Shared template content (source `strategy/_includes/service-page.njk`):

| Content ID | Pages / routes | Current content | Purpose; length/context | Status |
|---|---|---|---|---|
| SERVICE_TEMPLATE.SECTION_INCLUDED | CRM, Growth & Automation, Social Media | `Included` | Heading above three per-page highlight cards; 1 word. | Existing copy—verify |
| SERVICE_TEMPLATE.CTA | CRM, Growth & Automation, Social Media | `Let's Talk` → `/contact/` | Shared contact action; 2 words. Edit once in the shared include to update all three. | Existing copy—verify |

### CRM & Business Systems — `/crm-business-systems/`

Source values: `strategy/crm-business-systems.njk` front matter object `service`; template locations in `strategy/_includes/service-page.njk`.

| Content ID | Exact field / type | Current content | Purpose; recommended length | Status |
|---|---|---|---|---|
| CRM.META.TITLE | Front matter `title` | `Small Business CRM & HubSpot Consulting \| Thomas Web Group` | SEO title; 50–60 characters. | Existing metadata—verify |
| CRM.META.DESCRIPTION | Front matter `description` | `Organize leads and follow-up with small business CRM setup, HubSpot consulting, migrations, integrations, and reporting.` | Search/social summary; 140–160 characters. | Existing metadata—verify factual |
| CRM.SERVICE.EYEBROW | `service.eyebrow`, rendered section-title H2 | `CRM & BUSINESS SYSTEMS` | Service identifier; 2–5 words. | Existing copy—verify |
| CRM.SERVICE.HEADING | `service.heading`, rendered H1 | `Keep leads and customer follow-up in one place.` | Main customer benefit; 5–12 words. | Existing copy—verify |
| CRM.SERVICE.INTRO | `service.intro`, lead paragraph | `If inquiries are scattered across email, spreadsheets, and apps, we can organize leads in HubSpot or another CRM.` | Explain customer problem and service; 20–35 words. Verify supported platforms/scope. | Existing copy—verify factual |
| CRM.SERVICE.IMAGE_ALT | `service.imageAlt`, image alt | `Business systems supporting a local service company` | Describe image; 8 words. Verify image relevance. | Existing copy—verify |
| CRM.SERVICE.HIGHLIGHT.01.TITLE | `service.highlights[0].title` | `CRM setup and migrations` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| CRM.SERVICE.HIGHLIGHT.01.TEXT | `service.highlights[0].text` | `Set up HubSpot or another CRM, move records, or improve the system you already use.` | Explain deliverable; 15–25 words. | Existing copy—verify factual |
| CRM.SERVICE.HIGHLIGHT.02.TITLE | `service.highlights[1].title` | `Leads and follow-up` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| CRM.SERVICE.HIGHLIGHT.02.TEXT | `service.highlights[1].text` | `See each inquiry's status and automate routine reminders or follow-up.` | Explain deliverable; 10–20 words. | Existing copy—verify factual |
| CRM.SERVICE.HIGHLIGHT.03.TITLE | `service.highlights[2].title` | `Data and connections` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| CRM.SERVICE.HIGHLIGHT.03.TEXT | `service.highlights[2].text` | `Remove duplicate records, connect systems, and report on leads.` | Explain deliverable; 8–18 words. | Existing copy—verify factual |

### Growth & Automation — `/growth-automation/`

Source values: `strategy/growth-automation.njk` front matter object `service`; rendered by shared service template.

| Content ID | Exact field / type | Current content | Purpose; recommended length | Status |
|---|---|---|---|---|
| GROWTH.META.TITLE | Front matter `title` | `Small Business Growth Strategy & Automation \| Thomas Web Group` | SEO title; 50–60 characters. | Existing metadata—verify |
| GROWTH.META.DESCRIPTION | Front matter `description` | `Improve lead generation and reduce manual work with small business workflow automation, system integration, and reporting.` | Search/social summary; 140–160 characters. | Existing metadata—verify factual |
| GROWTH.SERVICE.EYEBROW | `service.eyebrow` | `GROWTH STRATEGY & AUTOMATION` | Service identifier; 2–5 words. | Existing copy—verify |
| GROWTH.SERVICE.HEADING | `service.heading`, H1 | `Spend less time on manual work and missed follow-ups.` | Main customer benefit; 7–12 words. | Existing copy—verify |
| GROWTH.SERVICE.INTRO | `service.intro` | `If staff repeat the same updates or leads wait for follow-up, we can map the process and automate routine steps.` | Explain problem/service; 20–35 words. Verify service capability. | Existing copy—verify factual |
| GROWTH.SERVICE.IMAGE_ALT | `service.imageAlt`, image alt | `Business performance and reporting tools` | Describe image; 5 words. Verify actual image. | Existing copy—verify |
| GROWTH.SERVICE.HIGHLIGHT.01.TITLE | `service.highlights[0].title` | `Find ways to reach customers` | Deliverable title; 3–6 words. | Existing copy—verify factual |
| GROWTH.SERVICE.HIGHLIGHT.01.TEXT | `service.highlights[0].text` | `Review how customers find you and identify changes to lead generation.` | Explain deliverable; 10–20 words. | Existing copy—verify factual |
| GROWTH.SERVICE.HIGHLIGHT.02.TITLE | `service.highlights[1].title` | `Simplify repeat work` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| GROWTH.SERVICE.HIGHLIGHT.02.TEXT | `service.highlights[1].text` | `Automate repetitive tasks such as assigning leads or sending routine notifications.` | Explain deliverable; 10–20 words. | Existing copy—verify factual |
| GROWTH.SERVICE.HIGHLIGHT.03.TITLE | `service.highlights[2].title` | `Connect tools and information` | Deliverable title; 3–6 words. | Existing copy—verify factual |
| GROWTH.SERVICE.HIGHLIGHT.03.TEXT | `service.highlights[2].text` | `Connect business tools and create reports that show lead and sales activity.` | Explain deliverable; 10–20 words. | Existing copy—verify factual |

### Social Media — `/social-media/`

Source values: `strategy/social-media.njk` front matter object `service`; rendered by shared service template.

| Content ID | Exact field / type | Current content | Purpose; recommended length | Status |
|---|---|---|---|---|
| SOCIAL.META.TITLE | Front matter `title` | `Social Media Management for Small Business \| Thomas Web Group` | SEO title; 50–60 characters. | Existing metadata—verify |
| SOCIAL.META.DESCRIPTION | Front matter `description` | `Facebook social media management for small businesses, including content planning, scheduled posts, and optional Instagram and LinkedIn support.` | Search/social summary; 140–160 characters. | Existing copy—verify factual |
| SOCIAL.SERVICE.EYEBROW | `service.eyebrow` | `SOCIAL MEDIA MANAGEMENT` | Service identifier; 2–4 words. | Existing copy—verify |
| SOCIAL.SERVICE.HEADING | `service.heading`, H1 | `Keep your Facebook Page active without doing every post yourself.` | Main benefit; 8–12 words. | Existing copy—verify |
| SOCIAL.SERVICE.INTRO | `service.intro` | `Short on time to plan and publish? We manage Facebook business pages with regular posts and basic graphics.` | Explain problem/service; 15–25 words. | Existing copy—verify factual |
| SOCIAL.SERVICE.IMAGE_ALT | `service.imageAlt`, image alt | `Online presence and digital content for a small business` | Describe image; 9 words. Verify image relevance. | Existing copy—verify |
| SOCIAL.SERVICE.HIGHLIGHT.01.TITLE | `service.highlights[0].title` | `Facebook Page management` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| SOCIAL.SERVICE.HIGHLIGHT.01.TEXT | `service.highlights[0].text` | `Share service updates and business news, with organic audience growth strategies.` | Explain deliverable; 10–20 words. | Existing copy—verify factual |
| SOCIAL.SERVICE.HIGHLIGHT.02.TITLE | `service.highlights[1].title` | `Content and scheduling` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| SOCIAL.SERVICE.HIGHLIGHT.02.TEXT | `service.highlights[1].text` | `Plan posts and basic graphics for Facebook, with optional Instagram and LinkedIn support.` | Explain scope and optional platforms; 12–20 words. | Existing copy—verify factual |
| SOCIAL.SERVICE.HIGHLIGHT.03.TITLE | `service.highlights[2].title` | `Advertising and reporting` | Deliverable title; 2–5 words. | Existing copy—verify factual |
| SOCIAL.SERVICE.HIGHLIGHT.03.TEXT | `service.highlights[2].text` | `Manage Facebook ads and provide monthly performance reports. Advertising spend is separate.` | Explain service and important cost distinction; 10–20 words. Verify ad-management scope and spend policy. | Existing copy—verify factual |

## FAQ — `/faq/`

Source: `strategy/faq.njk`. Questions and answers are stored in the Nunjucks `questions` array as `[question, answer]`; loop index renders all eight accordion items. First answer is expanded by default; other answers are collapsed but present and accessible via accordions.

| Content ID | Data property / type | Exact current content | Purpose; recommended length | Status |
|---|---|---|---|---|
| FAQ.META.TITLE | Front matter `title` | `Small Business Services FAQ \| Thomas Web Group` | SEO title; 50–60 characters. | Existing metadata—verify |
| FAQ.META.DESCRIPTION | Front matter `description` | `Answers about website design, social media management, CRM and HubSpot support, ongoing services, and working with Thomas Web Group.` | Search/social summary; 140–160 characters. | Existing metadata—verify |
| FAQ.PAGE.KICKER | Section H2 | `FAQ` | Short section label; 1 word. | Existing copy—verify |
| FAQ.PAGE.SUBTITLE.1 | First subtitle span | `Websites, Social Media,` | Service context; fragment shown beside second span. | Existing copy—verify |
| FAQ.PAGE.SUBTITLE.2 | Description-title span | `CRM Support` | Completes subtitle; 2 words. | Existing copy—verify |
| FAQ.PAGE.HEADING | Main H1 | `Questions About Working With Us` | Frame the FAQ; 5 words. | Existing copy—verify |
| FAQ.01.QUESTION | `questions[0][0]` | `What services do you offer?` | Service-scope question; preserve plain language. | Existing copy—verify |
| FAQ.01.ANSWER | `questions[0][1]` | `We help with website design, social media management, CRM and business systems, and growth strategy and automation.` | Clarify current offer; verify every listed service. | Existing copy—verify factual |
| FAQ.02.QUESTION | `questions[1][0]` | `Can you help with an existing website?` | Existing-site support question. | Existing copy—verify |
| FAQ.02.ANSWER | `questions[1][1]` | `Yes. We can improve an existing site or plan a redesign, and can also provide hosting and ongoing website care.` | Explain supported options; verify hosting/care availability. | Existing copy—verify factual |
| FAQ.03.QUESTION | `questions[2][0]` | `Which social media platforms do you support?` | Platform-scope question. | Existing copy—verify |
| FAQ.03.ANSWER | `questions[2][1]` | `Facebook is our primary focus. We also support Instagram and LinkedIn.` | State actual supported platforms; verify. | Existing copy—verify factual |
| FAQ.04.QUESTION | `questions[3][0]` | `Can you help with my current CRM?` | CRM support question. | Existing copy—verify |
| FAQ.04.ANSWER | `questions[3][1]` | `Yes. We can set up or improve HubSpot and other existing CRM systems, and help organize lead tracking and follow-up.` | Define platforms and scope; verify. | Existing copy—verify factual |
| FAQ.05.QUESTION | `questions[4][0]` | `Do you provide ongoing support?` | Recurring-service question. | Existing copy—verify |
| FAQ.05.ANSWER | `questions[4][1]` | `Yes. Monthly support can cover website maintenance, social media posting, CRM administration, and automation checks. We agree on the tasks first.` | Clarify recurring scope/process; verify availability and boundaries. | Existing copy—verify factual |
| FAQ.06.QUESTION | `questions[5][0]` | `How does pricing work?` | Pricing question. | Existing copy—verify |
| FAQ.06.ANSWER | `questions[5][1]` | `We do not publish fixed prices. Cost depends on the work involved; we outline scope and cost before work starts.` | Set pricing expectations; verify this policy and proposal process. | Existing copy—verify factual |
| FAQ.07.QUESTION | `questions[6][0]` | `Do you work outside East Tennessee?` | Geographic coverage question. | Existing copy—verify |
| FAQ.07.ANSWER | `questions[6][1]` | `Yes. East Tennessee is our local market, and we also work with businesses nationwide.` | State service area; verify reach. | Existing copy—verify factual |
| FAQ.08.QUESTION | `questions[7][0]` | `What happens after I get in touch?` | Inquiry-process question. | Existing copy—verify |
| FAQ.08.ANSWER | `questions[7][1]` | `We read your message and email you to clarify what you need and arrange a call.` | Set response expectations; verify actual process and timing. | Existing copy—verify factual |
| FAQ.PAGE.CTA.HEADING | Closing H2 | `Have a question about your project?` | Encourage remaining questions; 6 words. | Existing copy—verify |
| FAQ.PAGE.CTA.BUTTON | Closing CTA | `Let's Talk` → `/contact/` | Contact action; 2 words. | Shared existing copy—verify |

## Pricing / ongoing services — `/pricing/`

Source route metadata in `strategy/pricing.njk`; visible body from active include `strategy/_includes/pricing.njk`.

| Content ID | Location / type | Current content | Purpose; recommended length and context | Status |
|---|---|---|---|---|
| PRICING.META.TITLE | Route front matter `title` | `Monthly Business Services \| Thomas Web Group` | SEO title; about 50–60 characters. | Existing metadata—verify |
| PRICING.META.DESCRIPTION | Route front matter `description` | `Ongoing website care, social media management, CRM support, and automation for small businesses. Find support that fits your needs.` | Search/social summary; about 140–160 characters. | Existing metadata—verify factual |
| PRICING.SECTION.HEADING | Include H2 | `Ongoing Support` | Introduce recurring services; 2 words. | Existing copy—verify |
| PRICING.SECTION.SUBTITLE.1 | First span | `Monthly Services` | Context label; 2 words. | Existing copy—verify |
| PRICING.SECTION.SUBTITLE.2 | Second span | `Website, Social, CRM` | List categories; 3 items. | Existing copy—verify |
| PRICING.PLAN.WEBSITE.TITLE | Website Care plan H3 | `Website Care` | Service name; 2 words. | Existing copy—verify |
| PRICING.PLAN.WEBSITE.DESCRIPTION | Plan paragraph | `Hosting, updates, backups, monitoring, minor content changes, and basic traffic reporting.` | Enumerate inclusions; verify exact service boundaries. | Existing copy—verify factual |
| PRICING.PLAN.WEBSITE.CTA | Plan link | `Let's Talk` → `/contact/` | Contact action; 2 words. | Shared existing copy—verify |
| PRICING.PLAN.SOCIAL.TITLE | Social plan H3 | `Social Media Management` | Service name; 3 words. | Existing copy—verify |
| PRICING.PLAN.SOCIAL.DESCRIPTION | Plan paragraph | `Content planning, scheduled Facebook posts, basic creative, optional Instagram support, and performance reporting.` | Enumerate inclusions/platforms; verify scope. | Existing copy—verify factual |
| PRICING.PLAN.SOCIAL.CTA | Plan link | `Let's Talk` → `/contact/` | Contact action; 2 words. | Shared existing copy—verify |
| PRICING.PLAN.CRM.TITLE | CRM plan H3 | `CRM & Automation Support` | Service name; 4 words. | Existing copy—verify |
| PRICING.PLAN.CRM.DESCRIPTION | Plan paragraph | `CRM maintenance, pipeline updates, automation monitoring, data checks, and reporting.` | Enumerate inclusions; verify supported tasks. | Existing copy—verify factual |
| PRICING.PLAN.CRM.CTA | Plan link | `Let's Talk` → `/contact/` | Contact action; 2 words. | Shared existing copy—verify |
| PRICING.SCOPE.NOTE | `.service-summary` paragraph | `Monthly work is scoped to agreed tasks. One-time projects are also available.` | Clarify engagement structure; verify policy and availability. | Existing copy—verify factual |

## Privacy Policy — `/privacy-policy/`

Source: `strategy/privacy-policy.njk`. Legal/policy text requires business/legal review; inventory is not legal approval.

| Content ID | Location / type | Exact current content | Purpose; recommended length/context | Status |
|---|---|---|---|---|
| PRIVACY.META.TITLE | Front matter `title` | `Privacy Policy \| Thomas Web Group` | SEO title; about 50–60 characters. | Existing metadata—verify |
| PRIVACY.META.DESCRIPTION | Front matter `description` | `Thomas Web Group privacy policy and SMS messaging terms.` | Search/social summary; 140–160 characters. | Existing metadata—verify |
| PRIVACY.PAGE.SECTION_LABEL | Section H2 | `Privacy` | Page section label; 1 word. | Existing copy—verify |
| PRIVACY.PAGE.SUBTITLE.1 | First subtitle span | `Thomas Web Group` | Company identifier. | Existing copy—verify |
| PRIVACY.PAGE.SUBTITLE.2 | Second span | `Privacy Policy` | Policy identifier; 2 words. | Existing copy—verify |
| PRIVACY.PAGE.H1 | Main H1 | `Privacy Policy` | Document title; 2 words. | Technical/legal |
| PRIVACY.INTRO | Opening paragraph | `Thomas Web Group ("we," "us," or "our") respects your privacy and is committed to protecting your personal information. This Privacy Policy explains how we collect, use, store, and share information when you visit our website, contact us, use our services, or opt in to receive SMS messages.` | State policy scope; verify actual practices with owner/legal counsel. | Existing copy—legal review |
| PRIVACY.COLLECT.HEADING | H2 | `Information We Collect` | Section heading. | Technical/legal |
| PRIVACY.COLLECT.BODY | Paragraph | `We may collect your name, email address, phone number, business name, website address, form submissions, communications, SMS consent, IP address, browser and device type, pages visited, referral source, and general website usage information.` | Disclose actual data collected; verify form, analytics, logs, and vendor practices. | Existing copy—legal review |
| PRIVACY.USE.HEADING | H2 | `How We Use Your Information` | Section heading. | Technical/legal |
| PRIVACY.USE.BODY | Paragraph | `We may use information to operate and improve our business and website, respond to inquiries, provide services, prepare quotes, communicate with customers, send opted-in SMS messages, maintain records, improve performance, and protect against fraud or abuse.` | Explain purposes; verify all listed uses. | Existing copy—legal review |
| PRIVACY.COOKIES.HEADING | H2 | `Cookies and Analytics` | Section heading. | Technical/legal |
| PRIVACY.COOKIES.BODY | Paragraph | `Our website may use cookies or similar technologies to understand usage, measure performance, and improve the site. Third-party analytics or infrastructure providers may process limited technical information on our behalf.` | Disclose actual tools/technologies; verify what is installed. | Existing copy—legal review |
| PRIVACY.SHARING.HEADING | H2 | `Data Sharing` | Section heading. | Technical/legal |
| PRIVACY.SHARING.BODY | Paragraph | `Customer data is not shared with third parties for promotional or marketing purposes. Mobile opt-in and consent are never shared with anyone for any purpose. We may share information with providers that help operate our business, or when required by law.` | Describe sharing and SMS consent; verify providers and absolute claims. | Existing copy—legal review |
| PRIVACY.RETENTION.HEADING | H2 | `Data Retention and Security` | Section heading. | Technical/legal |
| PRIVACY.RETENTION.BODY | Paragraph | `We retain information as reasonably necessary for the purposes described here, business records, disputes, or legal obligations. We use reasonable safeguards, but no internet transmission or electronic storage method can be guaranteed completely secure.` | Disclose retention/security practices; verify actual schedule and controls. | Existing copy—legal review |
| PRIVACY.PAYMENTS.HEADING | H2 | `Payments` | Section heading. | Technical/legal |
| PRIVACY.PAYMENTS.BODY | Paragraph | `If you purchase services from Thomas Web Group, payment information may be processed by a third-party payment processor. Thomas Web Group does not generally store full payment card information.` | Explain payment processing; verify payment provider and storage practices. | Existing copy—legal review |
| PRIVACY.CHILDREN.HEADING | H2 | `Children's Privacy` | Section heading. | Technical/legal |
| PRIVACY.CHILDREN.BODY | Paragraph | `Our website and services are intended for businesses and adults and are not directed toward children under 13. We do not knowingly collect personal information from children under 13.` | State audience/data practice; verify policy/legal applicability. | Existing copy—legal review |
| PRIVACY.SMS.HEADING | H2 | `Messaging Program Terms` | Section heading. | Technical/legal |
| PRIVACY.SMS.BODY | Paragraph | `Customer care messages may be sent from (423) 225-8787. Text STOP to unsubscribe or HELP for assistance. Message and data rates may apply and frequency varies. Carriers are not liable for delayed or undelivered messages.` | SMS program disclosure; verify number, enrollment/consent, support flow, cadence, and required terms. | Existing copy—legal review |
| PRIVACY.CHOICES.HEADING | H2 | `Your Choices` | Section heading. | Technical/legal |
| PRIVACY.CHOICES.BODY | Paragraph | `You may contact us to ask about, correct, or request deletion of your information when appropriate, opt out of non-required communications, or withdraw SMS consent by texting STOP.` | Explain rights/choices; verify operational ability and legal requirements. | Existing copy—legal review |
| PRIVACY.CHANGES.HEADING | H2 | `Changes to This Privacy Policy` | Section heading. | Technical/legal |
| PRIVACY.CHANGES.BODY | Paragraph | `We may update this policy to reflect changes to our business, website, services, or legal requirements. The current version will be posted here.` | Explain update process; verify any effective-date requirement. | Existing copy—legal review |
| PRIVACY.CONTACT.HEADING | H2 | `Contact Us` | Section heading. | Technical/legal |
| PRIVACY.CONTACT.BODY | Paragraph links/text | `Thomas Web Group`; `raymond@thomaswebgroup.com`; `(423) 225-8787` | Policy contact channel; verify entity and contact details. | Existing copy—verify factual/legal |

## Terms — `/terms/`

Source: `strategy/terms.njk`. Existing legal copy needs owner/legal review; it is not approved simply because complete text is present.

| Content ID | Location / type | Exact current content | Purpose; recommended length/context | Status |
|---|---|---|---|---|
| TERMS.META.TITLE | Front matter `title` | `Website Terms \| Thomas Web Group` | SEO title; 50–60 characters. | Existing metadata—verify |
| TERMS.META.DESCRIPTION | Front matter `description` | `Terms governing use of the Thomas Web Group public website.` | Search/social summary; 140–160 characters. | Existing metadata—verify |
| TERMS.SECTION.LABEL | Section H2 | `Terms` | Section label; 1 word. | Technical/legal |
| TERMS.SUBTITLE.1 | First span | `Website` | Document context. | Technical/legal |
| TERMS.SUBTITLE.2 | Second span | `Terms` | Document context. | Technical/legal |
| TERMS.H1 | Main H1 | `Website Terms` | Document title; 2 words. | Technical/legal |
| TERMS.INTRO | Opening paragraph | `These terms govern use of the Thomas Web Group public website. They do not replace project contracts, proposals, statements of work, or hosting agreements.` | Define document scope; verify relationship with actual agreements. | Existing copy—legal review |
| TERMS.USE.HEADING | H2 | `Website Use` | Section heading. | Technical/legal |
| TERMS.USE.BODY | Paragraph | `Use this website lawfully and do not interfere with its operation, security, or availability.` | State use rule; legal review. | Existing copy—legal review |
| TERMS.INFORMATION.HEADING | H2 | `Informational Nature of Website Content` | Section heading. | Technical/legal |
| TERMS.INFORMATION.BODY | Paragraph | `Website content is general information about our work and offer. A quote or project agreement controls the details of a particular engagement.` | Clarify informational content/engagement terms. | Existing copy—legal review |
| TERMS.IP.HEADING | H2 | `Intellectual Property on ThomasWebGroup.com` | Section heading. | Technical/legal |
| TERMS.IP.BODY | Paragraph | `Thomas Web Group and its licensors retain rights in the website's original text, design, branding, and other materials unless stated otherwise. Do not copy or reuse them without permission.` | Explain site IP; confirm rights/licensors. | Existing copy—legal review |
| TERMS.LINKS.HEADING | H2 | `Third-Party Links` | Section heading. | Technical/legal |
| TERMS.LINKS.BODY | Paragraph | `Links to third-party websites are provided for convenience. Thomas Web Group is not responsible for their content, availability, or policies.` | Explain external-link disclaimer. | Existing copy—legal review |
| TERMS.NO_GUARANTEE.HEADING | H2 | `No Guarantee of Search Rankings, Leads, Revenue, or Business Results` | Section heading; long, wraps in layout. | Technical/legal |
| TERMS.NO_GUARANTEE.BODY | Paragraph | `We do not guarantee search rankings, leads, revenue, traffic, or other business results. Website performance depends on many factors outside the website alone.` | Define results disclaimer; verify alignment with service claims/contracts. | Existing copy—legal review |
| TERMS.ACCURACY.HEADING | H2 | `Accuracy and Updates` | Section heading. | Technical/legal |
| TERMS.ACCURACY.BODY | Paragraph | `We work to keep information current, but content may change without notice and may contain errors or omissions.` | Explain updates/accuracy. | Existing copy—legal review |
| TERMS.LIABILITY.HEADING | H2 | `Limitation of Liability` | Section heading. | Technical/legal |
| TERMS.LIABILITY.BODY | Paragraph | `To the extent permitted by law, Thomas Web Group will not be liable for indirect, incidental, special, consequential, or lost-profit damages arising from use of this public website.` | Limitation clause; legal counsel review. | Existing copy—legal review |
| TERMS.CHANGES.HEADING | H2 | `Changes to These Terms` | Section heading. | Technical/legal |
| TERMS.CHANGES.BODY | Paragraph | `We may update these terms by posting a revised version on this page. Continued use after an update means you accept the revised terms.` | Explain update process; legal review. | Existing copy—legal review |
| TERMS.CONTACT.HEADING | H2 | `Contact Information` | Section heading. | Technical/legal |
| TERMS.CONTACT.BODY | Paragraph links/text | `Thomas Web Group`; `raymond@thomaswebgroup.com`; `(423) 225-8787` | Contact for terms questions; verify entity/details. | Existing copy—verify factual/legal |

## Thank-you — `/thank-you/`

Source: `strategy/thank-you.njk`. This is a form success destination and has `noindex: true`.

| Content ID | Location / type | Current content | Purpose; length/context | Status |
|---|---|---|---|---|
| THANKYOU.META.TITLE | Front matter `title` | `Project Request Received \| Thomas Web Group` | Browser title; 50–60 characters. | Existing metadata—verify |
| THANKYOU.META.DESCRIPTION | Front matter `description` | `Confirmation for a Thomas Web Group business or website project inquiry.` | Metadata; 140–160 characters; page is noindex. | Existing metadata—verify |
| THANKYOU.H1 | Main H1 | `Thanks, we received your message.` | Confirm successful submission; 6 words. | Technical/system |
| THANKYOU.BODY | Lead paragraph | `We'll reply by email to discuss what you need.` | Set response expectation; verify actual channel/process. | Existing copy—verify factual |
| THANKYOU.CTA.HOME | Button | `Return Home` → `/` | Recovery/navigation; 2 words. | Technical/system |
| THANKYOU.CTA.WORK | Button | `View Our Work` → `/work/` | Next step; 3 words. | Existing copy—verify |

## Not found — `/404.html`

Source: `strategy/404.njk`. `noindex: true`; emitted by Eleventy as the 404 page.

| Content ID | Location / type | Current content | Purpose; length/context | Status |
|---|---|---|---|---|
| NOTFOUND.META.TITLE | Front matter `title` | `Page Not Found \| Thomas Web Group` | Browser title; about 50–60 characters. | Technical/system |
| NOTFOUND.META.DESCRIPTION | Front matter `description` | `The requested Thomas Web Group page could not be found.` | Metadata; page is noindex. | Technical/system |
| NOTFOUND.H1 | Main H1 | `Page not found` | Explain error; 3 words. | Technical/system |
| NOTFOUND.BODY | Lead paragraph | `That address doesn't match a page on this site.` | Explain error; 9 words. | Technical/system |
| NOTFOUND.CTA.HOME | Button | `Home` → `/` | Recovery link; 1 word. | Technical/system |
| NOTFOUND.CTA.WEBSITES | Button | `Website Design` → `/websites/` | Recovery link; 2 words. | Existing copy—verify |
| NOTFOUND.CTA.CONTACT | Button | `Let's Talk` → `/contact/` | Contact option; 2 words. | Shared existing copy—verify |

## SEO field audit

For routes using `strategy/_includes/base.njk`, `<title>` and Open Graph title use the page front-matter `title`; meta description and Open Graph description use front-matter `description`. `404.njk` does not set `layout: 'base.njk'`, so its front-matter title, description, `noindex`, Open Graph tags, shared header/footer, and other base metadata are not rendered in the emitted 404 HTML. No active route sets a `canonical` value, so the base layout emits no canonical link. The base layout emits `og:type=website`; it does not emit `og:image`, Twitter card fields, or a separate social description. H1 values are listed as page content above. Only `/thank-you/` renders `noindex, nofollow`; the `/404.html` front-matter `noindex: true` is not emitted because that page has no base layout.

| Route | Title tag / OG title source | Meta description / OG description source | H1 rendered | Canonical | Relevant image alt |
|---|---|---|---|---|---|
| `/` | `Thomas Web Group \| Websites & Business Growth Solutions` | `Websites, Google and AI search visibility, social media, and business automation for small businesses ready to attract more customers and improve operations.` | `Get Found. Win More Customers. Run Your Business Better.` | Missing | `Laptop showcase image placeholder. Add an approved Thomas Web Group project screenshot.` (ARIA label on role=img, not `<img>`) |
| `/websites/` | `Websites \| Thomas Web Group` | `Placeholder service page for website design and development.` | `[WEBSITE SERVICE INTRO]` | Missing | No image in page body |
| `/work/` | `Work \| Thomas Web Group` | `Placeholder portfolio page for selected Thomas Web Group work.` | `[WORK PAGE HEADING]` | Missing | Thumbnail placeholders are text, not images |
| `/work/dad-cuts-grass/` | `Dad Cuts Grass Website Project \| Thomas Web Group` | `A lawn-care website with service details and a custom online quote form for Dad Cuts Grass.` | `Dad Cuts Grass` | Missing | `Dad Cuts Grass website project` |
| `/work/smoky-mountain-acres/` | `Smoky Mountain Acres Website Project \| Thomas Web Group` | `A farm website for Smoky Mountain Acres, with pages for farm tours, livestock, local products, and educational articles.` | `Smoky Mountain Acres` | Missing | `Smoky Mountain Acres website project` |
| `/about/` | `About \| Thomas Web Group` | `Placeholder about page for the Thomas Web Group redesign.` | `[ABOUT PAGE TITLE]` | Missing | No image in page body |
| `/contact/` | `Contact \| Thomas Web Group` | `Placeholder contact page for project inquiries.` | `[CONTACT PAGE TITLE]` | Missing | No image in page body |
| `/crm-business-systems/` | `Small Business CRM & HubSpot Consulting \| Thomas Web Group` | `Organize leads and follow-up with small business CRM setup, HubSpot consulting, migrations, integrations, and reporting.` | `Keep leads and customer follow-up in one place.` | Missing | `Business systems supporting a local service company` |
| `/growth-automation/` | `Small Business Growth Strategy & Automation \| Thomas Web Group` | `Improve lead generation and reduce manual work with small business workflow automation, system integration, and reporting.` | Missing | `Business performance and reporting tools` |
| `/social-media/` | `Social Media Management for Small Business \| Thomas Web Group` | `Facebook social media management for small businesses, including content planning, scheduled posts, and optional Instagram and LinkedIn support.` | Missing | `Online presence and digital content for a small business` |
| `/faq/` | `Small Business Services FAQ \| Thomas Web Group` | `Answers about website design, social media management, CRM and HubSpot support, ongoing services, and working with Thomas Web Group.` | `Questions About Working With Us` | Missing | No image in page body |
| `/pricing/` | `Monthly Business Services \| Thomas Web Group` | `Ongoing website care, social media management, CRM support, and automation for small businesses. Find support that fits your needs.` | No H1; first heading is `Ongoing Support` (H2) | Missing | No image in page body |
| `/privacy-policy/` | `Privacy Policy \| Thomas Web Group` | `Thomas Web Group privacy policy and SMS messaging terms.` | `Privacy Policy` | Missing | No image in page body |
| `/terms/` | `Website Terms \| Thomas Web Group` | `Terms governing use of the Thomas Web Group public website.` | `Website Terms` | Missing | No image in page body |
| `/thank-you/` | `Project Request Received \| Thomas Web Group` | `Confirmation for a Thomas Web Group business or website project inquiry.` | `Thanks, we received your message.` | Missing | No image in page body |
| `/404.html` | Front matter value not rendered | Front matter value not rendered | `Page not found` | Missing | No image in page body |

## Hidden, responsive, and state-dependent content

- Header navigation and the quote link are present in the mobile menu; the menu is initially collapsed below the mobile breakpoint. The control changes its accessible label from `Open navigation` to `Close navigation`; that wording is in `strategy/assets/js/main.js`.
- The FAQ route renders all eight answers in Bootstrap accordion markup. The first answer is expanded by default; seven answers are initially collapsed, not absent.
- The contact form's placeholders appear only while their fields are empty. Its empty service prompt is a disabled selected option; the five service options appear when the selector opens.
- Native browser validation is driven by required fields and `type=email` / `type=url`. Error wording is browser-generated/localized rather than authored in project files.
- On successful contact form submission the action targets `/thank-you/`. No custom failure-state or inline error copy is defined in this form.
- The home laptop visual includes placeholder wording inside its screen and an accessible `aria-label`; there is no actual project screenshot currently referenced there.

## Content stored in data structures / reusable parameters

| Source structure | Active use | Exact content controls |
|---|---|---|
| YAML front matter in `strategy/crm-business-systems.njk`, `strategy/growth-automation.njk`, and `strategy/social-media.njk` | Each route includes `strategy/_includes/service-page.njk` | `title`, `description`, and `service.eyebrow`, `service.heading`, `service.intro`, `service.image`, `service.imageAlt`, `service.highlights[]` (`title`, `text`, `icon`). Copy fields are mapped to IDs in the service-page sections above; `icon` and `image` are implementation/assets, not copy. |
| Nunjucks variable `questions` in `strategy/faq.njk` | Iterated into the eight FAQ accordion items | Each element is `[question, answer]`; index `[0]` controls question and `[1]` answer. IDs `FAQ.01`–`FAQ.08` map to array order. |
| Route front matter in all page `.njk` files | `strategy/_includes/base.njk` reads metadata | `title`, `description`, `permalink`, and optional `noindex`; `canonical` is supported by the layout but not populated in active front matter. |
| Markup in `strategy/_includes/header.njk` / `footer.njk` | Shared base layout includes both on each base-layout route | Global text entries above are literal shared markup, not per-page parameters. Edit their source once to affect all rendered pages. |
| Markup in `strategy/_includes/pricing.njk` | Included only by `strategy/pricing.njk` | Plan names, descriptions, CTA labels, section headings and note are literal content in the include; it is not JSON/YAML data. |
| Project/service/work/home/about/contact templates | Rendered from literal markup | Cards and page content are static Nunjucks/HTML; no active data collection or external copy data file was found for these sections. |

No populated Eleventy `_data` directory or `.11tydata.*` file was found. The vendor Bootstrap Icons JSON file is icon catalog data, not site copy. The service front matter and FAQ array above are the active structured content sources.

## Information Needed From Business Owner

- **Company identity:** approved brand styling and punctuation; company background, start date/history, team size/roles, qualifications, and preferred first-person voice.
- **Services:** exact deliverables, supported platforms, boundaries, project process, hosting/support responsibilities, SEO scope, social channels, ad-management scope, automation tools, CRM expertise, and ongoing-service availability.
- **Project evidence:** which client projects may be named; project status; approved screenshots/logos; actual platforms/technologies; scope delivered; measurable outcomes with sources; live URLs; and permission to show each project.
- **Testimonials:** confirm exact quote wording, client identity/preferred attribution, permission to publish, and substantiation for outcome/conversion statements.
- **Contact and coverage:** verify Raymond's public name/title, monitored email, phone/SMS number, East Tennessee wording, nationwide service claim, and expected response timing.
- **Pricing/retainers:** confirm included tasks, exclusions, cadence, fees or quote policy, ad-spend handling, one-time project availability, and commitments in the monthly service descriptions.
- **Privacy practices:** actual form fields and storage/retention, analytics/cookies, processors/vendors, data-sharing practices, payment provider, security language, and rights request handling.
- **SMS program:** whether SMS is actually offered; consent and enrollment flow; exact sending number; message types/frequency; STOP/HELP handling; rates/carrier wording; and required compliance language.
- **Legal terms:** confirm the contracting entity, website IP ownership/licensing, third-party link practices, guarantees/disclaimers, liability language, governing law if needed, and effective/update date with legal counsel.
- **Visual assets:** approved image for homepage laptop and work thumbnails; verify every service/project image against its current alt text.

Do not infer any of these facts from placeholder wording or treat current claims as verified.

## Ambiguous, missing, or owner-dependent content

1. Websites, Work, About, Contact, and Footer retain explicit bracketed copy placeholders. The homepage's copy v1 has been applied, but its device screenshot request remains unresolved.
2. Work index has four generic thumbnail text blocks; no project card links directly to either named case-study route (all four go to `/contact/`). The named detail routes are nevertheless emitted by the build.
3. Homepage, Websites, and Work have repeated project cards with no project identity. The writer cannot supply factual client names, status, platform tags, or results without owner-provided project records.
4. The Websites intro placeholder is spelled `[WEBSTIES PAGE DESCRIPTION]` in source. Preserve its Content ID when replacing it; the typo is source text, not a recommendation.
5. `/pricing/` has a title/body but no H1 and is not in the global header/footer navigation. It is still generated and accessible by direct route.
6. `/crm-business-systems/`, `/growth-automation/`, `/social-media/`, `/faq/`, `/pricing/`, `/privacy-policy/`, `/terms/`, `/thank-you/`, and individual projects are also outside the five-item global header. They are active generated routes.
7. There is no explicit policy approval, testimonial release, results evidence, or formal copy approval in the repository. Existing long-form legal text and project quotes remain review items.
8. Homepage Copy v1 supplies a summary for Dad Cuts Grass that is explicitly pending verification. The suggested Eleventy / Decap CMS / Netlify tags for Smoky Mountain Acres also need project-stack confirmation. The third homepage project is withheld until a real project, scope, and publication status are confirmed.

## Obsolete/unreferenced content (not counted as active copy)

The following files under `strategy/_includes/` are not included by any active route/layout according to the active Nunjucks include references: `about.njk`, `call-to-action.njk`, `call-to-action2.njk`, `contact.njk`, `faq.njk`, `hero.njk`, `services.njk`, `steps.njk`, `testimonials.njk`, `what-we-offer.njk`, and `work.njk`. They contain legacy copy/placeholders (including an older contact form and FAQ), but none is rendered by the current route set. Do not use them as the authority for active page text unless the implementation later reactivates them.

## Inventory counts

Counting method: one content item is one separately editable user-facing copy field or metadata value on an active route. Repeated card fields are separate items. Shared component wording is counted once per source field, rather than once per page/rendered repetition. Technical metadata omissions are counted separately from present content.

- Active routes inventoried: **16**
- Content items with unique Content IDs: **395** (this counts the separately numbered repeated card/tag copy fields and shared-source fields once; held/unrendered third-project fields and removed status/unknown-technology fields are excluded).
- Items marked Placeholder: **118** content items.
- Existing non-placeholder copy/metadata requiring review or approval: **213** content items, including the supplied Homepage Copy v1 draft.
- Shared content elements documented once: **23 reusable UI text fields** (21 global brand/header/footer items and two shared service-template items; shared metadata mechanics are excluded).
- Missing SEO fields: **36 requested route-level fields**—16 canonical URL values, 16 `og:image` values, and rendered title, meta description, Open Graph title, and Open Graph description on `/404.html`. The 404 route also lacks rendered robots metadata because it has no base layout. All other routes have title and description tags; all but `/pricing/` have an H1. No separate Twitter-card fields are emitted.
- Items requiring factual input: **10 owner-information groups**, listed in “Information Needed From Business Owner.”
