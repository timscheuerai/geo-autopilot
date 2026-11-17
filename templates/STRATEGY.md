# SEO and GEO strategy

The daily loop reads this file first, then the day's report. You own it: change a rule here and the loop follows it on its next run. Copy it to `context/STRATEGY.md`, fill in every `<...>`, and keep the defaults you agree with. They come from running this loop on a real site.

## Reward

More Google clicks and impressions for `<your-site.com>` from searches that do not contain your brand name.

- Brand searches grow with marketing, not with page changes, so the loop moves **non-brand** searches. The report shows both.
- Each change is judged on its own page: equal windows before and after it goes live, read at 7 days (early), 14 (full) and 28 (final). A title change is judged on click-through, a lift on position, everything else on clicks and impressions.
- Next: sign-ups from organic search by landing page. Until you can measure them, clicks to money pages are the closest proxy.
- Secondary: Bing impressions, AI answers naming you, money pages indexed (`context/goal.json`).

## Brand

Regex that marks a brand query (case-insensitive): `<yourbrand|your brand|yourbrand\.com>`

## Focus

Who the pages are for, and where the loop spends its time first.

- Buyer: `<who searches and buys, in one sentence>`
- Competitors buyers compare you with: `<vendor 1>`, `<vendor 2>`, `<vendor 3>`
- Double down where traction already is: pages on page one or close to it get refreshed before anything new is written.

## Order of bets

The lanes pick work in this order. Rewrite it from your own Search Console data.

1. `<for example: pricing explainers for the vendors your buyers compare>`
2. `<for example: best-of lists and alternatives pages that already rank on page one and get cited by AI answers>`
3. `<for example: comparison pages against the vendors you meet in deals>`
4. `<pages close to page one: list them with their position>`

One intent, one page. A separate page exists only for a different intent, never as a near-copy for another audience.

## Leave alone

- Head terms where you rank beyond position 40: `<list>`.
- Generic topics and basic definition pages ("what is X"): no new ones, and no lane time polishing old ones beyond factual fixes.
- Queries an AI Overview already answers in full, and results pages made of job listings or forums.
- `<anything else: pages under legal review, the pricing page's prices>`

## Facts

Where the loop finds the truth about your own product. Every claim on a page about you comes from one of these, checked on the day.

- Pricing: `<URL of your pricing page>`
- Product and limits: `<URL of your docs>`
- Changes: `<URL of your changelog>`
- `<anything else: a facts file, a status page>`

## Never claim

Claims no page, pitch or profile may make, even when they sound true. Start with anything you do not have yet.

- `<for example: a certification you have not finished>`
- `<for example: an integration that is on the roadmap>`
- Beta or invite-only features as generally available.
- A customer name, logo or result without written permission.

## Banned words

`<words your brand never uses>`, plus: unlock, harness, streamline, elevate, dive into, "in today's landscape", em dashes.

Allowed terms (explain each once, in plain words, where it first appears): `<industry terms your buyers use>`

## Money pages

The pages that make money and must be indexed: `<home, /pricing, /compare/*, /alternatives/*, /guides/*>`

## Lanes

| Lane | Agents a run | Input | Done when |
| --- | --- | --- | --- |
| 1. Page-two refresh | up to 3, one per page | The report's "Page two: refresh queue", then "close to the top 3" | A section answering the page's page-two queries is live, passed independent QA, and a `refresh` experiment is recorded |
| 2. Indexing and links | 1 | The indexing queue, "Pages out of the index" | Today's pages are queued or requested, and internal-link or technical fixes for unindexed pages are live |
| 3. New content | 1, at most 1 new page a day; approved drafts first | `ready` briefs in `context/briefs/` | The page passed independent QA and waits as a draft for a human read. Once approved: live, `new page` experiment recorded |
| 4. Outreach prep | 1 | `seo-outbound-prep`, § Link earning | Three new send-ready packs in `context/outbound/`, each logged in the plan |
| 5. Learning | the orchestrator | Experiment readings | Readings applied to § Feedback loops |

A lane with nothing worth doing is skipped. No churn just to ship something.

## Link earning

Lane 4 works the tiers in this order and moves down only when the tier above has nothing left. Everything that speaks to another person stays a draft.

| Tier | Tactic |
| --- | --- |
| S | Lists buyers read: roundups that rank or that AI answers cite. Recheck lists that already name you once a month and prepare corrections. |
| S | Citable statistics: a research page with your own data, sample and method stated, each finding a complete sentence, a stable URL. Aggregates only. |
| S | Journalist requests: an expert profile and a direct answer with one original number or first-hand example. |
| S | Editorial references: only links that help the reader of that page. |
| A | Competitor-linked resources, where one of your pages adds the missing answer. |
| A | Recover earned links: unlinked mentions and reused charts or quotes. |
| A | Free tools for a calculation buyers repeat. |
| B | Broken resources, missing visuals, demo videos: offer only when the need is verified. |
| C | Customer stories with the vendors you run on. |
| D | Directories and review sites: identical details everywhere. |

## Authority

What the loop may do without asking. Change these to match how much you trust it.

- **Refresh live pages without asking,** when the section answers a query the page already ranks for, every competitor fact comes from the competitor's own pages, and an independent QA agent passed it.
- **Ship without asking:** technical fixes, metadata, structured data, sitemap, internal links, titles and descriptions.
- **New pages wait for a person.** After independent QA passes (32/40 or more, no critical fail, every claim checked at its source), a new page ships as a draft with `noindex`. It goes live only after a person has read and fact-checked it and written `Approved: <name> <date>` in its brief. Google's guidance on AI-generated content asks for exactly this review, and its spam policy on scaled content targets many pages made without added value. At most one new page a day: depth beats volume.
- **Resubmit `sitemap.xml`** when Google's copy is older than the live one. Everything else in Search Console stays read-only.
- **Drafts only:** anything that speaks in your name to other people or creates accounts elsewhere: outreach, journalist answers, credit requests, profiles, posts and comments.
- **Never:** paid calls beyond the caps in § Rules, posts or comments anywhere, links bought, bartered or traded.
- Record every decision the loop takes on its own in the day's report, so you can reverse it.

## Rules

- Keyword data budget: `<USD amount>` a month. AI-answer tracking budget: `<USD amount>` a month.
- Keyword research at most once a week. AI-answer run once a week, same prompts, same engines.
- `<how many rounds a day: 1 to start; more once you trust it>`
- Competitor facts are rechecked within 120 days, and every page shows the date.

## Feedback loops

- **Shipped to live:** the daily run marks an experiment live the day production serves its change.
- **Live to indexed:** new and changed pages go to the indexing queue; IndexNow and Bing get them the same day.
- **Indexed to ranked:** the readings at 7 days (early), 14 and 28.
- **Learning:** a kind of change whose two latest full readings (14 days or more) are `worse` or `no clear change` is paused, and the run's summary says why. A paused kind keeps one probe: at most one experiment of that kind at a time, on the strongest candidate, so it can earn its way back. A `better` full reading lifts the pause. A kind with `better` readings, early ones included, gets more of the day's agents. An early reading alone never pauses a kind.
