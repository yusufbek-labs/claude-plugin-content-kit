# Content Kit - a sample Claude Code plugin

**This is a sample project**, built as a portfolio piece. It shows how a small team's writing workflow can be packaged as a Claude Code plugin. It has no real clients, no testimonials and no performance numbers, and it has not been used in production.

## What it is

Content Kit adds a small blog-and-social workflow to Claude Code:

| Piece | Name | What it does |
| --- | --- | --- |
| Skill | `brand-voice` | Reads your past writing and saves a short voice profile (`brand-voice.md`). |
| Skill | `blog-draft` | Turns a topic into an outline (you approve it), then a full draft in your voice. |
| Skill | `repurpose-post` | Turns a finished post into LinkedIn, X and newsletter versions. |
| Command | `/content-kit:new-post` | Runs voice check, outline, draft and editor review in one go. |
| Command | `/content-kit:publish-pack` | Reviews a finished post, then creates the three promo versions. |
| Agent | `editor` | A read-only reviewer that checks voice, clarity and unsupported claims. |
| Hook | placeholder check | After a draft is saved, reminds Claude if `[ADD: ...]` or `[LINK]` placeholders are left. Advisory only; never blocks. |

Nothing is ever posted or sent for you. Output is text files in a `drafts/` folder for you to review.

## Install in 3 steps

You need Claude Code installed. The hook also uses Node.js. Without Node the hook is skipped (Claude Code may show a hook error) and everything else works.

1. **Get the folder.** Download or copy this `claude-plugin-content-kit` folder somewhere on your computer.
2. **Add it as a local marketplace.** In your terminal:
   ```
   claude plugin marketplace add ./claude-plugin-content-kit
   ```
   (Use the full path to the folder if you are not in its parent directory.)
3. **Install the plugin:**
   ```
   claude plugin install content-kit@content-kit-samples
   ```

Then start Claude Code in the folder where your content lives. Inside a session you can also use `/plugin` instead of the terminal commands, and `/reload-plugins` after any change.

Just want to try it without installing? Run `claude --plugin-dir ./claude-plugin-content-kit/plugins/content-kit`.

## Usage examples

**1. Teach it your voice (once).** Put 3 to 5 of your best past posts or emails in a folder, then say:

> Capture my brand voice from the files in ./samples

It writes `brand-voice.md`. Open it and fix anything that does not sound like you.

**2. Write a post.**

> /content-kit:new-post Five questions to ask before hiring a bookkeeper

It proposes an outline and waits for your OK, saves the draft to `drafts/`, then the editor agent reviews it. Anything it could not know (real examples, statistics) is left as an `[ADD: ...]` placeholder rather than invented.

**3. Make the promo pack.** After you have edited the draft and changed `status: draft` to `status: final`:

> /content-kit:publish-pack drafts/five-questions-bookkeeper.md

You get LinkedIn, X and newsletter versions in `drafts/five-questions-bookkeeper-repurposed.md`.

You can also just ask in plain words ("rewrite this post for LinkedIn"); the skills trigger on their own.

## How to customise

All of it is plain text. Edit the files under `plugins/content-kit/`:

- **Voice profile layout:** `skills/brand-voice/references/profile-template.md`
- **Post shapes and default length:** `skills/blog-draft/references/post-structures.md` and `skills/blog-draft/SKILL.md`
- **Channel rules** (word counts, hashtags, subject-line length): `skills/repurpose-post/references/channel-specs.md`
- **Editor strictness:** `agents/editor.md`
- **Workflow order:** `commands/new-post.md` and `commands/publish-pack.md`
- **Add a channel** (for example Instagram): add a section to `channel-specs.md` and one line to the steps in `repurpose-post/SKILL.md`.
- **Turn the hook off:** delete `hooks/hooks.json`.
- **Change the author/name:** `.claude-plugin/plugin.json` (the plugin name cannot start with `claude-`).

Run `/reload-plugins` (or restart Claude Code) after edits.

## Project layout

```
claude-plugin-content-kit/
├── .claude-plugin/marketplace.json     local marketplace catalog
└── plugins/content-kit/
    ├── .claude-plugin/plugin.json      plugin manifest
    ├── skills/{brand-voice,blog-draft,repurpose-post}/   SKILL.md + references/
    ├── commands/{new-post,publish-pack}.md
    ├── agents/editor.md
    ├── hooks/hooks.json
    └── scripts/check-placeholders.mjs
```

## Honest notes

- Written against the Claude Code plugin docs as of November 2026 (code.claude.com/docs). Plugin formats change; check the docs if something does not load.
- Statically checked with a script (JSON and frontmatter). It was **not** run through `claude plugin validate` or tested live, because the Claude CLI was not available when this was built.
- AI drafts need human review. The editor agent helps but does not replace you.

License: MIT.
