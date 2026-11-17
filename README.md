# GEO Autopilot

**Agent skills that find, write, check, ship and measure the pages that get your site found in Google and named in AI answers.**

This is the SEO and GEO loop I run with Claude Code, rebuilt so it works for any website. 7 skills cover every step from keyword research to outreach, and a daily run measures each change against a reward file, so the loop learns what works on your site.

GEO (generative engine optimization) is SEO for AI answers. ChatGPT, Gemini, Copilot and Claude search the web before they answer, then quote a passage from a page. The pages they quote are indexed, give the answer first, answer again under every heading, and source their facts.

**[Use this template](https://github.com/new?template_name=geo-autopilot&template_owner=timscheuerai)** · [Download ZIP](https://github.com/timscheuerai/geo-autopilot/archive/refs/heads/main.zip)

## The method in 5 steps

1. Write one page by hand. Pick the search that matters most to your business, often "{competitor} alternative", and write the best page on the internet for it yourself. That page is your template.
2. Let agents fill in the blanks across the rest. Turn your page into a brief with blanks for the vendor, the facts and the sources, and let agents fill it in for the next competitors and topics ([comparison brief](templates/comparison-brief.md), [guide brief](templates/guide-brief.md)).
3. Turn every step into a skill: research, brief, write, QA, ship, index, refresh, outreach, learn. A skill is a short manual your agent follows the same way every time.
4. Fine-tune the skills on the first pages. When a page comes out wrong, put the fix into the skill and run it again. Keep going until you trust it.
5. Put it on a loop against a reward file. [goal.json](templates/goal.json) holds the six numbers you want to move. A daily run reads Search Console, starts one agent per lane and records every change as an experiment, read at 7, 14 and 28 days.

## What you get

| Step | Skill | What it does |
|---|---|---|
| Research and brief | [seo-keyword-research](skills/seo-keyword-research/SKILL.md) | Starts from your own material, runs a capped keyword pass, scores clusters and writes 1 brief per page |
| Write and ship | [seo-content-writer](skills/seo-content-writer/SKILL.md) | Writes 1 page from 1 brief with every claim sourced, then ships it as a draft for a person to read |
| QA | [seo-content-qa](skills/seo-content-qa/SKILL.md) | A separate agent scores the page on 8 areas out of 40 and passes it at 32 with no critical fail |
| Index | [request-indexing](skills/request-indexing/SKILL.md) | Requests indexing in your own signed-in browser, pushes Bing through IndexNow, submits to Brave |
| Refresh | [seo-content-refresh](skills/seo-content-refresh/SKILL.md) | Adds a section for the queries a live page ranks 11 to 20 for |
| Outreach | [seo-outbound-prep](skills/seo-outbound-prep/SKILL.md) | Finds the lists that rank and the pages AI answers cite, and drafts the pitch for a person to send |
| Learn | [seo-daily](skills/seo-daily/SKILL.md) | The daily report and the orchestrator: up to 5 lane agents, every change an experiment, pauses what stays flat |

The [templates](templates/) hold the comparison brief, the guide brief (best-of list or pricing guide), the strategy file, the reward file and the experiment log.

## Start here

1. Click **[Use this template](https://github.com/new?template_name=geo-autopilot&template_owner=timscheuerai)** and clone your copy. Make it private once you add your own data.
2. Copy the templates into your workspace:

   ```bash
   cp templates/STRATEGY.md templates/goal.json templates/experiments.json context/
   ```

3. Give the agent read access to your data. For Search Console, create a service account in Google Cloud, turn on the Search Console API, and add the account's email as a user on your property (Full, if the loop should resubmit your sitemap). Optional: a Bing Webmaster Tools API key, an IndexNow key file at your site root, and a keyword API such as DataForSEO. Keep every key in environment variables or your secret manager, never in the repo.
4. Open the folder in Claude Code or Codex and paste:

   ```text
   Read AGENTS.md and README.md. Help me set up GEO Autopilot for https://YOUR-SITE.com.
   Fill in context/STRATEGY.md with me: ask for my buyers, the competitors they compare
   me with, where my product facts live, what I must never claim and my money pages.
   Then pull my first Search Console report with seo-daily, set the baselines in
   context/goal.json, and brief my first comparison page from templates/comparison-brief.md.
   I will write that first page myself.
   ```

To run the skills inside your website's repo instead, copy `skills/` into `.claude/skills/` (Claude Code) or `.agents/skills/` (Codex and other agents), and copy `context/` next to it.

## How the loop runs

```text
Search Console (free) ──> context/daily/<date>.md
        │
        v
orchestrator reads context/STRATEGY.md and starts up to 5 lane agents
        ├── refresh pages that rank 11 to 20 (up to 3 agents)
        ├── indexing and internal links
        ├── 1 new page a day: brief > write > separate QA > draft > a person reads > live
        └── outreach packs, drafts for a person to send
        │
        v
context/experiments.json: every change read at 7, 14 and 28 days
        │
        v
pause what stays flat, give more agents to what works
```

Run it once a day to start, from cron, a scheduled CI job or your agent's scheduler. Add later rounds once you trust it.

## Rules we learned the hard way

- Answer in the first 40 to 80 words, then again in the first sentence under every heading. AI answers quote a passage, not a page.
- Facts about a competitor come only from the competitor's own site, with the URL and the date you checked.
- The writer never grades its own page. A separate QA agent does.
- At most 1 new page a day, and a person reads every one before it goes live. Google asks for that human fact-check on AI-written pages, and its spam policy targets many pages made without added value.
- Refresh pages that rank 11 to 20 before you write new ones.
- Read every change at 7, 14 and 28 days. Pause a kind of change after 2 flat full readings.
- Outreach stays a draft until a person sends it. Never buy, barter or swap links.
- Request indexing only for pages production serves, from your own browser. Google's Indexing API is for job postings and livestreams only.

## What is in the repo

```text
skills/      7 skills: seo-daily (the loop), research, writer, QA, refresh, indexing, outreach
templates/   comparison-brief.md, guide-brief.md, STRATEGY.md, goal.json, experiments.json
context/     your workspace: strategy, reward file, experiments, sources, briefs, reports
scripts/     check-template.py, run before every commit to this template
```

## Credits

- The research, writer and QA skills are adapted from RomeoSEO's v2 skills (opportunity-research, content-brief, blog-writer and content-QA), which their author marked as a proposal.
- For a full technical site audit (crawl, Core Web Vitals, structured data, robots and AI crawlers), use [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) by Bhanu Namikaze (MIT), which grew out of AgriciDaniel's [claude-seo](https://github.com/AgriciDaniel/claude-seo).

Built by [Tim Scheuer](https://github.com/timscheuerai). [License](LICENSE)
