---
status: draft          # draft, ready, in-progress, human-review, approved, published
type: comparison
slug: {you}-vs-{vendor}
score:
---

# Brief: {you} vs {vendor}

Write your first comparison by hand, against the vendor you lose deals to most. When it is good, it becomes this template: every later comparison is the same page with the blanks filled in. Replace each `{...}` and delete these notes.

## Keyword

- Primary: `{vendor} alternative`
- Cluster: `{vendor} alternatives`, `alternatives to {vendor}`, `{you} vs {vendor}`, `{vendor} vs {you}`
- Volume, difficulty, intent, market: {from the research report}

Title: `{vendor} alternative: {you} vs {vendor} ({year})`. The "{vendor} alternatives" search usually has volume long before the brand pair does. At most 60 characters; use a short name for a long vendor name.

URL: `/compare/{you}-vs-{vendor}`

## Original contribution

- Sources: {files in context/sources/ and their URLs: a teardown you wrote, call notes cleared for public use, a migration you ran}
- What the reader can do after reading that they could not before: {one sentence}
- Claim limits: {dated results stay dated; private notes stay out}

## Page, in this order

1. **H1 and one line under it** naming the one difference: "{vendor} makes X a manual task. {you} runs it for you." An "every" or "only" claim uses the scope {vendor}'s own pages use.
2. **Short answer** (40 to 80 words): the verdict, who {vendor} suits, who {you} suits.
3. **Why switch** (3 or 4 reasons, right after the short answer). Each reason: {vendor}'s documented limit in plain words (third person, never a quote nobody gave), the fact behind it with its source, what {you} does instead, and the table row it rests on, which {you} must win. Keep the heading "Why switch" until call notes or public reviews show real finished switches.
4. **At-a-glance table** (8 to 14 rows). Rules:
   - the price is always a row;
   - {vendor}'s home-turf row (what they are known for) is always shown;
   - a row {vendor} leads can never be left out;
   - at most 3 rows even;
   - the rows follow where the real differences are against this vendor, not the same rows on every page.
5. **Row notes:** for each row, only the facts that decide it. Do not restate the table cell.
6. **How we compared:** the rubric in one paragraph, the rows left out and the line that {vendor} leads none of them, and the date the facts were checked.
7. **Run both** (when buyers often keep {vendor} for one job): how the two work side by side.
8. **FAQ** (5 to 8): questions in the searcher's words, page-two queries first. The FAQ markup matches the visible questions.
9. **Sources:** every {vendor} fact with its URL and the date checked.

## Winners are computed, never typed

Give every row a rule before you fill in a cell:

| Rule type | How it decides |
| --- | --- |
| Support level | full beats partial beats none |
| Checklist | count the components each side has (for example: sync, reports, permissions, mobile app) |
| Measure | a number with an "even" band (for example: within 10% is even) |
| Price scenario | the cost of one named, realistic task on each side's published prices |

A beta, invite-only or unlisted feature never scores, on either side, yours included. The tally ({you} X, {vendor} Y, even Z) appears once, under the table.

## Facts

- **{vendor}'s facts come from {vendor}'s own pages only:** pricing (open it in a browser; plan cards often render client-side), help center, API docs, trust center, status page, terms. Quote each fact with its URL and the date you opened it.
- "Not found" is an absence, not proof. Write "no page says X", never "X does not exist".
- A third-party site is not a fact about {vendor}.
- When {vendor}'s own pages disagree, say which page says what.
- {vendor}'s terms of service can limit what you may recommend (for example, a ban on using its data in another tool). Read them before a worked example uses their product.
- **Your side** comes only from the sources STRATEGY.md § Facts names. Nothing from § Never claim.

## Content lint (fairness and freshness)

- Every fact checked within 120 days; the page shows the date.
- 1,500 to 2,600 words. Title at most 60 characters, description 120 to 158.
- Verdicts framed as fit ("better for teams that..."), never absolute superiority.
- No superlative about {vendor} without evidence.
- No review or rating markup about yourself.
- No em dashes, no words from STRATEGY.md § Banned words.

## Links

- Links in (pages with a free slot): {2 or 3}
- Links out: {vendor}'s site, your related pages
- Conversion: {sign-up, pricing or setup page}

## Images

{a screenshot for each switch reason, never the same one twice; what each must show}

## Acceptance

- [ ] Brief check passes (seo-keyword-research)
- [ ] Every {vendor} cell has a URL and a date
- [ ] Winners computed by the rubric
- [ ] Content lint passes
- [ ] Independent seo-content-qa PASS (32/40 or more)
- [ ] A person read and fact-checked it
- [ ] Live, indexing request sent, `new page` experiment recorded

## Notes

{QA verdicts, `Approved: <name> <date>`}
