# Contributing to the Reel CTA Link Hub

Thanks for helping this hub stay useful. The rules are short, because the hub's
whole value is trust: a word must always lead to a real resource.

## Add a new resource

1. Add the resource file under `resources/`, for example `resources/NEWWORD.md`.
   Keep it copy-paste ready, in plain Markdown, with no passwords, personal
   data, or links to things that do not exist.
2. Add one entry to `resources.json`: word, title, one-line description,
   status, and file path.
3. Rebuild the search page with `python3 build.py`, which embeds the resources
   into `index.html`.
4. Update the table in `README.md` so the word, title, and file match.

## Rules

- **No fake links.** If a resource is not ready, its status stays
  `coming-soon` and it gets no file link.
- **One word, one resource.** Do not point two words at the same file unless
  the guide genuinely covers both.
- **Original or clearly credited.** Do not paste someone else's paid or
  private content. Your own guides, prompts, and checklists are welcome.
- **Keep it short and usable.** A visitor should be able to copy the text and
  use it in under 10 minutes, without buying anything first.

## Fix or improve a resource

Open a pull request with the changed file and a one-line note on what changed
and why. Small, focused fixes are better than rewrites.

## Star it if it helped

If any guide here saved you time, a Star on the repository helps other people
find it. That is also how a useful repo reaches GitHub Trending: real stars,
in a short time, from people who actually used it.
