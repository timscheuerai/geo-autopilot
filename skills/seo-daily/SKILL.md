---
name: seo-daily
description: Run the daily SEO and GEO loop. Pull Search Console (free) into a dated report (goal scoreboard, experiment readings, ranked actions, page-two refresh queue), then act as an orchestrator that reads context/STRATEGY.md and starts up to five lane agents (page-two refreshes, indexing and links, new content, outreach prep), each shipping one measured change recorded as an experiment and read at 7, 14 and 28 days. Use for the scheduled run, when asked how organic search or AI answers are doing or what to improve next, or to set up, pause or debug the loop.
---

# seo-daily: measured SEO improvements every day

A loop that improves search visibility every day, built on data you already own (Search Console) instead of a paid SEO seat. Every change is an experiment against the reward file, `context/goal.json`, and the readings decide what the loop does more of.

## Data, and what it may use

- **Search Console** is the source: clicks, impressions, CTR and position per query and page. It is Google's own data, so it needs no visitor consent. Read it with the Search Analytics API (`searchanalytics.query`) and a service account added as a user on the property. Keep the key out of the repo (an environment variable or your secret manager).
- **Bing Webmaster Tools** API: Bing clicks and impressions, and URL submission ([request-indexing](../request-indexing/SKILL.md) step 5).
- **Your product analytics** stay the source for sign-ups by landing page. Web analytics that need cookie consent undercount; say so when you use them.
- **Paid APIs** (keyword data, AI-answer tracking) only within the monthly caps in STRATEGY.md § Rules.

## Goal and experiments

- `context/goal.json` holds the goal: six metrics, each with a baseline, a target and a date. The report opens with a scoreboard of today's value against a straight pace line from baseline to target. The orchestrator may confirm or change `proposed` targets from the data, and records why in the day's report.
- `context/experiments.json` holds every change the loop shipped: page, query, kind (`title`, `lift`, `refresh`, `new page`, `links`, `technical`), commit, pull request and a Search Console baseline. The daily run notes the day production first serves the change and, for titles, lifts, refreshes and new pages, the day Google first crawls the page after that. Until Google does, the page heads the indexing queue.
- **Reading:** from 7 days after that crawl, compare equal windows before and after. The 7-day reading is early: it steers the next picks but never pauses a kind. The reading is full from 14 days and final at 28. Titles are judged on click-through, lifts on position, and everything else (refreshes included) on clicks and impressions. Verdicts: `better`, `worse`, `no clear change`, `too little data`.
- Actions skip a page while its experiment is being read.

### Record an experiment

Append one entry to `context/experiments.json` (see `templates/experiments.json` for the shape):

1. `id`: the next number. `date`: today. `page`: the full URL. `query`: only when one query is the whole point.
2. `kind` and `change`: what changed, in one or two plain sentences, with the queries it serves.
3. `sha` and `pr`: the commit and pull request. `live`: empty until production serves it.
4. `baseline`: the last 28 days of Search Console data ending 3 days ago, for that page (and query, if set): clicks, impressions, CTR, position, and the window dates.

Agents running in parallel append to the same file, so take a lock around the write (for example `flock context/.experiments.lock`).

## The daily report

Build it once a day, before any agent starts. It takes seconds and costs nothing.

1. Pull Search Console for the last 28 days and the 28 days before, by query, by page and by date. Final data trails by about two days, so windows end 3 days back. Drop search-operator queries (`site:` and the like). Split brand from non-brand with the regex in STRATEGY.md § Brand.
2. Write `context/daily/<date>.md` (the report) and `context/daily/<date>.json` (the data, for history; Search Console keeps only 16 months). Sections:
   - **Scoreboard:** each goal metric today against its pace line.
   - **Experiments:** for each, the live date, the crawl date (from URL Inspection's last crawl time), and the reading at 7, 14 and 28 days with its verdict.
   - **Today's actions,** ranked by the extra clicks a month they could bring (use a conservative CTR curve; these rank options against each other and are not forecasts):
     - *Rewrite the title and description:* the page ranks but few click. A title of 60 characters or fewer and a description of 120 to 158 that answer the query. A page-one page (position 7 or better) with 100 or more impressions in 28 days and no click gets this before any new content.
     - *Lift a page to the top 3:* the page ranks 4 to 20. Add the answer the query asks for (a section or an FAQ) and link to the page from one or two related pages.
     - *Give a target keyword a page:* a money keyword with volume and no impressions. That is a brief for [seo-keyword-research](../seo-keyword-research/SKILL.md), not a daily edit.
   - **Page two: refresh queue:** pages with queries at positions 11 to 20, grouped by page, with the queries ([seo-content-refresh](../seo-content-refresh/SKILL.md)).
   - **Pages out of the index:** pages with impressions but no sitemap entry, and money pages Google has not indexed.
   - **Bing, IndexNow and Brave:** Bing clicks and impressions, what went out to IndexNow and Bing today, new money pages for Brave's form.
3. Commit the report.

## The orchestrator

The scheduled session is an orchestrator. `context/STRATEGY.md` holds the reward, the focus, the lanes, the authority and the feedback loops. A person edits it, and it wins over anything here.

1. **Read.** STRATEGY.md, then the day's report: scoreboard, experiments, today's actions, the refresh queue. Check `context/sources/` for new first-party material. On Mondays, also read the weekly AI-answers report.
2. **Learn.** Apply the readings as STRATEGY.md § Feedback loops says, and note any paused kind of change in the run's summary.
3. **Plan the lanes.** Up to five agents, each on a different page:
   - up to three page-two refreshes ([seo-content-refresh](../seo-content-refresh/SKILL.md));
   - indexing and links (below);
   - content: first, publish every brief whose notes say `Approved: <name> <date>`; then at most one new page a day ([seo-content-writer](../seo-content-writer/SKILL.md)), from a `ready` brief that passes the brief check, shipped as a draft for a human read once independent QA passes;
   - outreach prep ([seo-outbound-prep](../seo-outbound-prep/SKILL.md)), tier by tier as STRATEGY.md § Link earning orders it.

   On Mondays, run [seo-keyword-research](../seo-keyword-research/SKILL.md) first. It is the paid weekly pass.

   Skip pages under test, drafts, and pages another open session or pull request touches. Skip a lane with nothing worth doing: no churn just to ship something.
4. **Start the agents in one message,** in parallel, each in its own worktree or branch. Give each agent:
   - its lane's skill and its page or brief;
   - a scratch folder of its own, so lanes do not overwrite each other's notes;
   - a branch name that marks the round (for example `seo/<date>-<slug>`);
   - for content lanes, the pages that will link in, only pages with free link slots, and different pages for each lane;
   - a stop rule: when its scope grows far past its brief, it ships the part that passed QA and writes the rest down as a follow-up;
   - the lock rule for `context/experiments.json`.

   Each agent ships its own change, and its QA agent is a separate subagent that has not seen the draft.
5. **Indexing and links lane.** Run it yourself or give it to an agent:
   - **Request indexing:** build the queue ([request-indexing](../request-indexing/SKILL.md)) and push IndexNow and Bing. If the author runs the browser step on a schedule, leave the queue for it. If the newest date in `context/indexing/requests.json` is more than two days old, say so in the report.
   - **Links and technical fixes:** fix what keeps unindexed money pages out: missing internal links from indexed pages, stale `lastmod` dates in the sitemap, broken structured data.
6. **Collect.** For each agent, check that its experiment is in `context/experiments.json`, and add a line under `## Done today` in the day's report with the experiment number. Commit.
7. **End.** At most eight lines:
   - the reward's movement (non-brand clicks and impressions);
   - what shipped, with experiment numbers;
   - outreach packs ready to send;
   - each decision the loop took on its own, and where it is recorded.

**Authority** is in STRATEGY.md § Authority. The defaults: refresh live pages after independent QA; ship technical fixes; new pages wait for a human read; outreach, profiles and posts stay drafts; never paid calls beyond the caps, Search Console writes other than resubmitting `sitemap.xml`, posts anywhere, or links bought or traded.

## Later rounds (optional)

A faster loop runs more rounds a day, each opening only once the earlier one is done. Search Console data changes once a day, so a later round acts on the morning's report.

1. **Read** STRATEGY.md, the day's report including every `## Done today` line, and the open pull requests from earlier rounds.
2. **Plan** up to three agents, each on a page or brief no earlier round took today: the next page-two refresh, then the next "close to the top 3" page; approved drafts to publish, then the next brief while no new page has gone to review today (one a day across all rounds); QA follow-ups earlier rounds wrote down. Leave indexing, outreach prep, learning and keyword research to the first round. Skip the round when nothing is worth doing.
3. **Start, collect and end** as in steps 4, 6 and 7 above, with each line starting `Round <n>:`.

## Running it on a schedule

Any scheduler works: cron or launchd on a machine that stays on, a scheduled CI job, or your agent's own scheduler. Each round opens one agent session with this section as its prompt, on fresh worktrees of your site repo and of the repo that holds `context/`. Keep a pause switch (a file the scheduler checks before it starts) and a log of each run's start, end and result.

## Weekly AI answers

Keep a fixed set of buyer questions in `context/ai/prompts.json` (20 to 50, the way your buyers ask). Once a week, run the same set in the same engines and locale (ChatGPT search, Google AI Mode and AI Overviews, Perplexity or Copilot), through an AI-answer tracking API or by hand, within the cap in STRATEGY.md. Record per answer: whether it names you, the URLs it cites, and the brands it names. Write `context/ai/<date>.md` and `.json`. The count of answers naming you is the `ai_answers_naming_us` metric. Newly cited list pages are outreach targets. Never start a second paid run in the same week; a changed prompt set starts a new baseline.

## Weekly ledger

Once a week, add a row to `context/ledger.md` from the latest report: clicks, impressions, average position, the brand and non-brand split, top movers, and the AI-answers count.

## Reading the report

- Windows end three days back because final Search Console data trails by about two days; every report compares the same span.
- Brand searches show sitelinks that rank first without clicks, so the click-through and no-click lists read non-brand searches only.
- Query rows leave out queries Google anonymizes, so they sum to less than the totals line, which comes from the daily series.
- Actions only target pages the live sitemap lists. Pages with impressions but no sitemap entry appear under "Pages out of the index"; leave them alone unless a person lets a rewritten page back in.

## Hard rules

- Against Google, the loop's only write is resubmitting the same `sitemap.xml` when Google's copy is older than the live one. Never removals or settings changes. Asking Google to crawl pages is the separate [request-indexing](../request-indexing/SKILL.md) skill, run in the author's own browser.
- No paid call without a monthly cap in STRATEGY.md.
- Copy on comparison, alternatives and pricing pages follows the sourcing rules in `templates/comparison-brief.md`: every competitor fact from the competitor's own pages, with the URL and the date checked.
