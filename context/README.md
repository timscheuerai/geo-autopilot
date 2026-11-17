# context/

Your SEO workspace. The skills read and write everything here, so keep it in a private repo once you fill it in.

Start by copying the templates in:

```bash
cp templates/STRATEGY.md templates/goal.json templates/experiments.json context/
```

Fill in every `<...>` in `STRATEGY.md`, set the baselines and targets in `goal.json` from your first report, and delete the fictional example in `experiments.json` (leave `[]`).

| Path | Written by | What it holds |
| --- | --- | --- |
| `STRATEGY.md` | you | Reward, focus, order of bets, leave-alone list, facts, authority, rules. The loop reads it first. |
| `goal.json` | you, then the loop | The reward file: six metrics with baseline, target and date |
| `experiments.json` | every lane | Each shipped change with its baseline and readings at 7, 14 and 28 days |
| `sources/` | you | Your first-party material: posts, talks, playbooks, templates, cleared call notes. One file per source with its URL and date |
| `research/<date>.md`, `.json`, `spend.json` | seo-keyword-research | Weekly keyword and SERP pass, clusters, scores, and the spend log |
| `briefs/<slug>.md` | seo-keyword-research | One brief per page, from `templates/`. Status: `draft`, `ready`, `in-progress`, `human-review`, `approved`, `published` |
| `daily/<date>.md`, `.json` | seo-daily | The daily report: scoreboard, experiments, actions, refresh queue, `## Done today` |
| `indexing/requests.json`, `pushed.json`, `queue-<date>.md` | request-indexing | What was requested from Google and Brave, what went to IndexNow and Bing |
| `outbound/PLAN.md`, `<publisher>.md`, `batch-<n>.md`, `profiles.md` | seo-outbound-prep | Target table, one pack per publisher, batches to send, directory profiles |
| `ai/prompts.json`, `ai/<date>.md`, `.json` | seo-daily | The fixed buyer questions and each week's AI-answer run |
| `ledger.md` | seo-daily | One row a week |

Credentials never go here. Keep the Search Console service-account key, the Bing and keyword API keys and the IndexNow key in environment variables or your secret manager.
