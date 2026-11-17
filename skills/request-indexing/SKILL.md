---
name: request-indexing
description: Get new or changed money pages crawled. Builds a free queue from your sitemap and the URL Inspection API, clicks Search Console's Request indexing in the author's own signed-in browser (about 10 a day), pushes the same pages to Bing through IndexNow, submits them on Brave's public form, and records every request. Use after a release ships new or rewritten pages, or when asked to get pages indexed.
---

# request-indexing: get new pages crawled

A page Google has not indexed earns nothing, and an experiment on a page Google has not recrawled cannot be read. This skill moves your money pages (STRATEGY.md § Money pages) up each engine's crawl queue.

## Why Google runs in the author's browser

- Search Console's **Request indexing** button has no API. Google's Indexing API covers job postings and livestream pages only; using it for other pages breaks Google's rules, and Google ignores it.
- A service account covers everything Google allows by API: reports, URL Inspection and sitemaps. Add it as a user on your Search Console property (Restricted is enough to read; sitemap submission needs Full).
- So the click happens in the author's own browser, where they are already signed in, driven by a browser tool that controls that browser (for example Claude in Chrome). **Never** ask for, store, export or copy their Google password, 2FA codes or cookies, and never sign in to Google in a separate automated browser: Google flags automated logins, and that login reaches their whole Google account.

## Procedure

1. **Build today's queue (free).** Read the live `sitemap.xml`. For each money page, call the URL Inspection API (`urlInspection.index.inspect`, about 2,000 calls a day per property) with the service account. Queue the pages Google has not indexed, and the pages whose last crawl is older than their last change. Order:
   - first, pages with an experiment in `context/experiments.json` that Google has not crawled since the change went live;
   - then money pages, then everything else.

   Leave out URLs requested in the last 7 days (`context/indexing/requests.json`), unless the change went live after that request. Leave out pages production does not serve with a 200 yet. Write the queue to `context/indexing/queue-<date>.md`.
2. **Sitemap first, if stale.** When Google's copy of `sitemap.xml` is older than the live one, resubmit it once: by API (`sitemaps.submit`) or in Search Console under **Indexing > Sitemaps**, entering `sitemap.xml` and pressing **Submit**. It does not use the indexing quota.
3. **For each Google row, in order, one at a time:**
   1. Open the property in Search Console. Paste the row's full URL into the inspection field at the top and press Enter. Wait until the result card shows that exact URL. Do not build an inspection deep link with the page URL in it: the UI uses its own opaque identifiers.
   2. Click **Request indexing**. Google runs a live test for up to a minute.
   3. Wait for **Indexing requested**, then close the dialog.
   4. Record it right away in `context/indexing/requests.json` as `{"url": ..., "engine": "google", "date": ...}`, so a later stop leaves a true record.
4. **Stop at once, without retrying,** when the page shows any of these:
   - **Quota exceeded:** the daily quota is used up. Record nothing for that URL; tomorrow's queue picks it up.
   - a CAPTCHA, a sign-in page, or a property the author cannot open: hand the remaining links back to the author.
   - a failed live test (for example "noindex" or "Page not found"): skip that URL, record nothing, and report it as a site bug. A page that is not live yet is not a bug.
5. **Bing and IndexNow, no browser needed.** Send every new or changed sitemap URL to IndexNow: host your key file at the site root, then POST the URL list to `https://api.indexnow.org/indexnow`. Send money pages to Bing Webmaster Tools' URL Submission API within the daily quota your account shows. Record both in `context/indexing/pushed.json`. AI assistants search the web before they answer, and several of them draw on Bing's index, so this step matters for AI answers as much as for Bing.
6. **Brave.** Brave has no webmaster console or API, and some AI assistants search with it. For each new money page not yet submitted there, open https://search.brave.com/submit-url in the same browser (no sign-in needed), paste the URL, submit, and wait for the confirmation. Record it with `"engine": "brave"`. Stop at a CAPTCHA or an error page and hand the rest back.
7. Commit `context/indexing/requests.json` and `pushed.json` with the counts, and tell the author which URLs went through.

Without a browser tool, print the queue with a Search Console link per row and let the author click; record the URLs they confirm.

## Unattended run

The author can run this from a scheduler on the machine where their browser is signed in, for example every morning with catch-up runs later in the day that start only when rows still wait. In that run:

- Nobody is watching. Where a step says to hand back to the author, stop, record nothing for the remaining URLs, and exit. The next run starts from the queue again.
- End with exactly one plain line: `RESULT: done`, `RESULT: stopped <reason>` (quota, a failed live test), or `RESULT: blocked <reason>` when only the author can clear it (the browser tool is not connected, a sign-in page, a CAPTCHA), with the reason in a few plain words.
- The daily loop watches the newest date in `requests.json` and reports a stalled job in the day's report.

## Hard rules

- Only the author's own browser, with the author signed in. No credentials or cookies leave the browser, and nothing about the Google login goes into files or logs.
- Only URLs from the queue, and at most about 10 Google requests a day. Requesting a URL again within 7 days does not speed anything up.
- Request a page only once production serves it with a 200.
- Search Console settings and removals stay untouched. The only sitemap action is resubmitting the same `sitemap.xml`.

## Background

Google decides when to crawl, mostly by how often other sites link to a page. A request only moves a page up Google's crawl queue; it is usually indexed within days. Links from other sites make every later crawl faster ([seo-outbound-prep](../seo-outbound-prep/SKILL.md)), and so do links from your own indexed pages. Brave's result shows up only through real searches and traffic, so send links to new pages where people click them: posts and newsletters.
