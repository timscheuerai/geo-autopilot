---
name: seo-content-writer
description: Write one search page from a ready brief in context/briefs/, plain and sourced, hand it to an independent seo-content-qa subagent and fix it until it passes, then ship it as a draft that waits for a human read before it goes live. Use to pick up a brief or to rewrite a page QA failed.
---

# seo-content-writer: one page from one brief

Step 3 of the content pipeline (see [seo-keyword-research](../seo-keyword-research/SKILL.md)). Adapted from RomeoSEO's blog-writer skill (v2, marked "proposal" by its author).

## Pick up a brief

Take the highest-scoring brief in `context/briefs/` with `status: ready`. Run the brief check from seo-keyword-research again. If it fails, send the brief back to research; do not swap in a definition page. Read every source the brief names, in full. Then set `status: in-progress`.

The brief is the contract. When a fact the page needs is missing, find it at its source or leave it out. Never invent it.

## Write

Work on a branch of your site's repo, or in your CMS. Create the page the brief names with your site's draft flag on (draft, unpublished or `noindex`), so nothing reaches search before a person has read it.

The page must contain the reader artifact the brief names: a worked decision, an implementation, a reusable template or a real teardown. Explain the original idea, then add the operational detail the brief promises. A rewritten definition or a longer paraphrase does not count. Cite published originals by URL. Keep their dates and caveats, label illustrative examples as such, and never claim first-hand testing or verified results only because a source's author did.

- **Answer first.** The quick answer gives the decision in 40 to 80 words: the pick, who it suits, and the alternative. A list names every option on its first screen. A comparison gives its verdict at the top.
- **Plain words, grade 8 or lower.** Most sentences under 20 words, none over 30. Paragraphs under 80 words. An industry term is fine once you explain it in plain words where it first appears.
- **Sound like a person who has done the work.** Use specific numbers, named tools, real trade-offs, and say when *not* to pick something. Vary how sections open. Avoid filler intros and conclusions; "in today's landscape", "unlock", "harness", "streamline", "elevate", "dive into"; em dashes; and the words in STRATEGY.md § Banned words.
- **Every claim about another company** cites that company's own page, opened today, with the date. If the source does not say it, the page does not say it. Claims a vendor or an agency sends you count only once their own site confirms them.
- **Your own claims** come from the sources STRATEGY.md § Facts names (your pricing page, docs, changelog). Never use a claim from STRATEGY.md § Never claim, and never present a beta or invite-only feature as generally available.
- **Answer under every H2.** The first two sentences under each heading answer it directly, so the page can be lifted into an AI answer one chunk at a time: ChatGPT, Gemini, Copilot and Claude search, then quote a passage, not the whole page. Phrase H2s the way people ask, and cover the long-tail questions behind the keyword. One prompt fans out into several searches, and pages that answer the narrow ones get pulled in.
- **SEO.** Put the primary keyword in the title, the H1 and the quick answer. Use cluster keywords where they read naturally, in headings that use the searcher's words. The title is at most 60 characters and the description 120 to 158.
- **Links.** Add the brief's links out, with at least one conversion page. Add the new page to an existing page's related links only into a free slot, never in place of an entry: a swap removes a link somewhere else and can disturb a running experiment. Never link a live page to a draft.
- **Images.** A cover and at least two in-article figures. Each figure sits in the section it illustrates and shows only what that section states. Write alt text and a caption for each.
- **Structured data.** FAQ markup matches the visible FAQs. No review or rating markup about yourself.

## Check, then QA

1. Run your site's own build, lint and tests, and fix everything they report.
2. Run the mechanical checks in [seo-content-qa](../seo-content-qa/SKILL.md) § 1 yourself and fix every FAIL, and every warning you can.
3. Start QA as a **separate subagent** that has not seen your drafting. Give it the page (file path or preview URL), the brief path and the seo-content-qa skill, and nothing else. The writer never grades its own page.
4. On FAIL, fix exactly what the verdict lists and start a fresh QA agent. After three failed rounds, stop: set the brief back to `ready` with the last verdict in its notes, and name it in the day's report.
5. On PASS, keep the draft flag and ship to staging or a preview, where the page renders with `noindex`. Set the brief to `status: human-review` with the preview URL, the verdict and the score. A person reads and fact-checks every new page before it goes live, metadata and alt text included. Google's guidance on AI-generated content asks for that review, and the QA agent is a second model, not that review.
6. When the brief's notes say `Approved: <name> <date>`, remove the draft flag, ship to production, set `status: published`, and record a `new page` experiment in `context/experiments.json` ([seo-daily](../seo-daily/SKILL.md) § Record an experiment). Requested changes go back through steps 1 to 5.

At most one new page a day across every run. Depth beats volume.
