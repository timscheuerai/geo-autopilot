---
name: seo-keyword-research
description: Find the next search pages worth writing. Start from your own first-party material, run a capped keyword and SERP pass, score each cluster for fit, de-duplicate against existing pages and briefs, and write one brief per page into context/briefs/. Use weekly, or when asked what to write next or for keyword research.
---

# seo-keyword-research: what to write next

Step 1 of the content pipeline: research and brief (this skill), [write](../seo-content-writer/SKILL.md), [QA](../seo-content-qa/SKILL.md), ship, [index](../request-indexing/SKILL.md), measure ([seo-daily](../seo-daily/SKILL.md)). Adapted from RomeoSEO's opportunity-research and content-brief skills (v2, marked "proposal" by their author).

Read `context/STRATEGY.md` first. Its Focus, Order of bets and Leave alone sections win over anything here.

## Start from what only you can write

A keyword tool tells you what people search. It does not tell you what you can say that the top 10 cannot. Start from the author's own material: posts, talks, playbooks, templates, lead magnets, and sales-call notes that someone cleared for public use. Keep each one, or a link to it, in `context/sources/`: one file per source with its URL, date and a short summary.

For every candidate page, name the reader artifact: a worked example, an implementation walkthrough, a decision framework, a teardown or a usable template that the source did not already give. A source link alone is not enough, and neither is a longer paraphrase of a post. Search volume decides between useful ideas. It never justifies a basic definition page ("what is X") on its own.

**Brief check.** A brief moves to `ready` only when all of these hold:

- every source it names exists in `context/sources/`, and you read it in full;
- the reader artifact is named in one sentence;
- the claim limits are written down: a dated result from an old post is history, not a current verified outcome, and a private note is not public copy until someone clears it.

A brief that fails the check stays `draft`.

## 1. Pull the data (paid, capped)

Use a keyword API: DataForSEO (Labs keyword ideas, keywords for site, ranked keywords, and the Google organic SERP endpoint) or the API of the SEO tool you already pay for.

- **Seeds:** your category, the jobs buyers hire you for, your competitors' domains, and the queries Search Console already shows your site for (seo-daily writes them to `context/daily/`).
- **Cap:** STRATEGY.md § Rules sets a monthly budget. Estimate a run's cost before you start it, never start one that would pass the cap, and log every call's cost in `context/research/spend.json`.
- **Cadence:** at most once a week. Between runs, work from the latest report.
- **Clusters:** keywords whose Google top 10 share three or more URLs belong together, so one page can win all of them. For each cluster, record what ranks now (page types and angles), your position, and any page of yours that already matches.
- **Output:** `context/research/<date>.md` (readable) and `context/research/<date>.json` (data).

## 2. Judge each cluster

Score each cluster 0 to 5 on six things, and write down the reason:

- **Business fit:** would the searcher be your buyer (STRATEGY.md § Focus)?
- **Can you answer it truthfully?** Check STRATEGY.md § Facts. A page that needs a claim you cannot make scores 0.
- **Demand:** volume and trend.
- **Odds of ranking:** difficulty, plus whether the top 10 holds pages you can beat. Vendor blogs and listicles yes; review sites, analyst firms and big brands' own product pages rarely.
- **Conversion path:** does the page lead naturally to a sign-up, the pricing page or a setup doc?
- **Effort:** a refresh is cheaper than a new page.

Then pick one action per cluster:

- **Defend:** you rank 1 to 10. Do not write a new page; a lift may go to seo-daily.
- **Page-two push:** you rank 11 to 30. Refresh the existing page ([seo-content-refresh](../seo-content-refresh/SKILL.md)).
- **New page:** nothing of yours matches the search intent.
- **Skip:** wrong intent (navigational, jobs, another meaning of the word), a fact you cannot support, or a results page made only of forums or review sites.

Choose the page type the results page rewards:

- comparison, you against one vendor ([comparison brief](../../templates/comparison-brief.md));
- alternatives page for one vendor;
- best-of list or another vendor's pricing guide ([guide brief](../../templates/guide-brief.md)). If you list yourself, say so on the page and say who should pick something else;
- guide article, for lists of things you are not;
- category explainer;
- docs page.

## 3. De-duplicate

Search `context/briefs/`, your sitemap and your site's drafts. Compare by search intent, not exact words. If a page or brief already covers the cluster, add the new keywords to it instead of writing another.

One intent, one page. Never write near-copies such as "{vendor} alternative for {audience}" for every audience: they split your own ranking, and they are what Google's spam policy on scaled content targets.

## 4. Write one brief per page

Copy the matching template into `context/briefs/<slug>.md` and fill it in. Every brief holds:

- **Keyword:** the primary keyword, the cluster keywords, volume, difficulty, intent and market.
- **Original contribution:** the source files and URLs, the reader's problem, the added artifact, existing coverage to avoid, and the claim limits.
- **Page:** type, the file or CMS entry to create in your site, and the URL.
- **What ranks now:** the top 5 (domain, page type, angle) and the gap you can fill credibly.
- **Outline:** the answer to give first; the H2s searchers expect, phrased as their questions, including the narrow long-tail ones an AI answer fans out into; 5 to 8 FAQ questions in the searcher's words.
- **Facts to source:** every claim about another company comes from that company's own page, checked within 120 days. Your own facts come from the sources STRATEGY.md § Facts names. List the claims you cannot make.
- **Links:** two or three existing pages that should link to the new one (only where they have a free slot), the pages it links to, and one conversion link.
- **Images:** what a screenshot or diagram should show.
- **Acceptance:** the brief check passes, the artifact is on the page and grounded in its sources, independent seo-content-qa passes, a person has read it, and it is live.

Write at most 10 briefs a week, highest score first, so briefs do not pile up faster than pages ship. Commit the research report and its briefs together.
