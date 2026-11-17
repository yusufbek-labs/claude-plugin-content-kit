// Advisory PostToolUse hook. Reads the hook JSON from stdin; if a Markdown file
// inside a "drafts" folder still contains [ADD: ...] or [LINK] placeholders,
// it tells Claude. It never blocks: it always exits 0 and fails open on any error.
import { readFileSync } from "node:fs";

try {
  const input = JSON.parse(readFileSync(0, "utf8"));
  const file = input?.tool_input?.file_path;
  if (typeof file === "string" && /[\\/]drafts[\\/][^\\/]+\.md$/i.test(file)) {
    const text = readFileSync(file, "utf8");
    const hits = text.match(/\[(ADD:[^\]]*|LINK)\]/g);
    if (hits) {
      process.stdout.write(JSON.stringify({
        hookSpecificOutput: {
          hookEventName: "PostToolUse",
          additionalContext: `Note: ${hits.length} placeholder(s) remain in the draft and must be filled before publishing: ${hits.slice(0, 5).join(", ")}`
        }
      }));
    }
  }
} catch {
  // fail open
}
process.exit(0);
