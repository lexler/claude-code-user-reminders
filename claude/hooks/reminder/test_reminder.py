#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["pytest"]
# ///

import subprocess
import os
import sys
import pytest
sys.path.insert(0, os.path.dirname(__file__))
from reminder import reminders

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "reminder.py")

def test_output_format():
    result = subprocess.run([SCRIPT_PATH], capture_output=True, text=True)
    
    output = result.stdout.strip()
    assert output.startswith("<reminder>"), f"Should start with '<reminder>', got: {output}"
    assert output.endswith("]"), f"Should end with ']', got: {output}"

def test_exit_code_zero():
    result = subprocess.run([SCRIPT_PATH], capture_output=True, text=True)
    assert result.returncode == 0, f"Should exit with 0, got {result.returncode}"

def test_outputs_to_stdout_not_stderr():
    result = subprocess.run([SCRIPT_PATH], capture_output=True, text=True)
    assert result.stderr == "", f"stderr should be empty, got: {result.stderr}"
    assert result.stdout != "", "stdout should have content"

def test_reminder_from_list():
    result = subprocess.run([SCRIPT_PATH], capture_output=True, text=True)
    output = result.stdout.strip()
    start = output.find("<reminder>") + len("<reminder>")
    end = output.find("</reminder>")
    reminder_text = output[start:end]
    assert reminder_text in reminders, f"Reminder '{reminder_text}' not in reminders list"

def test_randomness():
    if len(reminders) <= 1:
        return
    
    seen_reminders = set()
    for _ in range(10):
        result = subprocess.run([SCRIPT_PATH], capture_output=True, text=True)
        output = result.stdout.strip()
        start = output.find("<reminder>") + len("<reminder>")
        end = output.find("</reminder>")
        reminder_text = output[start:end]
        seen_reminders.add(reminder_text)
    
    assert len(seen_reminders) >= 2, f"Expected variety in {len(reminders)} reminders, saw only {len(seen_reminders)}"

if __name__ == "__main__":
    pytest.main([__file__, "-xvs"])