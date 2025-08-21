# Claude Code Reminder Hook

A lightweight Claude Code hook that ensures your assistant consistently follows your most important rules by injecting contextual reminders with each user prompt.

## What It Does

This hook solves a common frustration: Claude Code forgets to follow your critical rules from `CLAUDE.md`, especially as the conversation gets longer.
But it is very good and consistent when using its internal tools like TODOs. Why is it so good at those and so bad at following your instructions?
Part of the reason is that Anthropic uses hidden `<system-reminder>` tags to nudge Claude Code toward certain behaviors. 
This project brings that same power to you, allowing you to inject your own reminders that appear before each user prompt.

## How It Works

The hook:
1. Runs automatically when you submit a prompt (via the `UserPromptSubmit` event)
2. Selects a random reminder from your list of reminders
3. Injects it as a `<reminder>` tag that's visible to Claude Code but mostly invisible to you
4. Helps Claude Code maintain consistent behavior across long conversations

You can view these reminders after installing this hook by starting a new Claude Code session and:
- Pressing `Esc` twice after Claude finishes responding
- Checking conversation logs in `~/.claude/projects/` for a given conversation

## Installation

### Prerequisites
- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) - Install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Or modify the shebang in `reminder.py` from `#!/usr/bin/env -S uv run --script` to `#!/usr/bin/env python3`

### Step 1: Clone or Download
1. Clone this repository
2. Copy the `claude/hooks/reminder/` folder to wherever you want to store your hooks
   - For example: `~/.claude/hooks/reminder/` for global use
   - Or: `/path/to/your/project/.claude/hooks/reminder/` for project-specific use

### Step 2: Configure Settings

**Add this to your `settings.json`:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "<PATH_TO_REMINDER_SCRIPT>"
          }
        ]
      }
    ]
  }
}
```

**Path options:**
- **Global** (user level, applies to all conversations): `~/.claude/settings.json`
- **Project** (project level): `$PROJECT_DIR/.claude/settings.json`

**If settings.json doesn't exist yet:**
1. Type `/hooks` in Claude Code to create a dummy hook. Select one of the options, for example, stop hook. Create command like 'ls' or 'pwd' that does nothing.
2. Claude Code will create the settings.json file for you, depending on which level 
3. Edit the file and replace the dummy hook with the reminder hook configuration.

## Customization

Edit the `reminders` list in the `reminder.py` file wherever you copied it:

```python
reminders = [
    "🤝 Exercise full agency to push back on mistakes. Flag issues early, ask questions if unsure of direction instead of choosing randomly",
    "🤲 Don't flatter me. Give me honest feedback even if I don't want to hear it",
    # Add your own critical rules here
]
```

### Writing Effective Reminders

**Treat reminder space as extreme premium!**

✅ **DO:**
- Keep reminders short and actionable
- Focus on behaviors that Claude Code frequently forgets
- Highly recommended to limit it to 2-5 critical rules maximum

❌ **DON'T:**
- Add every rule from your CLAUDE.md
- Use long, complex instructions
- Include context-specific rules that don't apply broadly

## Tradeoffs and Cost Considerations

Each reminder:
- Adds a few more tokens to your context
- Costs a small amount in API usage
- May slightly reduce available context for very long conversations

Be aware of the tradeoffs and decide if it is worth it for you for the critical rules.

## Testing Your Setup

### Quick Test
1. Start a new Claude Code conversation
2. Type a simple prompt like "hello"
3. After Claude responds, press `Esc` twice
4. You should see the last reminder it send in the list of previous messages it got.

You can also ask it to tell you what was the last reminder it received, although that is non-deterministic.

### Run Unit Tests
Run from project root:
```bash
./test.sh
```

## Troubleshooting

**Reminders not appearing?**
- Verify the script path in settings.json is absolute or uses `$CLAUDE_PROJECT_DIR`
- Ensure reminder.py has execute permissions: `chmod +x reminder.py`
- Check Claude Code logs for hook execution errors
- Make sure you started the new conversation

## License

MIT License - see [LICENSE](LICENSE) file for details.
