---
name: blog-draft
description: Turns a topic into a blog post outline and then a full draft written in the brand's voice. Use when the user wants to write, outline or draft a blog post or article from a topic, idea or notes, especially when a brand-voice.md profile exists.
argument-hint: "[topic]"
---

# Blog outline and draft

Topic: $ARGUMENTS (if empty, ask for the topic, the target reader, and the one action the reader should take).

## Steps

1. **Load the voice.** Read `brand-voice.md` in the project folder. If it is missing, say so and offer to run the `brand-voice` skill first; continue in a plain, friendly tone only if the user declines.
2. **Brief.** Confirm in one line: reader, goal, target length (default 700-900 words), and any facts or sources the user supplies. Ask at most 3 questions, only for what is missing.
3. **Outline.** Produce a headline, 3 to 5 sections each with a one-line purpose, and a closing call to action. Use the shapes in [references/post-structures.md](references/post-structures.md). **Stop and wait for the user to approve or adjust the outline.**
4. **Draft.** Write the full post following the approved outline and the voice profile. Save it to `drafts/<kebab-case-title>.md` with front matter: `title`, `status: draft`, `topic`.
5. **Hand off.** Report the word count and list every factual claim, statistic or quote the user must verify. Suggest running the `editor` agent.

## Rules

- Do not invent statistics, quotes, customers, testimonials or sources. Use a clearly marked placeholder such as `[ADD: real example from your business]` instead.
- Lead with the reader's problem, not the company.
- Short paragraphs (1-3 sentences), descriptive subheadings, no filler openers.
