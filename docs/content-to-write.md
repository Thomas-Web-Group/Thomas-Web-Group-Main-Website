# Thomas Web Group — Content Replacement Worksheet

> **Implementation note (2026-10-10):** This worksheet is the pre-implementation copywriting draft. Supplied content has since been implemented; see `content-implementation-report.md` for the current implementation and `content-needs-owner-review.md` for outstanding verification items.

Use the stable Content IDs when returning copy. Keep the page, destination, factual limits, and approximate length with each item. Where a separate length is not stated (for example, a short button label), keep the replacement close to the current component's length; the inventory contains full length/context notes. `[NEW COPY]` is an intentional blank for the writer; do not copy it into the site. Do not invent project results, credentials, service promises, legal claims, or business facts. See `content-inventory.md` for source mapping, all SEO fields, status detail, and the full audit.

## Shared components — edit once at source

These elements appear on multiple pages. Do not create separate per-page variants unless the business owner explicitly wants different wording. Header/footer copy is defined once in the shared includes and changing it there propagates to pages that use the shared base layout.

### Header (`strategy/_includes/header.njk`)

- **GLOBAL.BRAND** — Brand wordmark: `Thomas Web Group` (header displays trailing period). Writing objective: confirm approved brand spelling/punctuation. Length: name only. Fact needed: brand style approval. **[NEW COPY]** `[confirm brand]`
- **GLOBAL.HEADER.NAV.HOME** — Navigation label: `01 Home`. Objective: preserve concise route label. **[NEW COPY]** `[retain or approved label]`
- **GLOBAL.HEADER.NAV.WEBSITES** — `02 Websites`. **[NEW COPY]** `[retain or approved label]`
- **GLOBAL.HEADER.NAV.WORK** — `03 Work`. **[NEW COPY]** `[retain or approved label]`
- **GLOBAL.HEADER.NAV.ABOUT** — `04 About`. **[NEW COPY]** `[retain or approved label]`
- **GLOBAL.HEADER.NAV.CONTACT** — `05 Contact`. **[NEW COPY]** `[retain or approved label]`
- **GLOBAL.HEADER.QUOTE_CTA** — Desktop and mobile CTA: `Get a Project Quote` → `/contact/`. Objective: one clear conversion action; 2–5 words. **[NEW COPY]** `[approved shared CTA]`
- **GLOBAL.HEADER.BRAND_ACCESSIBLE_NAME** — `Thomas Web Group home`. Objective: accessible logo-link name; technical, usually retain. **[NEW COPY]** `[confirm accessible name]`
- **GLOBAL.HEADER.MENU_OPEN / GLOBAL.HEADER.MENU_CLOSE** — `Open navigation` / `Close navigation`. Objective: clearly identify mobile menu state; technical. **[NEW COPY]** `[confirm accessible labels]`

### Footer (`strategy/_includes/footer.njk`)

Pages: all base-layout pages. Edit each source field once; same footer is rendered site-wide.

- **GLOBAL.FOOTER.INTRO** — Current: `Thomas Web Group helps small businesses improve their websites, online visibility, customer management, and everyday operations through practical digital solutions.` Objective: concise company/service summary; 20 words. Copy v1 applied; review for factual accuracy.
- **GLOBAL.FOOTER.EXPLORE** — Current: `Explore`; heading above Home / Websites / Work. Objective: retain or name group; 1–2 words. **[NEW COPY]**
- **GLOBAL.FOOTER.COMPANY** — Current: `Company`; heading above About / Contact / quote CTA. Objective: retain or name group; 1–2 words. **[NEW COPY]**
- **GLOBAL.FOOTER.CONTACT_HEADING** — Current: `Contact`. Objective: retain concise heading. **[NEW COPY]**
- **GLOBAL.FOOTER.EMAIL** — Current: `raymond@thomaswebgroup.com`. Objective: verify public contact inbox, not rewrite. Fact needed: confirmed monitored email. **[NEW COPY]** `[verified email]`
- **GLOBAL.FOOTER.PHONE** — Current: `(423) 225-8787`. Objective: verify public number. Fact needed: confirmed phone/SMS number. **[NEW COPY]** `[verified number]`
- **GLOBAL.FOOTER.LOCATION** — Current: `East Tennessee`. Objective: confirm service-area phrasing. Fact needed: local market/geographic claim. **[NEW COPY]** `[verified location wording]`
- **GLOBAL.FOOTER.QUOTE_LINK** — Current: `Get a Project Quote` → `/contact/`. Same copy intent as header. **[NEW COPY]** `[use approved shared CTA]`
- **GLOBAL.FOOTER.YEAR** — Current: `© 2024 Thomas Web Group`. Objective: confirm copyright holder and whether year should be fixed/current. **[NEW COPY]** `[verified copyright line]`
- **GLOBAL.FOOTER.LEGAL** — Current: `[LEGAL FOOTER TEXT]`. Objective: supply approved legal/company note; 3–15 words. Facts needed: exact legal notice and any required link. **[NEW COPY]**
- **GLOBAL.SCROLL_TOP** — Current: arrow icon only; no accessible name. Objective: supply concise accessible name if retained; 2–5 words. **[NEW COPY]** `[accessible label]`

### Shared service-detail template

Used by CRM & Business Systems, Growth & Automation, and Social Media. The shared template is `strategy/_includes/service-page.njk`; each route’s per-service content is in its front matter and is listed under that route below.

- **SERVICE_TEMPLATE.SECTION_INCLUDED** — Current: `Included`. Objective: retain or clarify service highlights heading; 1–3 words. **[NEW COPY]**
- **SERVICE_TEMPLATE.CTA** — Current: `Let's Talk` → `/contact/`. Objective: shared contact CTA; 1–3 words. **[NEW COPY]**

## Home — `/`

Source: `strategy/index.njk`. Keep hero heading, supporting copy, and paired CTAs working together. Laptop artwork is currently an explicit asset placeholder.

- **HOME.META.TITLE** — Current: `Thomas Web Group | Websites & Business Growth Solutions`. Objective: accurate, concise brand/page title; 55 characters. Copy v1 applied; review before approval.
- **HOME.META.DESCRIPTION** — Current: `Websites, Google and AI search visibility, social media, and business automation for small businesses ready to attract more customers and improve operations.` Objective: summarize the actual audience, offer, and value; 157 characters. Copy v1 applied; review factual claims before approval.

### Hero

- **HOME.HERO.EYEBROW** — Current: `Digital Growth & Business Systems`. Objective: identify the agency/category; 5 words. Copy v1 applied; review before approval.
- **HOME.HERO.HEADING** — Current: `Get Found. Win More Customers. Run Your Business Better.` Objective: primary small-business benefit/value proposition; 9 words, suited to a large hero heading. Copy v1 applied; review before approval.
- **HOME.HERO.DESCRIPTION** — Current: `We help small businesses build a stronger online presence, turn more inquiries into customers, and spend less time on repetitive work through better websites, marketing, and connected systems.` Objective: explain audience, services, and outcome; 28 words. Copy v1 applied; review factual claims before approval.
- **HOME.HERO.CTA_WORK** — Current: `View Our Work` → `/work/`. Objective: browse evidence; 3 words. Copy v1 applied.
- **HOME.HERO.CTA_SERVICES** — Current: `Explore Websites` → `/websites/`. Objective: move toward website services; 2 words. Copy v1 applied.
- **HOME.HERO.IMAGE_ALT** — Current: `Laptop showcase image placeholder. Add an approved Thomas Web Group project screenshot.` Objective: describe actual approved visual; 5–15 words. Fact needed: approved project screenshot/which project it depicts. **[NEW COPY]** `[approved, accurate image alt]`
- **HOME.HERO.SCREEN** — Current: `[APPROVED PROJECT SCREENSHOT NEEDED]`. Objective: asset selection, not marketing copy. Fact needed: approved project screenshot/device art. **[NEW COPY]** `[approved screenshot asset; no invented client work]`

### Featured projects

- **HOME.PROJECTS.KICKER** — Current: `Our Work`. Objective: short section eyebrow; 2 words. Copy v1 applied.
- **HOME.PROJECTS.HEADING** — Current: `Real Businesses. Practical Solutions.` Objective: introduce project examples; 4 words. Copy v1 applied.

Two project cards are currently shown. No third example is included until the business owner confirms a real project, its scope, and publication status.

- **HOME.PROJECTS.01.TITLE** — Current: `Smoky Mountain Acres`. Objective: identify the project; 3 words. Copy v1 applied.
- **HOME.PROJECTS.01.SUMMARY** — Current: `A custom farm website with livestock listings, availability tracking, and a simple content management system that makes keeping the website updated easier.` Objective: describe delivered scope; 22 words. Verify project details before approval.
- **HOME.PROJECTS.01.TECH.1 / .TECH.2 / .TECH.3** — Current tags: `Eleventy` / `Decap CMS` / `Netlify`. Suggested technologies from copy v1; confirm the project stack before publication.
- **HOME.PROJECTS.01.CTA** — Current: `View Project` → `/work/`. Objective: project navigation; 2 words. Copy v1 applied.
- **HOME.PROJECTS.02.TITLE** — Current: `Dad Cuts Grass`. Objective: identify the project; 3 words. Copy v1 applied.
- **HOME.PROJECTS.02.SUMMARY** — Current: `A lawn care website designed to make it easier for customers to explore services and request quotes online.` Objective: describe project purpose; 18 words. **Pending verification** per copy v1; confirm project scope before publication.
- **HOME.PROJECTS.02.CTA** — Current: `View Project` → `/work/`. Objective: project navigation; 2 words. Copy v1 applied.

### Additional services and closing CTA

- **HOME.SERVICES.KICKER** — Current: `Beyond Websites`. Objective: section eyebrow; 2 words. Copy v1 applied.
- **HOME.SERVICES.HEADING** — Current: `More Ways to Grow Your Business`. Objective: introduce cards; 6 words. Copy v1 applied.
- **HOME.SERVICES.01.TITLE / .DESCRIPTION** — Current: `Social Media & Online Visibility` / `Stay visible to potential customers with consistent social media activity and a stronger presence where people search for businesses.` Objective: identify the service and its value; 5-word heading and 18-word description. Copy v1 applied; verify service scope.
- **HOME.SERVICES.02.TITLE / .DESCRIPTION** — Current: `Customer & Lead Management` / `Keep customer information organized, track potential jobs, and follow up with leads before opportunities slip through the cracks.` Objective: identify the service and its value; 4-word heading and 18-word description. Copy v1 applied; verify service scope.
- **HOME.SERVICES.03.TITLE / .DESCRIPTION** — Current: `Business Automation & Reporting` / `Connect your existing tools, reduce repetitive administrative work, and get clearer information about how your business is performing.` Objective: identify the service and its value; 4-word heading and 18-word description. Copy v1 applied; verify service scope.
- **HOME.CTA.EYEBROW** — Current: `Let's Talk Business`. Objective: short lead-in; 3 words. Copy v1 applied.
- **HOME.CTA.HEADING** — Current: `What's Holding Your Business Back?` Objective: final specific invitation; 5 words. Copy v1 applied.
- **HOME.CTA.BUTTON** — Current: `Get a Project Quote` → `/contact/`. Coordinate with shared header/footer CTA; retained as supplied copy v1.

## Websites — `/websites/`

Source: `strategy/websites.njk`; order follows page appearance.

- **WEBSITES.META.TITLE** — `Websites | Thomas Web Group`; page-specific SEO title, about 50–60 characters. **[NEW COPY]**
- **WEBSITES.META.DESCRIPTION** — `Placeholder service page for website design and development.`; summarize real website service, audience, and value, about 140–160 characters. **[NEW COPY]**

### Intro and capabilities

- **WEBSITES.INTRO.KICKER** — `[SERVICE PAGE TITLE]`; service eyebrow, 2–6 words. **[NEW COPY]**
- **WEBSITES.INTRO.HEADING** — `[WEBSITE SERVICE INTRO]`; H1 stating website service/customer benefit, 5–12 words. **[NEW COPY]**
- **WEBSITES.INTRO.DESCRIPTION** — `[WEBSTIES PAGE DESCRIPTION]`; explain service, audience, and outcomes, 25–45 words. **[NEW COPY]**
- **WEBSITES.CAPABILITIES.KICKER** — `[CAPABILITIES]`; eyebrow, 1–3 words. **[NEW COPY]**
- **WEBSITES.CAPABILITIES.HEADING** — `Website capabilities`; retain/refine heading, 2–5 words. **[NEW COPY]**
- **WEBSITES.CAPABILITY.01.TITLE / .02.TITLE / .03.TITLE** — Each `[CAPABILITY TITLE]`; actual deliverable, 2–5 words. **[NEW COPY]**
- **WEBSITES.CAPABILITY.01.DESCRIPTION / .02.DESCRIPTION / .03.DESCRIPTION** — Each `[CAPABILITY DESCRIPTION]`; explain value/scope, 12–25 words. Facts needed: actual included services. **[NEW COPY]**

### Process

- **WEBSITES.PROCESS.KICKER** — `[PROCESS]`; eyebrow, 1–3 words. **[NEW COPY]**
- **WEBSITES.PROCESS.HEADING** — `Process overview`; 2–4 words. **[NEW COPY]**
- **WEBSITES.PROCESS.01.TITLE / .02.TITLE / .03.TITLE / .04.TITLE** — Current values respectively `[DISCOVERY]`, `[PLANNING]`, `[BUILD]`, `[LAUNCH]`. Objective: confirmed stage names; 1–4 words each. **[NEW COPY]**
- **WEBSITES.PROCESS.01.DESCRIPTION / .02.DESCRIPTION / .03.DESCRIPTION / .04.DESCRIPTION** — Current values respectively `[DISCOVERY DESCRIPTION]`, `[PLANNING DESCRIPTION]`, `[BUILD DESCRIPTION]`, `[LAUNCH DESCRIPTION]`. Objective: explain actual stage and client involvement; 12–25 words each. Facts needed: real process/timeline/review stages. **[NEW COPY]**

### Selected website projects

- **WEBSITES.WORK.KICKER** — `[SELECTED WORK]`; eyebrow, 1–3 words. **[NEW COPY]**
- **WEBSITES.WORK.HEADING** — `Selected website projects`; heading, 2–5 words. **[NEW COPY]**
- For each card **01**, **02**, and **03**:
  - `WEBSITES.WORK.nn.STATUS`: `[PROJECT STATUS]`; verified status, 1–3 words. **[NEW COPY]**
  - `WEBSITES.WORK.nn.TITLE`: `[PROJECT TITLE]`; approved client/project name, 2–6 words. **[NEW COPY]**
  - `WEBSITES.WORK.nn.SUMMARY`: `[PROJECT SUMMARY]`; 15–30 words on need/work/results. **[NEW COPY]**
  - `WEBSITES.WORK.nn.TECH.1`, `.TECH.2`, `.TECH.3`: three separately identified `[TECH]` tags; verified stack, 1–3 words each. **[NEW COPY]** `[tag]`
  - `WEBSITES.WORK.nn.CTA`: `View project` → `/work/`; link label, 1–3 words. **[NEW COPY]** `[approved link label]`
  Facts needed for every project: identity/permission, work performed, status, technology, approved evidence.

### FAQ and CTA

- **WEBSITES.FAQ.KICKER** — `[FAQ]`; eyebrow, 1–3 words. **[NEW COPY]**
- **WEBSITES.FAQ.HEADING** — `Frequently asked questions`; section heading, 2–5 words. **[NEW COPY]**
- **WEBSITES.FAQ.01.QUESTION / .02.QUESTION / .03.QUESTION** — Each `[QUESTION]`; answer real website buyer concerns; 5–12 words each. **[NEW COPY]**
- **WEBSITES.FAQ.01.ANSWER / .02.ANSWER / .03.ANSWER** — Each `[ANSWER]`; direct factual answers, 25–60 words each. Facts needed: policies, support scope, pricing/timelines if mentioned. **[NEW COPY]**
- **WEBSITES.CTA.EYEBROW** — `[PROJECT QUOTE]`; lead-in, 1–4 words. **[NEW COPY]**
- **WEBSITES.CTA.HEADING** — `Get a Project Quote`; coordinate with CTA button; 3–6 words. **[NEW COPY]**
- **WEBSITES.CTA.BUTTON** — `Get a Project Quote` → `/contact/`; coordinate with shared CTA. **[NEW COPY]** `[approved CTA]`

## Work index — `/work/`

Source: `strategy/work.njk`. Four repeated card slots; none currently has real project imagery.

- **WORK.META.TITLE** — `Work | Thomas Web Group`; portfolio SEO title, about 50–60 characters. **[NEW COPY]**
- **WORK.META.DESCRIPTION** — `Placeholder portfolio page for selected Thomas Web Group work.`; summarize verified portfolio, about 140–160 characters. **[NEW COPY]**
- **WORK.INTRO.KICKER** — `[WORK INDEX]`; eyebrow, 1–3 words. **[NEW COPY]**
- **WORK.INTRO.HEADING** — `[WORK PAGE HEADING]`; H1 introducing case studies, 3–8 words. **[NEW COPY]**
- **WORK.INTRO.DESCRIPTION** — `[WORK PAGE DESCRIPTION]`; explain portfolio scope, 20–40 words. **[NEW COPY]**
- For each card **01–04**:
  - `WORK.CARD.nn.IMAGE`: `[IMAGE]`; select approved project thumbnail (asset, not copy). **[NEW COPY]** `[approved image asset]`
  - `WORK.CARD.nn.STATUS`: `[STATUS]`; verified status, 1–3 words. **[NEW COPY]**
  - `WORK.CARD.nn.TITLE`: `[PROJECT TITLE]`; approved name, 2–6 words. **[NEW COPY]**
  - `WORK.CARD.nn.SUMMARY`: `[PROJECT SUMMARY]`; concise need/work/result, 15–30 words. **[NEW COPY]**
  - `WORK.CARD.nn.TECH.1`, `.TECH.2`, `.TECH.3`: three separately identified `[TECH]` tags; verified platforms, 1–3 words each. **[NEW COPY]** `[tag]`
  - `WORK.CARD.nn.CTA`: `Request details` → `/contact/`; 1–3 words. **[NEW COPY]** `[approved contact CTA]`
- **WORK.CTA.EYEBROW** — `[WORK CTA]`; 1–4 words. **[NEW COPY]**
- **WORK.CTA.HEADING / WORK.CTA.BUTTON** — `Get a Project Quote`; button links `/contact/`. Coordinate with shared CTA. **[NEW COPY]** `[approved CTA]`

## Project detail pages

### Dad Cuts Grass — `/work/dad-cuts-grass/`

- **PROJECT.DAD.META.TITLE** — `Dad Cuts Grass Website Project | Thomas Web Group`; SEO title, 50–60 characters. **[NEW COPY]**
- **PROJECT.DAD.META.DESCRIPTION** — `A lawn-care website with service details and a custom online quote form for Dad Cuts Grass.`; SEO description, 140–160 characters. Verify project facts. **[NEW COPY]**
- **PROJECT.DAD.SECTION_LABEL** — `Website Project`; category header, 2 words. **[NEW COPY]** `[confirm label]`
- **PROJECT.DAD.CATEGORY** — `Local Service Business`; category descriptor. **[NEW COPY]** `[verified category]`
- **PROJECT.DAD.CLIENT_LABEL / PROJECT.DAD.H1** — `Dad Cuts Grass`; identify the project consistently. **[NEW COPY]** `[approved project name]`
- **PROJECT.DAD.IMAGE_ALT** — `Dad Cuts Grass website project`; describe the current image accurately, 5–10 words. Confirm image is a logo/project visual. **[NEW COPY]**
- **PROJECT.DAD.INTRO** — `Dad Cuts Grass needed a website where local customers could review lawn-care services and request an instant quote.`; project need, 10–25 words. Confirm quote functionality. **[NEW COPY]**
- **PROJECT.DAD.BUILD.HEADING** — `What We Built`; section label. **[NEW COPY]**
- **PROJECT.DAD.BUILD.01** — `Mobile-friendly lawn-care service pages`; confirm deliverable. **[NEW COPY]**
- **PROJECT.DAD.BUILD.02** — `Custom online quote form`; confirm it is custom/current. **[NEW COPY]**
- **PROJECT.DAD.BUILD.03** — `Contact options for prospective customers`; confirm deliverable. **[NEW COPY]**
- **PROJECT.DAD.TESTIMONIAL.HEADING** — `Client Feedback`; verify testimonial has publication permission. **[NEW COPY]**
- **PROJECT.DAD.TESTIMONIAL.TEXT** — `Everything changed after I got the new website going. They helped implement instant online quotes for my customers and I was shocked at how well that has converted for us. Really great people. Thanks Thomas Web Group!` Verify exact quote and conversion claim; retain client voice. **[NEW COPY]**
- **PROJECT.DAD.TESTIMONIAL.ATTRIBUTION** — `Ray T, Owner`; confirm preferred public attribution and consent. **[NEW COPY]** `[approved attribution]`
- **PROJECT.DAD.CTA.HEADING** — `Need online quote requests for your service business?`; prospect-oriented close, 8–12 words. **[NEW COPY]**
- **PROJECT.DAD.CTA.BUTTON** — `Let's Talk` → `/contact/`; coordinate with shared CTA. **[NEW COPY]**

### Smoky Mountain Acres — `/work/smoky-mountain-acres/`

- **PROJECT.SMA.META.TITLE** — `Smoky Mountain Acres Website Project | Thomas Web Group`; SEO title, 50–60 characters. **[NEW COPY]**
- **PROJECT.SMA.META.DESCRIPTION** — `A farm website for Smoky Mountain Acres, with pages for farm tours, livestock, local products, and educational articles.`; SEO description, 140–160 characters. Verify project facts. **[NEW COPY]**
- **PROJECT.SMA.SECTION_LABEL** — `Website Project`; category header. **[NEW COPY]** `[confirm label]`
- **PROJECT.SMA.CATEGORY** — `Farm & Local Business`; verify sector label. **[NEW COPY]**
- **PROJECT.SMA.CLIENT_LABEL / PROJECT.SMA.H1** — `Smoky Mountain Acres`; identify project consistently. **[NEW COPY]** `[approved project name]`
- **PROJECT.SMA.IMAGE_ALT** — `Smoky Mountain Acres website project`; describe actual logo/image accurately. **[NEW COPY]**
- **PROJECT.SMA.INTRO** — `The farm needed pages for its livestock, farm tours, local products, and educational content.`; 10–25 words. Confirm scope. **[NEW COPY]**
- **PROJECT.SMA.LIVE_LINK** — `View Live Website` → `https://smokymountainacres.com`; verify destination/label. **[NEW COPY]**
- **PROJECT.SMA.BUILD.HEADING** — `What We Built`. **[NEW COPY]**
- **PROJECT.SMA.BUILD.01** — `Pages for livestock, farm tours, and local products`; verify completed pages. **[NEW COPY]**
- **PROJECT.SMA.BUILD.02** — `Blog for farm updates and educational articles`; verify blog scope. **[NEW COPY]**
- **PROJECT.SMA.BUILD.03** — `Optimized farm photography`; verify actual optimization. **[NEW COPY]**
- **PROJECT.SMA.TESTIMONIAL.HEADING** — `Client Feedback`; verify permission. **[NEW COPY]**
- **PROJECT.SMA.TESTIMONIAL.TEXT** — `We are a local farm in East TN who needed a website that reflected our family's values and mission. One challenge was trying to figure out what sort of design we wanted and what we wanted the website to say. Thomas Web Group worked patiently with us to give us exactly what we were looking for! I can't recommend them enough and am so excited with our new website!` Verify exact quote and permission; retain client voice. **[NEW COPY]**
- **PROJECT.SMA.TESTIMONIAL.ATTRIBUTION** — `Kristen Lee, Client`; confirm public attribution and consent. **[NEW COPY]** `[approved attribution]`
- **PROJECT.SMA.CTA.HEADING** — `Need a website with room for multiple services and content?`; 8–12 words. **[NEW COPY]**
- **PROJECT.SMA.CTA.BUTTON** — `Let's Talk` → `/contact/`; shared contact action. **[NEW COPY]**

## About — `/about/`

Source: `strategy/about.njk`.

- **ABOUT.META.TITLE** — `About | Thomas Web Group`; about-page SEO title, about 50–60 characters. **[NEW COPY]**
- **ABOUT.META.DESCRIPTION** — `Placeholder about page for the Thomas Web Group redesign.`; company summary, about 140–160 characters. **[NEW COPY]**
- **ABOUT.INTRO.KICKER** — `[ABOUT PAGE]`; 1–3 words. **[NEW COPY]**
- **ABOUT.INTRO.HEADING** — `[ABOUT PAGE TITLE]`; company H1, 3–8 words. **[NEW COPY]**
- **ABOUT.INTRO.DESCRIPTION** — `[ABOUT CONTENT]`; who the business serves/what it does, 30–60 words. Facts needed: company background and audience. **[NEW COPY]**
- **ABOUT.EXPERTISE.KICKER** — `[AREAS OF EXPERTISE]`; 2–5 words. **[NEW COPY]**
- **ABOUT.EXPERTISE.HEADING** — `Areas of expertise`; 2–5 words. **[NEW COPY]**
- **ABOUT.EXPERTISE.01.TITLE / .02.TITLE / .03.TITLE** — Each `[EXPERTISE AREA]`; verified competency names, 2–5 words. **[NEW COPY]**
- **ABOUT.EXPERTISE.01.DESCRIPTION / .02.DESCRIPTION / .03.DESCRIPTION** — Each `[EXPERTISE DESCRIPTION]`; evidence-based support, 12–25 words. **[NEW COPY]**
- **ABOUT.APPROACH.KICKER** — `[APPROACH]`; 1–3 words. **[NEW COPY]**
- **ABOUT.APPROACH.HEADING** — `Approach to client work`; 3–6 words. **[NEW COPY]**
- **ABOUT.APPROACH.BODY** — `[CLIENT WORK APPROACH]`; actual collaboration/process, 40–80 words. Facts needed: true process and commitments. **[NEW COPY]**
- **ABOUT.BACKGROUND.KICKER** — `[BACKGROUND]`; 1–3 words. **[NEW COPY]**
- **ABOUT.BACKGROUND.HEADING** — `Background and team`; 3–5 words. **[NEW COPY]**
- **ABOUT.BACKGROUND.01.TITLE / .02.TITLE / .03.TITLE** — Current: `[BACKGROUND SUMMARY]`, `[TEAM SUMMARY]`, `[WORK STYLE]`. Each card heading, 2–6 words. **[NEW COPY]**
- **ABOUT.BACKGROUND.01.DESCRIPTION / .02.DESCRIPTION / .03.DESCRIPTION** — Current: `[BACKGROUND DESCRIPTION]`, `[TEAM DESCRIPTION]`, `[WORK STYLE DESCRIPTION]`. About 15–35 words each. Facts needed: history, roles/experience, actual work style. **[NEW COPY]**
- **ABOUT.CTA.EYEBROW** — `[CTA]`; 1–4 words. **[NEW COPY]**
- **ABOUT.CTA.HEADING / ABOUT.CTA.BUTTON** — `Get a Project Quote`; button → `/contact/`. Coordinate with shared CTA. **[NEW COPY]** `[approved CTA]`

## Contact — `/contact/`

Source: `strategy/contact.njk`. Preserve form field names, required states, Netlify attributes, and `/thank-you/` action; those are integration details, not copywriting fields.

- **CONTACT.META.TITLE** — `Contact | Thomas Web Group`; contact-page SEO title, about 50–60 characters. **[NEW COPY]**
- **CONTACT.META.DESCRIPTION** — `Placeholder contact page for project inquiries.`; set accurate inquiry expectations, about 140–160 characters. **[NEW COPY]**
- **CONTACT.INTRO.KICKER** — `[CONTACT PAGE]`; 1–3 words. **[NEW COPY]**
- **CONTACT.INTRO.HEADING** — `[CONTACT PAGE TITLE]`; H1, 3–8 words. **[NEW COPY]**
- **CONTACT.INTRO.DESCRIPTION** — `[CONTACT PAGE INTRODUCTION]`; explain how to inquire, 20–40 words. **[NEW COPY]**
- **CONTACT.INFO.KICKER** — `[INQUIRY OPTIONS]`; 1–3 words. **[NEW COPY]**
- **CONTACT.INFO.HEADING** — `Project inquiry`; 2–4 words. **[NEW COPY]**
- **CONTACT.INFO.DESCRIPTION** — `[CONTACT INTRODUCTION]`; response/contact expectations, 15–30 words. **[NEW COPY]**
- **CONTACT.INFO.EMAIL** — `Email: raymond@thomaswebgroup.com`; verify public email. **[NEW COPY]** `[verified email]`
- **CONTACT.INFO.PHONE** — `Phone: (423) 225-8787`; verify number. **[NEW COPY]** `[verified phone]`
- **CONTACT.INFO.LOCATION** — `Location: East Tennessee`; verify phrasing. **[NEW COPY]** `[verified location]`
- **CONTACT.FORM.KICKER** — `[FORM]`; 1–3 words. **[NEW COPY]**
- **CONTACT.FORM.HEADING** — `Project inquiry form`; 2–5 words. **[NEW COPY]**
- **CONTACT.FORM.NAME.LABEL / .BUSINESS.LABEL / .EMAIL.LABEL / .WEBSITE.LABEL / .SERVICE.LABEL / .PROJECT.LABEL** — Current labels: `Name`, `Business name`, `Email`, `Website (optional)`, `Service interest`, `Project description`. Keep clear and accessible; labels are technical/system text. **[NEW COPY]** `[retain or approved label edits]`
- **CONTACT.FORM.NAME.PLACEHOLDER** — `[YOUR NAME]`; current 2 words. **[NEW COPY]**
- **CONTACT.FORM.BUSINESS.PLACEHOLDER** — `[BUSINESS NAME]`; current 2 words. **[NEW COPY]**
- **CONTACT.FORM.EMAIL.PLACEHOLDER** — `[EMAIL ADDRESS]`; current 2 words. **[NEW COPY]**
- **CONTACT.FORM.WEBSITE.PLACEHOLDER** — `[WEBSITE URL]`; current 2 words. **[NEW COPY]**
- **CONTACT.FORM.SERVICE.EMPTY** — `[SELECT A SERVICE]`; select prompt, 3 words. **[NEW COPY]**
- **CONTACT.FORM.SERVICE.OPTION.WEBSITE / .CRM / .AUTOMATION / .SEO / .SOCIAL** — Current options: `Website Design`, `CRM and Business Systems`, `Automation`, `SEO and Search Visibility`, `Social Media`. Confirm each is offered; selection values are technical and must remain mapped correctly. **[NEW COPY]** `[approved service option labels]`
- **CONTACT.FORM.PROJECT.PLACEHOLDER** — `[PROJECT DESCRIPTION]`; prompt; 2 words. **[NEW COPY]**
- **CONTACT.FORM.SUBMIT** — `Submit inquiry`; submit action, 2 words. **[NEW COPY]** `[approved submit label]`
- **CONTACT.FORM.HELPER** — `[FORM HELPER TEXT]`; privacy/response expectations, 10–25 words. Facts needed: what happens to submissions, response expectation, privacy link if appropriate. **[NEW COPY]**

## CRM & Business Systems — `/crm-business-systems/`

Content values are YAML front matter in `strategy/crm-business-systems.njk` under `service`; the template in `strategy/_includes/service-page.njk` repeats the same layout. `service.image` and `service.highlights[].icon` are assets/implementation, not copy.

- **CRM.SERVICE.EYEBROW** — `CRM & BUSINESS SYSTEMS`; 2–5 words. **[NEW COPY]**
- **CRM.SERVICE.HEADING** — `Keep leads and customer follow-up in one place.`; H1/benefit, 5–12 words. **[NEW COPY]**
- **CRM.SERVICE.INTRO** — `If inquiries are scattered across email, spreadsheets, and apps, we can organize leads in HubSpot or another CRM.`; 20–35 words. Verify supported CRM platforms and migration scope. **[NEW COPY]**
- **CRM.SERVICE.IMAGE_ALT** — `Business systems supporting a local service company`; 5–12 words; describe actual image. **[NEW COPY]**
- **CRM.SERVICE.HIGHLIGHT.01.TITLE / .TEXT** — `CRM setup and migrations` / `Set up HubSpot or another CRM, move records, or improve the system you already use.` Confirm actual support. **[NEW COPY]**
- **CRM.SERVICE.HIGHLIGHT.02.TITLE / .TEXT** — `Leads and follow-up` / `See each inquiry's status and automate routine reminders or follow-up.` Confirm features. **[NEW COPY]**
- **CRM.SERVICE.HIGHLIGHT.03.TITLE / .TEXT** — `Data and connections` / `Remove duplicate records, connect systems, and report on leads.` Confirm tools/deliverables. **[NEW COPY]**
- Metadata: **CRM.META.TITLE** `Small Business CRM & HubSpot Consulting | Thomas Web Group`; **CRM.META.DESCRIPTION** `Organize leads and follow-up with small business CRM setup, HubSpot consulting, migrations, integrations, and reporting.` Replace/review for SEO lengths (title 50–60 chars, description 140–160 chars). **[NEW COPY]**
- Shared components: `Included` heading and `Let's Talk` CTA are in shared service template; see shared section.

## Growth & Automation — `/growth-automation/`

Source YAML front matter: `strategy/growth-automation.njk`, object `service`.

- **GROWTH.SERVICE.EYEBROW** — `GROWTH STRATEGY & AUTOMATION`; 2–5 words. **[NEW COPY]**
- **GROWTH.SERVICE.HEADING** — `Spend less time on manual work and missed follow-ups.`; H1, 7–12 words. **[NEW COPY]**
- **GROWTH.SERVICE.INTRO** — `If staff repeat the same updates or leads wait for follow-up, we can map the process and automate routine steps.`; 20–35 words. Verify automation capability. **[NEW COPY]**
- **GROWTH.SERVICE.IMAGE_ALT** — `Business performance and reporting tools`; describe actual image, 5–12 words. **[NEW COPY]**
- **GROWTH.SERVICE.HIGHLIGHT.01.TITLE / .TEXT** — `Find ways to reach customers` / `Review how customers find you and identify changes to lead generation.` Verify deliverables. **[NEW COPY]**
- **GROWTH.SERVICE.HIGHLIGHT.02.TITLE / .TEXT** — `Simplify repeat work` / `Automate repetitive tasks such as assigning leads or sending routine notifications.` Verify automation scope. **[NEW COPY]**
- **GROWTH.SERVICE.HIGHLIGHT.03.TITLE / .TEXT** — `Connect tools and information` / `Connect business tools and create reports that show lead and sales activity.` Verify tools/data access. **[NEW COPY]**
- Metadata: **GROWTH.META.TITLE** `Small Business Growth Strategy & Automation | Thomas Web Group`; **GROWTH.META.DESCRIPTION** `Improve lead generation and reduce manual work with small business workflow automation, system integration, and reporting.` Review for SEO lengths. **[NEW COPY]**
- Shared components: `Included` and `Let's Talk`; see shared section.

## Social Media — `/social-media/`

Source YAML front matter: `strategy/social-media.njk`, object `service`.

- **SOCIAL.SERVICE.EYEBROW** — `SOCIAL MEDIA MANAGEMENT`; 2–4 words. **[NEW COPY]**
- **SOCIAL.SERVICE.HEADING** — `Keep your Facebook Page active without doing every post yourself.`; H1, 8–12 words. **[NEW COPY]**
- **SOCIAL.SERVICE.INTRO** — `Short on time to plan and publish? We manage Facebook business pages with regular posts and basic graphics.`; 15–25 words. Verify actual publishing service. **[NEW COPY]**
- **SOCIAL.SERVICE.IMAGE_ALT** — `Online presence and digital content for a small business`; describe actual image, 5–12 words. **[NEW COPY]**
- **SOCIAL.SERVICE.HIGHLIGHT.01.TITLE / .TEXT** — `Facebook Page management` / `Share service updates and business news, with organic audience growth strategies.` Verify platform and growth claims. **[NEW COPY]**
- **SOCIAL.SERVICE.HIGHLIGHT.02.TITLE / .TEXT** — `Content and scheduling` / `Plan posts and basic graphics for Facebook, with optional Instagram and LinkedIn support.` Verify optional platforms and scope. **[NEW COPY]**
- **SOCIAL.SERVICE.HIGHLIGHT.03.TITLE / .TEXT** — `Advertising and reporting` / `Manage Facebook ads and provide monthly performance reports. Advertising spend is separate.` Verify ad service, reporting cadence, and spend policy. **[NEW COPY]**
- Metadata: **SOCIAL.META.TITLE** `Social Media Management for Small Business | Thomas Web Group`; **SOCIAL.META.DESCRIPTION** `Facebook social media management for small businesses, including content planning, scheduled posts, and optional Instagram and LinkedIn support.` Review for SEO lengths. **[NEW COPY]**
- Shared components: `Included` and `Let's Talk`; see shared section.

## FAQ — `/faq/`

Source: `strategy/faq.njk`; Nunjucks array `questions`, eight `[question, answer]` pairs. First item is open initially; other answers remain in collapsed accordion panels.

- **FAQ.PAGE.KICKER** — `FAQ`; 1–2 words. **[NEW COPY]**
- **FAQ.PAGE.SUBTITLE.1 / .2** — `Websites, Social Media,` + `CRM Support`; together describe FAQ scope. **[NEW COPY]** `[approved scope label]`
- **FAQ.PAGE.HEADING** — `Questions About Working With Us`; H1, 4–7 words. **[NEW COPY]**
- **FAQ.01.QUESTION** — `What services do you offer?` **[NEW COPY]**
- **FAQ.01.ANSWER** — `We help with website design, social media management, CRM and business systems, and growth strategy and automation.` Verify service list. **[NEW COPY]**
- **FAQ.02.QUESTION** — `Can you help with an existing website?` **[NEW COPY]**
- **FAQ.02.ANSWER** — `Yes. We can improve an existing site or plan a redesign, and can also provide hosting and ongoing website care.` Verify hosting/care. **[NEW COPY]**
- **FAQ.03.QUESTION** — `Which social media platforms do you support?` **[NEW COPY]**
- **FAQ.03.ANSWER** — `Facebook is our primary focus. We also support Instagram and LinkedIn.` Verify platform scope. **[NEW COPY]**
- **FAQ.04.QUESTION** — `Can you help with my current CRM?` **[NEW COPY]**
- **FAQ.04.ANSWER** — `Yes. We can set up or improve HubSpot and other existing CRM systems, and help organize lead tracking and follow-up.` Verify supported CRM platforms. **[NEW COPY]**
- **FAQ.05.QUESTION** — `Do you provide ongoing support?` **[NEW COPY]**
- **FAQ.05.ANSWER** — `Yes. Monthly support can cover website maintenance, social media posting, CRM administration, and automation checks. We agree on the tasks first.` Verify availability and task scope. **[NEW COPY]**
- **FAQ.06.QUESTION** — `How does pricing work?` **[NEW COPY]**
- **FAQ.06.ANSWER** — `We do not publish fixed prices. Cost depends on the work involved; we outline scope and cost before work starts.` Verify quote/pricing policy. **[NEW COPY]**
- **FAQ.07.QUESTION** — `Do you work outside East Tennessee?` **[NEW COPY]**
- **FAQ.07.ANSWER** — `Yes. East Tennessee is our local market, and we also work with businesses nationwide.` Verify geographic service claim. **[NEW COPY]**
- **FAQ.08.QUESTION** — `What happens after I get in touch?` **[NEW COPY]**
- **FAQ.08.ANSWER** — `We read your message and email you to clarify what you need and arrange a call.` Verify actual inquiry workflow and timing. **[NEW COPY]**
- **FAQ.PAGE.CTA.HEADING** — `Have a question about your project?`; 5–8 words. **[NEW COPY]**
- **FAQ.PAGE.CTA.BUTTON** — `Let's Talk` → `/contact/`; coordinate with shared CTA. **[NEW COPY]**
- Metadata: **FAQ.META.TITLE** `Small Business Services FAQ | Thomas Web Group`; **FAQ.META.DESCRIPTION** `Answers about website design, social media management, CRM and HubSpot support, ongoing services, and working with Thomas Web Group.` Review SEO lengths. **[NEW COPY]**

## Pricing / ongoing services — `/pricing/`

Source: metadata in `strategy/pricing.njk`; body in `strategy/_includes/pricing.njk`.

- **PRICING.SECTION.HEADING** — `Ongoing Support`; section H2. **[NEW COPY]**
- **PRICING.SECTION.SUBTITLE.1 / .2** — `Monthly Services` / `Website, Social, CRM`; 2–4 words each. **[NEW COPY]**
- **PRICING.PLAN.WEBSITE.TITLE** — `Website Care`. **[NEW COPY]**
- **PRICING.PLAN.WEBSITE.DESCRIPTION** — `Hosting, updates, backups, monitoring, minor content changes, and basic traffic reporting.` Verify every inclusion/exclusion and price implication. **[NEW COPY]**
- **PRICING.PLAN.WEBSITE.CTA** — `Let's Talk` → `/contact/`. **[NEW COPY]**
- **PRICING.PLAN.SOCIAL.TITLE** — `Social Media Management`. **[NEW COPY]**
- **PRICING.PLAN.SOCIAL.DESCRIPTION** — `Content planning, scheduled Facebook posts, basic creative, optional Instagram support, and performance reporting.` Verify deliverables/platforms/cadence. **[NEW COPY]**
- **PRICING.PLAN.SOCIAL.CTA** — `Let's Talk` → `/contact/`. **[NEW COPY]**
- **PRICING.PLAN.CRM.TITLE** — `CRM & Automation Support`. **[NEW COPY]**
- **PRICING.PLAN.CRM.DESCRIPTION** — `CRM maintenance, pipeline updates, automation monitoring, data checks, and reporting.` Verify service tasks. **[NEW COPY]**
- **PRICING.PLAN.CRM.CTA** — `Let's Talk` → `/contact/`. **[NEW COPY]**
- **PRICING.SCOPE.NOTE** — `Monthly work is scoped to agreed tasks. One-time projects are also available.` Verify actual scope and one-time project availability. **[NEW COPY]**
- Metadata: **PRICING.META.TITLE** `Monthly Business Services | Thomas Web Group`; **PRICING.META.DESCRIPTION** `Ongoing website care, social media management, CRM support, and automation for small businesses. Find support that fits your needs.` Review SEO lengths.
- **SEO/content structure note:** no H1 is currently rendered on this route; `Ongoing Support` is an H2. Any structural change is outside this copy worksheet and requires a separate implementation instruction.

## Privacy Policy — `/privacy-policy/`

Source: `strategy/privacy-policy.njk`. This is legal policy content, not ordinary promotional copy. Have business/legal counsel confirm actual practice and supply or approve all replacement language. Do not draft unsupported promises.

- **PRIVACY.PAGE.SECTION_LABEL / .SUBTITLE.1 / .SUBTITLE.2 / .PAGE.H1** — Current labels: `Privacy`; `Thomas Web Group`; `Privacy Policy`; `Privacy Policy`. Confirm document title treatment. **[NEW COPY]** `[approved headings]`
- **PRIVACY.INTRO** — `Thomas Web Group ("we," "us," or "our") respects your privacy and is committed to protecting your personal information. This Privacy Policy explains how we collect, use, store, and share information when you visit our website, contact us, use our services, or opt in to receive SMS messages.` **[NEW COPY]** `[counsel-approved text based on actual practices]`
- **PRIVACY.COLLECT.HEADING / .BODY** — Heading: `Information We Collect`. Body: `We may collect your name, email address, phone number, business name, website address, form submissions, communications, SMS consent, IP address, browser and device type, pages visited, referral source, and general website usage information.` Verify form/storage/analytics/logging. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.USE.HEADING / .BODY** — Heading: `How We Use Your Information`. Body: `We may use information to operate and improve our business and website, respond to inquiries, provide services, prepare quotes, communicate with customers, send opted-in SMS messages, maintain records, improve performance, and protect against fraud or abuse.` Verify every use. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.COOKIES.HEADING / .BODY** — Heading: `Cookies and Analytics`. Body: `Our website may use cookies or similar technologies to understand usage, measure performance, and improve the site. Third-party analytics or infrastructure providers may process limited technical information on our behalf.` Confirm actual site tools/vendors. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.SHARING.HEADING / .BODY** — Heading: `Data Sharing`. Body: `Customer data is not shared with third parties for promotional or marketing purposes. Mobile opt-in and consent are never shared with anyone for any purpose. We may share information with providers that help operate our business, or when required by law.` Verify providers and absolute SMS-consent claim. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.RETENTION.HEADING / .BODY** — Heading: `Data Retention and Security`. Body: `We retain information as reasonably necessary for the purposes described here, business records, disputes, or legal obligations. We use reasonable safeguards, but no internet transmission or electronic storage method can be guaranteed completely secure.` Confirm retention and security practices. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.PAYMENTS.HEADING / .BODY** — Heading: `Payments`. Body: `If you purchase services from Thomas Web Group, payment information may be processed by a third-party payment processor. Thomas Web Group does not generally store full payment card information.` Confirm whether/how payment is processed. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.CHILDREN.HEADING / .BODY** — Heading: `Children's Privacy`. Body: `Our website and services are intended for businesses and adults and are not directed toward children under 13. We do not knowingly collect personal information from children under 13.` Legal review required. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.SMS.HEADING / .BODY** — Heading: `Messaging Program Terms`. Body: `Customer care messages may be sent from (423) 225-8787. Text STOP to unsubscribe or HELP for assistance. Message and data rates may apply and frequency varies. Carriers are not liable for delayed or undelivered messages.` Confirm the SMS program exists, actual enrollment/consent, number, frequency and compliance requirements. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.CHOICES.HEADING / .BODY** — Heading: `Your Choices`. Body: `You may contact us to ask about, correct, or request deletion of your information when appropriate, opt out of non-required communications, or withdraw SMS consent by texting STOP.` Confirm request handling and rights. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.CHANGES.HEADING / .BODY** — Heading: `Changes to This Privacy Policy`. Body: `We may update this policy to reflect changes to our business, website, services, or legal requirements. The current version will be posted here.` Confirm date/notice approach. **[NEW COPY]** `[counsel-approved section]`
- **PRIVACY.CONTACT.HEADING / .BODY** — Heading `Contact Us`; current body lists `Thomas Web Group`, `raymond@thomaswebgroup.com`, `(423) 225-8787`. Verify contact channels and legal entity. **[NEW COPY]** `[verified details / counsel-approved section]`
- Metadata: **PRIVACY.META.TITLE** `Privacy Policy | Thomas Web Group`; **PRIVACY.META.DESCRIPTION** `Thomas Web Group privacy policy and SMS messaging terms.` Review SEO fields without changing legal meaning.

## Terms — `/terms/`

Source: `strategy/terms.njk`. All text is legal language and must be checked with counsel. Existing terms expressly say they do not replace project contracts.

- **TERMS.SECTION.LABEL / .SUBTITLE.1 / .SUBTITLE.2 / .H1** — Current: `Terms`; `Website`; `Terms`; `Website Terms`. Confirm heading hierarchy/treatment. **[NEW COPY]** `[approved headings]`
- **TERMS.INTRO** — `These terms govern use of the Thomas Web Group public website. They do not replace project contracts, proposals, statements of work, or hosting agreements.` **[NEW COPY]** `[counsel-approved text]`
- **TERMS.USE.HEADING / .BODY** — `Website Use`; `Use this website lawfully and do not interfere with its operation, security, or availability.` **[NEW COPY]** `[counsel-approved section]`
- **TERMS.INFORMATION.HEADING / .BODY** — `Informational Nature of Website Content`; `Website content is general information about our work and offer. A quote or project agreement controls the details of a particular engagement.` **[NEW COPY]** `[counsel-approved section]`
- **TERMS.IP.HEADING / .BODY** — `Intellectual Property on ThomasWebGroup.com`; `Thomas Web Group and its licensors retain rights in the website's original text, design, branding, and other materials unless stated otherwise. Do not copy or reuse them without permission.` Verify ownership/licenses. **[NEW COPY]** `[counsel-approved section]`
- **TERMS.LINKS.HEADING / .BODY** — `Third-Party Links`; `Links to third-party websites are provided for convenience. Thomas Web Group is not responsible for their content, availability, or policies.` **[NEW COPY]** `[counsel-approved section]`
- **TERMS.NO_GUARANTEE.HEADING / .BODY** — `No Guarantee of Search Rankings, Leads, Revenue, or Business Results`; `We do not guarantee search rankings, leads, revenue, traffic, or other business results. Website performance depends on many factors outside the website alone.` Verify consistency with marketing and contracts. **[NEW COPY]** `[counsel-approved section]`
- **TERMS.ACCURACY.HEADING / .BODY** — `Accuracy and Updates`; `We work to keep information current, but content may change without notice and may contain errors or omissions.` **[NEW COPY]** `[counsel-approved section]`
- **TERMS.LIABILITY.HEADING / .BODY** — `Limitation of Liability`; `To the extent permitted by law, Thomas Web Group will not be liable for indirect, incidental, special, consequential, or lost-profit damages arising from use of this public website.` Counsel review required. **[NEW COPY]** `[counsel-approved section]`
- **TERMS.CHANGES.HEADING / .BODY** — `Changes to These Terms`; `We may update these terms by posting a revised version on this page. Continued use after an update means you accept the revised terms.` Counsel review required. **[NEW COPY]** `[counsel-approved section]`
- **TERMS.CONTACT.HEADING / .BODY** — `Contact Information`; current body: `Thomas Web Group`, `raymond@thomaswebgroup.com`, `(423) 225-8787`. Verify legal entity/contact details. **[NEW COPY]** `[verified details / counsel-approved section]`
- Metadata: **TERMS.META.TITLE** `Website Terms | Thomas Web Group`; **TERMS.META.DESCRIPTION** `Terms governing use of the Thomas Web Group public website.` Keep metadata consistent with counsel-approved document.

## Thank-you — `/thank-you/`

Source: `strategy/thank-you.njk`; this route is noindex and is the contact form's success destination.

- **THANKYOU.H1** — `Thanks, we received your message.` Confirm successful-submission state; 4–8 words. **[NEW COPY]**
- **THANKYOU.BODY** — `We'll reply by email to discuss what you need.` Verify actual follow-up channel/process and any response-time commitment. **[NEW COPY]**
- **THANKYOU.CTA.HOME** — `Return Home` → `/`; recovery link, 1–3 words. **[NEW COPY]**
- **THANKYOU.CTA.WORK** — `View Our Work` → `/work/`; next step, 2–4 words. **[NEW COPY]**
- Metadata: **THANKYOU.META.TITLE** `Project Request Received | Thomas Web Group`; **THANKYOU.META.DESCRIPTION** `Confirmation for a Thomas Web Group business or website project inquiry.` The route is noindex; review for consistency, not search promotion.

## Not found — `/404.html`

Source: `strategy/404.njk`. Current page front matter is not rendered as document metadata because this template does not use the base layout.

- **NOTFOUND.H1** — `Page not found`; 2–5 words. **[NEW COPY]**
- **NOTFOUND.BODY** — `That address doesn't match a page on this site.`; explain missing route in plain language. **[NEW COPY]**
- **NOTFOUND.CTA.HOME** — `Home` → `/`; 1 word. **[NEW COPY]**
- **NOTFOUND.CTA.WEBSITES** — `Website Design` → `/websites/`; 2 words. **[NEW COPY]**
- **NOTFOUND.CTA.CONTACT** — `Let's Talk` → `/contact/`; coordinate with shared CTA. **[NEW COPY]**
- Front matter values **NOTFOUND.META.TITLE** `Page Not Found | Thomas Web Group` and **NOTFOUND.META.DESCRIPTION** `The requested Thomas Web Group page could not be found.` exist but are not rendered. Do not assume rewriting them resolves the metadata issue; that would require a separate template/layout change.

## Information Needed From Business Owner

The writer needs owner-confirmed facts for the company identity/history/team; exact service scope/process/platforms; response timing; contact and geography claims; prices/recurring inclusions; project/client permissions, screenshots, tech stack, outcomes, and testimonials; and the real data/SMS/legal practices described in the policy pages. The project source contains no verified results metrics, bios, experience credentials, testimonial permissions, or approval markers. Do not fill these gaps with generic claims stated as facts.
