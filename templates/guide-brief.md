---
status: draft          # draft, ready, in-progress, human-review, approved, published
type: best-of list     # best-of list or pricing guide
slug: {slug}
score:
---

# Brief: {title}

For a best-of list ("best {category} tools") or a pricing guide for another vendor ("{vendor} pricing"). Both are buyer searches, both get cited by AI answers, and both stay useful only if they are refreshed. Replace each `{...}` and delete these notes.

## Keyword

- Primary: {keyword}
- Cluster: {keywords whose top 10 share three or more URLs}
- Volume, difficulty, intent, market: {from the research report}
- Page-two queries to answer (from Search Console): {list}

Title: at most 60 characters, primary keyword first, the year if the results page uses it. Description: 120 to 158 characters that make the click worth it.

URL: `/guides/{slug}`

## Original contribution

- Sources: {files in context/sources/}
- The reader artifact: {a worked cost example, a decision table, a template}
- Claim limits: {dated results stay dated}

## Page, in this order

1. **Answer first** (40 to 80 words): the pick, who it suits, and the alternative. A list names every option on its first screen. A pricing guide gives the entry price and what a typical team pays.
2. **Comparison table:** one row per tool (or per plan, for a pricing guide). Columns: {who it suits, entry price, the deciding features, free plan}. Every cell sourced.
3. **The body:**
   - *Best-of list:* one entry per tool with who it suits, strengths, watch-outs, the price from its own pricing page with the date, and a link to its site. If you list yourself, say so, and say who should pick something else.
   - *Pricing guide:* current plans and credit or usage costs from the vendor's own pages; what one real task costs (a worked example with the numbers shown); a dated "Prices checked {date}" line; and what the same task costs with you, if you sell something comparable.
4. **How we picked:** claims nothing the page cannot show. "We chose these tools ourselves; each entry says who it suits" is enough. Never "the most popular" without a source.
5. **FAQ** (5 to 8): the page-two queries first, in the searcher's words. The first sentence answers the question; up to three sentences of detail follow. The FAQ markup matches.
6. **Sources:** every outside fact with its URL and the date checked.
7. **One next step:** a single conversion link that fits the reader (sign-up, pricing, a setup doc), not three competing calls to action.

## Rules

- Answer under every H2: the first sentence answers the heading in 25 words or fewer.
- Every claim about another company from that company's own page, checked within 120 days. When its pages disagree, say which page says what.
- Your own facts only from STRATEGY.md § Facts; nothing from § Never claim.
- Refresh once a month: prices, new tools, a dated updated line, the next step still right.

## Links

- Links in (pages with a free slot): {2 or 3}
- Links out: each tool's site, your related pages
- Conversion: {one page}

## Images

{a cover, the decision table as a figure, a screenshot of the pricing math}

## Acceptance

- [ ] Brief check passes (seo-keyword-research)
- [ ] Every outside fact has a URL and a date
- [ ] Independent seo-content-qa PASS (32/40 or more)
- [ ] A person read and fact-checked it
- [ ] Live, indexing request sent, `new page` experiment recorded

## Notes

{QA verdicts, `Approved: <name> <date>`}
