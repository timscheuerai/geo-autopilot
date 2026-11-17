---
name: seo-outbound-prep
description: Prepare off-page SEO and GEO outreach, tier by tier as context/STRATEGY.md orders it (lists that rank, corrections, journalist requests, credit and broken-link requests, competitor-linked resources, vendor stories, directories). Pick the independent pages that rank for your money keywords or that AI answers cite, verify each page and its public contact path for free, and write a send-ready pack (the ask, your page, the pitch and one follow-up). Drafts only, a person sends. Use for outreach prep, a new batch, or recording a reply or a won placement.
---

# seo-outbound-prep: placements a person can send in minutes

Links and mentions on independent pages that rank, and on the pages AI answers cite, are the off-page lever. They move your Google and Bing impressions and the share of AI answers that name you. This skill does all the prep. A person does the sending.

## Hard rules

- **Drafts only.** Never send an email, DM, comment or post, never submit a form, never create or claim an account. A pack is a draft until a person sends it.
- **Free checks only.** Plain page fetches. No paid lookups, no paid listing, sponsored slot or review fee without a budget decision written in STRATEGY.md.
- **Public contacts only.** Use a path the site itself lists: an author or editor page, a contact or submission form, a listed address such as `hello@`, or a profile the site links as its contact. Never guess, scrape or enrich a personal email. No listed path means status `needs-contact`, not a guess.
- **Your claims match your live site on the day.** Take facts from your own live pages (pricing, docs, the page you pitch), list each one a pitch uses in the pack, and never use anything on STRATEGY.md § Never claim. Quote your price exactly as the pricing page states it, never a time-limited offer.
- **Every claim about the target** comes from its page as fetched that day: title, date, author, what it lists, how it picks.
- **Voice:** the author's own email voice. Short, plain, grade 8, one concrete reason from their page, one ask, a next step, signed with the author's name. No em dashes, no flattery, no "not just X but Y".
- **Never buy, barter or swap links.** No link in return, no money, product or service for a link. A credit line is the publisher's choice.

## Pick targets

Read, in this order: the newest weekly AI-answers report (`context/ai/<date>.md`, the cited URLs), the newest research report (`context/research/<date>.json`, the top 10 per keyword), and the target table in `context/outbound/PLAN.md` (skip anything already listed).

Keep a page when all of these hold:

1. It ranks in Google's top 10 for one of your money keywords, or a tracked AI answer cited it.
2. It is a list, comparison or tool roundup where you fit the job the page is about.
3. The publisher does not sell a product that competes with yours. Adjacent vendors go to tier B.
4. It was updated in the last 12 months (a visible "Updated" line or `dateModified` in its structured data). Older pages are tier B at best.

Tiers: **A** independent and evidenced (top 10 or AI-cited) with a clear fit; **B** adjacent-vendor lists, partial fit or stale pages; **C** review sites and directories (profiles, not pitches). Within a tier, rank by citations across AI runs, then rank and volume, then odds (a page that already names you, a friendly author, a page that invites suggestions).

## Verify (free, same day)

Fetch the page and the publisher's contact, about, author and submission pages with a normal browser user agent. Record the HTTP status, title, date, author, whether you are already named, and the exact contact path (the URL plus what the site says it is for). A bot wall (403, "Just a moment") means "check in a browser", never "no contact". Keep only contact links the site lists, never addresses found loose in page text.

## Write the pack

One file per publisher: `context/outbound/<publisher-slug>.md`. Several pages from one publisher share one pack and one message.

```markdown
---
target: https://...
publisher: ...
kind: list            # list, correction, journalist, credit, broken-link, resource, vendor-story, asset-offer
tier: A
status: ready
batch: 1
contact: https://.../contact
contact_verified: 2026-01-15
our_page: https://your-site.com/...
sent:
followed_up:
outcome:
---

## Why it matters
The evidence with dates: engine and question, or keyword, rank and volume. Page date and author. Whether you are on it.

## The ask
One sentence: the exact change (add us to section X, fix our line, link our page).

## Our page
The one URL of yours that fits the page's job, checked to answer 200 and be indexable.

## Contact path
Where and how, as the site lists it.

## Facts used
Each claim about you in the pitch, with the live URL it came from.

## Pitch
Ready to paste. A form gets its field values instead of an email.

## Follow-up
One, 7 days later, two to four lines.

## Notes for the sender
Traps: paid programmes, affiliate links, the page's own thesis.

## Outcome log
Empty until something happens.
```

Add the row to the target table in `context/outbound/PLAN.md` with status `prepped`.

## Status lifecycle

`prepped` (researched) > `ready` (pack written, in a batch) > `sent` (a person sent it; date) > `followed-up` > `won` (the page names or links you), `declined`, or `no-reply` (14 days after the follow-up). `needs-contact` and `dead` (page gone, publisher now competes) park a row. The pack's frontmatter holds the live status; update the plan table at batch boundaries only.

## Batches

Ten packs make one batch. List them in one file, `context/outbound/batch-<n>.md`, with the pack paths and one line per pack saying what "sent" means for it. One batch, one review for the sender; never one task per target.

## Beyond lists: the other link-earning tiers

STRATEGY.md § Link earning orders the tactics. Work the highest tier with work left. Every one is a pack with the same frontmatter, the same hard rules and the same batches.

- **Correction** (monthly): fetch every page in the plan that already names you and compare its lines with your live site. A stale fact gets a pack with the exact replacement sentence.
- **Journalist:** keep `context/outbound/journalist-profile.md` current (the author's real experience, a citable research page of yours, a headshot path). For an open request that matches a money keyword, the pack holds the request URL and deadline, a direct two-sentence answer first, one original number or first-hand example with its source, and the page that lets the journalist check it. Skip requests that close within a day: a person sends, so they need the time.
- **Credit** (monthly): search free sources for unlinked mentions of your name, charts or quotes. The pack quotes the mention and asks for one link to the page it describes.
- **Broken link and resource:** only with a verified dead URL (archived copy read) or a competitor resource whose citing sentence one of your pages answers better. Name the sentence and your page. Never pitch a draft or a page under an experiment.
- **Vendor story:** one pack per vendor you run on that publishes customer stories, with the workflow and a result you can prove. A person decides which vendors may be named in public.
- **Asset offer** (a graphic or a video): ask first; make the asset only after the author agrees, from facts the author checked.

## Review sites and directories

Review sites and directories are profile tasks: prefill every field in `context/outbound/profiles.md` from your live site (name line, short and long description, categories, features, pricing, integrations, links, assets), mark paid options, and never create the account yourself. Review requests go to customers only through a person, with no gating and only the site's own disclosed incentives.

## Forums and video

Brief, never post. A brief names the thread or video, why it matters (cited by which AI answer), what a useful, disclosed answer from the author or a video of your own would cover, and the page of yours that answers it. Forum answers are the author's own and disclosed, with at most one mention of your company in four comments.

## Record results

When a person reports a send or a reply, or a weekly check finds a change, update the pack's frontmatter and Outcome log (date, what happened, their reply in one line).

Weekly check (free): fetch every `sent` and `followed-up` target and look for your name and a link to your domain (note `rel` nofollow or sponsored). A hit means `won`.

## When a page links to you

1. Record the win in the pack and in the plan's Placements won section (target, date, anchor, link type).
2. Request indexing for **your** linked page through [request-indexing](../request-indexing/SKILL.md), so Google recrawls it with the new link. Google and Bing take requests for your own site only. Submit the target URL on Brave's public form in the same session.
3. Record a `links` experiment for your page in `context/experiments.json`, with the date the target page changed as its live date ([seo-daily](../seo-daily/SKILL.md) § Record an experiment). The loop reads it at 14 and 28 days.
4. Track referral visits from the target's domain in your analytics, and whether the next weekly AI run cites the target page with you named. Report both in the next batch.
