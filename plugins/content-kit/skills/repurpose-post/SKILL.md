---
name: repurpose-post
description: Repurposes a finished blog post into a LinkedIn post, an X (Twitter) post or thread, and a newsletter version, keeping the brand voice. Use when the user wants to promote, share, adapt, cross-post or turn an existing article into social posts or an email newsletter.
argument-hint: "[path to finished post]"
---

# Repurpose a post

Source post: the file in `$ARGUMENTS`, or the post the user just pasted or finished. If none is clear, ask.

## Steps

1. Read the post and `brand-voice.md` if present. If the post's front matter says `status: draft`, tell the user it is not marked final and ask whether to continue.
2. Extract the single core idea, 3 supporting points, and the call to action.
3. Write three variants, each rewritten for its channel rather than just shortened, following [references/channel-specs.md](references/channel-specs.md):
   - LinkedIn post
   - X: one post, plus an optional thread
   - Newsletter section (subject line, preview text, body)
4. Save all three to `drafts/<post-name>-repurposed.md` under three headings.
5. Report character counts for the X posts and flag anything over the limit.

## Rules

- Add no new claims, numbers or quotes that are not in the source post.
- Keep links as placeholders (`[LINK]`) unless the user gave a URL.
- Never publish or send anything; output is text for the user to review and post themselves.
