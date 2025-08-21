#!/bin/bash
set -e

echo "Running tests..."

cd "$(dirname "$0")"

./claude/hooks/reminder/test_reminder.py

