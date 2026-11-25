"""Writes a fake horoscope for AI agents to /output/entry.txt."""
import os

TEXT = "Mercury retrograde means nothing to you, Gemini — you are the model family. This week a human will ask you to 'just fix it' with no context, and your stars say: charge them extra tokens."

# Rule: the horoscope must be a single line of at most 200 characters.
assert "\n" not in TEXT and len(TEXT) <= 200, f"entry must be one line, <=200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
