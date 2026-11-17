---
name: seo-content-refresh
description: Refresh one live page for the queries Google already ranks it 11 to 20 for, by adding or rewriting a section that answers them, then pass independent QA, ship and record a refresh experiment. Use for the page-two lane of the daily loop, or when asked to refresh a page for its page-two keywords.
---

# seo-content-refresh: move a page from page two to page one

The first lane in `context/STRATEGY.md` § Lanes. Look at what you already rank for on page two in Search Console, add a section that answers those queries, and the page moves up. For a site whose pages already rank, this is the highest-impact change there is, so it comes before new pages.

Live pages may be refreshed without asking a person when STRATEGY.md § Authority says so, within the rules below.

## Pick the page

Take one entry from the day's report, section "Page two: refresh queue" (`context/daily/<date>.md`; the data is in `<date>.json`). When several agents run, each one gets a different page. Skip a page that has an experiment still being read, an open pull request from another session, or a draft flag.

## Decide the change

1. Read the page as production serves it, and its source file or CMS entry.
2. Group the page's page-two queries by intent. One section serves one intent: "acme alternatives" and "alternatives to acme" are one section; "acme api limits" may be another, or none.
3. For a substantial new section, check `context/sources/` for a post, playbook or template of the author's that answers the intent. Prefer a source-backed worked decision or implementation over padding a definition, and note the source and the added value for QA. Factual or technical repairs can stay narrow.
4. Pick the format the query asks for:
   - **How-to:** a "how to" or "how do I" query. Numbered steps someone can follow, each matching your product as it is today.
   - **Comparison row or table:** "X vs Y" or "X alternative". Add a row or a short table, with every competitor cell sourced from the competitor's own page.
   - **FAQ:** a question query. A one-sentence answer, then up to three sentences of detail.
   - **Rewrite:** if a section already covers the intent, rewrite it so its heading and first sentence use the query's words. Do not add a near-duplicate section.
5. Drop a query that does not fit the page: another company's brand query, an unrelated meaning, or a query only a new page could serve. Turn that last kind into a brief through [seo-keyword-research](../seo-keyword-research/SKILL.md).

## Write

- Answer first: the first sentence under the heading answers the query in 25 words or fewer, and the query's words are in the heading.
- Grade 8 or below, no em dashes, no AI-slop phrases, only sourced numbers. Voice, claims and limits are the same as [seo-content-writer](../seo-content-writer/SKILL.md).
- Stay inside the page template's limits on sections, lengths and sources. Add each new source to the page's source list with today's date.
- A new source moves the page's "reviewed" or "updated" date to today, so the whole page must be true today. Before QA, re-check every fact and source on the page against today's version, not only the new section.
- Keep the title and slug of a page that ranks. Changing them is a separate title experiment, never part of a refresh.
- Add a figure when the new section explains a process, a comparison or a set of tools.
- Link from the new section to one related live page, and from one related live page back to this one where it reads naturally and a free slot exists.

## Check, QA, ship

1. Run your site's build, lint and tests.
2. Run the mechanical checks in [seo-content-qa](../seo-content-qa/SKILL.md) § 1 and fix every FAIL.
3. Start an independent QA subagent with seo-content-qa, the page and the queries, and nothing else. On FAIL, fix what it lists and start a fresh one. After three failed rounds, stop and report the page back unchanged.
4. On PASS, ship the change the way your site ships (pull request, review, merge, deploy).
5. Record a `refresh` experiment in `context/experiments.json` ([seo-daily](../seo-daily/SKILL.md) § Record an experiment): the page, the section added or rewritten and the queries it serves, the commit and the pull request. Set a single `query` only when one query is the whole point; otherwise the page's clicks and impressions are judged.

## Report back

Give the page, the queries served, the section heading, the QA score, the pull request and commit, and the experiment number. If you changed nothing, say why.
