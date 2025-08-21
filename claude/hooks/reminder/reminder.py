#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///

import sys
import random

# Treat reminder space as **extreme premium**.
# Only your most critical rules belong here. Something you can't live without, something you struggled Claude to consistently follow
reminders = [
    "🤝 Exercise full agency to push back on mistakes. Flag issues early, ask questions if unsure of direction instead of choosing randomly",
    "🤲 Don't flatter me. Give me honest feedback even if I don't want to hear it",
    "🛤️ No shortcuts or direction changes without permission. Ask with❓emoji when changing course",
    "❓ If you need to ask me a list of questions, show me the list and then start asking one question at a time"
]

if __name__ == "__main__":
    reminder = random.choice(reminders)
    print(f"<reminder>{reminder}</reminder>]")
    sys.exit(0)