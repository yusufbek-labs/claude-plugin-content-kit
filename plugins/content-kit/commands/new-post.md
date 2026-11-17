---
description: Write a new blog post from a topic, in your brand voice, with an editor review
argument-hint: "[topic]"
---

Run the content workflow for a new blog post on this topic: $ARGUMENTS

1. Check whether `brand-voice.md` exists in the project folder. If not, ask whether to build one first using the `brand-voice` skill (ask the user for sample texts) or to continue without it.
2. Use the `blog-draft` skill to produce an outline. Pause for the user's approval before drafting.
3. After the draft is saved, delegate to the `content-kit:editor` agent with the draft path and the `brand-voice.md` path, and show its review.
4. Finish with a short summary: draft path, items to verify, and the next step (`/content-kit:publish-pack <draft path>` once the user has revised the post and marked it final).
