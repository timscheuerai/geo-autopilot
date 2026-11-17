# Working in GEO Autopilot

Read README.md, then the skill for the task in `skills/`. This repo is a set of agent skills and templates that find, write, check, ship and measure search pages for one website, with `context/` as the workspace the skills read and write.

- The canonical skills are in `skills/`. `.agents/skills` and `.claude/skills` point to that folder. Update `skills/catalog.json` when a skill's name or description changes.
- Read `context/STRATEGY.md` before any SEO work. If it is missing or still has `<...>` blanks, help the reader fill it in from `templates/STRATEGY.md` first. Its rules win over the skills.
- Facts about the reader's product come only from the sources STRATEGY.md § Facts names. Facts about another company come only from that company's own pages, with the URL and the date checked. Unknown facts stay unknown: ask, or leave them out.
- The writer never grades its own page. QA runs as a separate subagent that has not seen the draft.
- New pages ship as drafts and go live only after a person writes `Approved: <name> <date>` in the brief. At most one new page a day.
- Outreach, profiles, posts and comments stay drafts. Never send, post, submit a form or create an account. Never buy, barter or swap links.
- Paid API calls run only within the monthly caps in STRATEGY.md § Rules. State the cost before a paid run.
- Never ask for, store or copy the reader's Google password, 2FA codes or cookies. Keys live in environment variables or a secret manager, never in the repo.
- Before committing changes to this template, run `python3 scripts/check-template.py`.
