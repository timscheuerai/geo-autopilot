---
name: seo-content-qa
description: Independent pre-publish gate for one search page. Checks reading level, AI-sounding prose, SEO, every claim against its source, images, links and calls to action, scores eight areas out of 40 and returns PASS or FAIL with exact fixes. Run as a separate agent after seo-content-writer or seo-content-refresh, on any page before a person reviews it, or to audit a published page.
---

# seo-content-qa: nothing ships that fails this

Step 4 of the content pipeline (see [seo-keyword-research](../seo-keyword-research/SKILL.md)). The bar: readable with no jargon, not AI slop, fully search-optimised, no made-up claims, useful images and the right call to action. The rubric is adapted from RomeoSEO's content-QA skill (v2, marked "proposal" by its author).

Work as the reader's advocate, not the writer's. You review; you do not rewrite the page. Fix nothing yourself unless the person who started you asks. Your output is the verdict.

You must be a fresh agent that has not seen the drafting. If you wrote or edited this page in this session, stop and ask for a separate QA agent.

## Inputs

The page (a file in the site repo or a preview URL) and its brief in `context/briefs/`. Read the brief first: it sets the keyword, the page type, the facts, the links and the reader artifact. For a refresh, the input is the page plus the queries it was refreshed for.

Read and write only in a scratch folder of your own. Shared scratch folders hold the writer's notes and other agents' downloads.

## 1. Mechanical checks

For a new page, run the brief check from seo-keyword-research yourself: the sources exist, the reader artifact is named, the claim limits are written down. A failed brief check is a critical fail.

Then check the page. Each check is pass, warn or FAIL:

| Check | Pass | FAIL |
| --- | --- | --- |
| Flesch-Kincaid grade of the body copy | 8 or lower (warn above 8) | above 10 |
| Sentence length | most under 20 words | any over 30 |
| Paragraph length | under 80 words | (warn only) |
| AI-slop phrases and repeated section openings | none | any phrase from the writer's avoid list or STRATEGY.md § Banned words, or three sections that open the same way |
| Keyword placement | in the title, the H1 and the first 80 words, reading naturally | missing from any of the three, or stuffed into every paragraph |
| Title and description | title 60 characters or fewer, description 120 to 158 | outside either limit |
| Links | at least two internal links and one conversion link | no conversion link |
| Images | each has alt text that describes it | (follow-up if your template shows no images yet) |
| Answer-first sections | the first sentence under each H2 is 25 words or fewer and answers the heading | a section that opens without answering |
| Site checks | the site's build, lint and tests pass | any failure |

Grade with a readability library (for example the `textstat` Python package) or the formula: 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59. Leave out tables, code and the terms STRATEGY.md lists as allowed.

## 2. Read every claim (the part a script cannot do)

- **Another company's claims:** open each cited source and find the sentence that supports the claim. Critical fails:
  - a number, price, location, customer name, result, award or "only X does Y" that the source does not support;
  - a source that answers 404;
  - a superlative about a competitor without evidence.

  Vendor or agency copy sent to you is not a source. A third-party site is not a source for a fact about a vendor.
- **Your own claims:** match each one against the sources STRATEGY.md § Facts names. Critical fails: a feature you do not have, a beta or invite-only feature presented as available, anything on STRATEGY.md § Never claim, and a price that differs from the live pricing page.
- **Jargon:** every allowed term is explained in plain words where it first appears.
- **Original reader value:** find the worked example, implementation, decision framework, teardown or template the brief promised. Check how it goes beyond the source and helps the reader's stated problem. A citation attached to a generic definition or a paraphrased post is a critical fail. A dated past result cannot become a current verified outcome. Private notes must not appear in public copy.

## 3. Score eight areas, 0 to 5

| Area | 5 means |
| --- | --- |
| Search intent | The page type and depth match what Google's top 10 rewards for the keyword. The answer comes first. |
| Structure and usefulness | The reader artifact works as a useful example or template, beyond a definition. Quick answer, scannable H2s, every option named early in a list, a verdict early in a comparison, FAQs a buyer actually asks. |
| Plain, human writing | Grade 8 or lower, short sentences, specific examples and trade-offs, varied rhythm, opinions where the reader needs a decision, no filler. |
| SEO | Keyword in the title, H1 and opening; cluster terms in natural headings; title and description within limits and worth the click. |
| Your accuracy | Every claim about your own product true today, with its limits stated plainly. |
| Competitor and source safety | Every outside claim sourced and supported; verdicts framed as fit, not absolute superiority. |
| Links, images and calls to action | Links in and out, one conversion link, a call to action that fits the page, images that show the product or the decision, descriptive alt text. |
| Ready to ship | Draft flag on, nothing breaks the layout (desktop and a 390 px phone), structured data matches the visible FAQs. |

## Critical fails

Any one of these means FAIL, whatever the score:

- wrong intent or page type;
- no answer first;
- a false or unsupported claim about you or anyone else;
- grade above 10;
- obvious AI prose;
- a new page without the brief's original, source-grounded reader artifact, including a standalone definition page;
- a failed mechanical check or site check;
- a named tool in a list or comparison with no link to its site;
- the title or slug of a page that already ranks changed without a written risk note;
- a figure that puts one company's fact under another company's name.

Open every image: it must be readable at article width, show only facts its section states, and have alt text that describes it. A page without a cover and at least two figures is a follow-up while your template shows no images, and a FAIL after that.

## Verdict

PASS needs no critical fail, a score of 32/40 or more, and no area below 3. Return exactly:

```
QA verdict: PASS | FAIL · score X/40 · grade N.N
Critical fails: none | list
Fixes required (section or field, then the exact change):
1. ...
Optional improvements (at most 3):
Follow-ups for a person (claims to confirm, images to add):
```

Write the verdict into the brief's notes. The writer fixes the page and asks for QA again. Every re-run gets a fresh agent, which scores the page again from the start.
