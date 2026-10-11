# Thomas Web Group — Content Needing Owner Review

Review date: 2026-10-10

This document lists factual confirmation and approval still needed. It does not draft replacement copy or treat any existing statement as verified.

## Priority 1 — Legal, privacy, and messaging practices

| Content ID | Page | Current status / exact question | Source | Recommended action |
|---|---|---|---|---|
| `PRIVACY.COOKIES.BODY` | `/privacy-policy/` | The policy says cookies or similar technologies and third-party analytics/infrastructure providers may process usage data. Which analytics, cookies, hosting, and other tools are actually active on the deployed site? | `strategy/privacy-policy.njk` | Confirm actual technologies and practices; have counsel review the policy. |
| `PRIVACY.SHARING.BODY` | `/privacy-policy/` | The policy says customer data is not shared for promotion and SMS consent is never shared for any purpose, while allowing operational vendors and legal disclosures. Confirm these exact practices and any exceptions. | `strategy/privacy-policy.njk` | Verify vendor/data-sharing practices and obtain legal review. |
| `PRIVACY.RETENTION.BODY`, `PRIVACY.COLLECT.BODY`, `PRIVACY.USE.BODY`, `PRIVACY.CHOICES.BODY` | `/privacy-policy/` | Confirm collected fields, form storage/retention, inquiry handling, deletion/correction process, IP/browser/usage collection, and whether SMS consent is collected. | `strategy/privacy-policy.njk`, `strategy/contact.njk` | Compare policy with the live form, hosting, analytics, and operating practices; counsel review. |
| `PRIVACY.SMS.BODY` | `/privacy-policy/` | The policy describes customer-care SMS from `(423) 225-8787`, STOP/HELP, rates, and variable frequency. Is an SMS program active, is this the correct sending number, and are the consent and opt-out practices accurately described? | `strategy/privacy-policy.njk` | Confirm the SMS program and applicable compliance wording; counsel review. |
| `PRIVACY.PAYMENTS.BODY` | `/privacy-policy/` | Confirm whether the business accepts online payments, which provider processes them, and whether the description of stored card data is accurate. | `strategy/privacy-policy.njk` | Verify the actual payment flow or clarify with counsel if no payments are processed. |
| `TERMS.*` | `/terms/` | The complete terms, including IP ownership, third-party links, disclaimers, liability, and changes, have not been legally verified. Confirm the contracting/legal entity and whether these terms accurately describe the business. | `strategy/terms.njk` | Have qualified counsel review; do not treat current wording as approved legal advice. |

## Priority 2 — Contact details and customer expectations

| Content ID | Page | Current status / exact question | Source | Recommended action |
|---|---|---|---|---|
| `GLOBAL.FOOTER.EMAIL`, `CONTACT.INFO.*`, `PRIVACY.CONTACT.BODY`, `TERMS.CONTACT.BODY` | Shared footer, Contact, Privacy, Terms | Current email is `raymond@thomaswebgroup.com`. Is it public, correct, and monitored? | `strategy/_includes/footer.njk`, `strategy/contact.njk`, `strategy/privacy-policy.njk`, `strategy/terms.njk` | Confirm the address and monitoring. It was preserved unchanged. |
| `GLOBAL.FOOTER.PHONE`, `CONTACT.INFO.*`, `PRIVACY.SMS.BODY`, `PRIVACY.CONTACT.BODY`, `TERMS.CONTACT.BODY` | Shared footer, Contact, Privacy, Terms | Current public number is `(423) 225-8787` (`+14232258787` in the telephone link). Is it correct, monitored, and also the SMS sending number? | Same as above | Confirm the public/telephone/SMS number. It was preserved unchanged. |
| `GLOBAL.FOOTER.LOCATION`, `FAQ.07` | Shared footer, FAQ | The public wording identifies East Tennessee as the local market and says many projects can be handled remotely. Confirm the intended geography and remote-service claim. | `strategy/_includes/footer.njk`, `strategy/faq.njk` | Confirm before publication. |
| `THANKYOU.BODY`, `FAQ.08`, `CONTACT.INFO.DESCRIPTION` | Thank-you, FAQ, Contact | Confirm the actual inquiry review/follow-up process and channel. No response-time guarantee was added. | `strategy/thank-you.njk`, `strategy/faq.njk`, `strategy/contact.njk` | Confirm the process; add a response expectation only if the business can reliably meet it. |

## Priority 3 — Project facts, permissions, and visuals

| Content ID | Page | Current status / exact question | Source | Recommended action |
|---|---|---|---|---|
| `HOME.PROJECTS.01.SUMMARY`, `WORK.CARD.01.*`, `PROJECT.DAD.*` | Home, Work, Dad Cuts Grass | Confirm that the described lawn-care website, online quote process, service details, and project scope match the work delivered. The previous testimonial/attribution is hidden pending permission; exact conversion statistics remain unpublished. | `strategy/index.njk`, `strategy/work.njk`, `strategy/work/dad-cuts-grass.njk` | Verify scope and claims; approve testimonial wording, attribution, and publication rights before reinstating it. |
| `PROJECT.DAD.TESTIMONIAL.TEXT`, `PROJECT.DAD.TESTIMONIAL.ATTRIBUTION` | Dad Cuts Grass | Existing testimonial and attribution are not displayed because permission was not confirmed. | `strategy/work/dad-cuts-grass.njk` (prior source content in Git history) | Obtain written approval for exact quote and attribution before reuse. |
| `HOME.PROJECTS.02.SUMMARY`, `WORK.CARD.02.*`, `PROJECT.SMA.*` | Home, Work, Smoky Mountain Acres | Confirm the farm/site features and project scope. `https://smokymountainacres.com` responded with the farm website during this review; the owner should confirm this is still the intended case-study link and that the described delivered features are accurate. The supplied technology tags are displayed as provided. | `strategy/index.njk`, `strategy/work.njk`, `strategy/work/smoky-mountain-acres.njk` | Verify scope; approve testimonial wording, attribution, and publication rights before reinstating the hidden testimonial. |
| `PROJECT.SMA.TESTIMONIAL.TEXT`, `PROJECT.SMA.TESTIMONIAL.ATTRIBUTION` | Smoky Mountain Acres | Existing testimonial and attribution are not displayed because permission was not confirmed. | `strategy/work/smoky-mountain-acres.njk` (prior source content in Git history) | Obtain written approval for exact quote and attribution before reuse. |
| `HOME.HERO.IMAGE_ALT`, `HOME.HERO.SCREEN` | Home | The current hero is a CSS laptop mockup, not an approved client screenshot. It is presented as decorative; no sample/fictitious project is shown. | `strategy/index.njk` | Supply an approved project screenshot only if the mockup is to be replaced; confirm whether the decorative treatment is acceptable. |
| `PROJECT.DAD.IMAGE_ALT`, `PROJECT.SMA.IMAGE_ALT` | Project detail pages | Actual project logo assets are displayed. Confirm permission to publish these logos as portfolio imagery. | `strategy/work/dad-cuts-grass.njk`, `strategy/work/smoky-mountain-acres.njk` | Confirm publication rights for each logo. |
| `CRM.SERVICE.IMAGE`, `GROWTH.SERVICE.IMAGE`, `SOCIAL.SERVICE.IMAGE` | Service pages | Existing images depict unrelated sample/demo websites. They remain decorative with empty alt text, not evidence of client projects. | `strategy/crm-business-systems.njk`, `strategy/growth-automation.njk`, `strategy/social-media.njk` | Confirm whether to keep these decorative visuals or supply representative approved service imagery. |

## Priority 4 — Service and company claims

| Content ID | Page | Current status / exact question | Source | Recommended action |
|---|---|---|---|---|
| `ABOUT.BACKGROUND.01.*`, `ABOUT.BACKGROUND.02.*`, `ABOUT.EXPERTISE.*` | About | Supplied copy describes CRM/revenue-operations experience, integrations, reporting, website development, online quoting, and manageable content systems. Confirm it accurately reflects Thomas Web Group's experience and current capabilities. | `strategy/about.njk` | Verify before representing these as company capabilities; no founder biography or team size was added. |
| `CRM.SERVICE.*`, `GROWTH.SERVICE.*`, `SOCIAL.SERVICE.*`, `WEBSITES.CAPABILITY.*` | Service pages | Confirm current service scope, tools/platforms supported, deliverables, and operational limits. HubSpot is referenced as an example, not as an exclusive platform. | Service-page front matter and `strategy/websites.njk` | Verify capabilities and any service commitments before publication. |
| `FAQ.05.QUESTION`, `FAQ.05.ANSWER` | FAQ | The answer says ongoing work may include website updates, social media management, CRM administration, automation, or reporting, with responsibilities agreed before work begins. Confirm which of these are actually offered. | `strategy/faq.njk` | Confirm the available ongoing support scope; no fixed package or price is published. |
| `SOCIAL.SERVICE.NOTE` | Social Media | The supplied page says paid advertising can be discussed separately; no management or outcome promise is made in that sentence. Confirm whether this accurately reflects the current offering. | `strategy/social-media.njk` | Confirm availability and boundaries. |

## Priority 5 — Form and deployment verification

| Content ID | Page | Current status / exact question | Source | Recommended action |
|---|---|---|---|---|
| `CONTACT.FORM.*`, `THANKYOU.*` | Contact, Thank-you | Required fields, native email/URL validation, service selector, Netlify form name, existing field names, POST action, and thank-you destination were checked locally. No real submission was made. Is Netlify Forms enabled on the deployed site, and does its successful POST redirect to this page while failures remain errors? | `strategy/contact.njk`, `strategy/thank-you.njk` | Verify using the deployed form without submitting fabricated data. The Eleventy local preview does not verify Netlify's backend. |
| `GLOBAL.FOOTER.YEAR` | Shared footer | Copyright now uses the build-time year (2026 for this build). Confirm the business/legal entity named in the notice. | `strategy/_includes/footer.njk`, `strategy/eleventy.config.js` | Confirm the copyright holder; the year updates on subsequent builds. |
