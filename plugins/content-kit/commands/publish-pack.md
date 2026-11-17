---
description: Review a finished post and turn it into LinkedIn, X and newsletter versions
argument-hint: "[path to post]"
---

Prepare the promotion pack for this post: $ARGUMENTS

1. If no path was given, list the files in `drafts/` and ask which one to use.
2. Delegate to the `content-kit:editor` agent for a final review of the post. If it reports any blocking issue, show it and stop; ask whether to continue anyway.
3. Use the `repurpose-post` skill on the post to create the LinkedIn, X and newsletter variants.
4. Show where the output was saved and remind the user that nothing has been posted or sent.
