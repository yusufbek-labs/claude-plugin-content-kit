---
name: brand-voice
description: Captures a brand's writing voice from sample texts and saves it as a reusable voice profile (brand-voice.md). Use when the user shares past posts, emails or website copy and wants their tone, style or "how we sound" documented, or asks to create, update or check a brand voice profile.
argument-hint: "[paths to sample files, or paste text]"
---

# Brand voice capture

Turn sample writing into a short, reusable voice profile that other skills can follow.

## Steps

1. **Collect samples.** Use files named in `$ARGUMENTS`, text pasted in the chat, or ask for 3 to 5 pieces of real writing (blog posts, newsletters, About page). With fewer than 2 samples, say the profile will be low-confidence and continue.
2. **Analyse** only what the samples show. Cover the dimensions in [references/profile-template.md](references/profile-template.md): tone, sentence rhythm, vocabulary, point of view, formatting habits, things the brand never does.
3. **Quote evidence.** Every claim in the profile needs a short quote from a sample. Do not infer traits that are not visible.
4. **Write the profile** to `brand-voice.md` in the current project folder, using the template. If the file exists, show a short summary of what would change and ask before overwriting.
5. **Summarise** in 5 lines or fewer and tell the user they can edit `brand-voice.md` directly; the other skills read it.

## Rules

- Never invent facts about the business (names, products, numbers).
- Keep the profile under about 60 lines so it is cheap to reload.
- Include 2 "sounds like us" and 2 "does not sound like us" example sentences you write yourself, labelled as examples.
