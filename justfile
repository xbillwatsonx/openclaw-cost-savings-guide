# OpenClaw Cost Savings Guide public package, version 0.1.0.

# Show all commands
help:
    @just --list

# Open command menu
menu:
    @justx

# Run deterministic package validation
validate:
    python3 validate-package.py

# Build the version 0.1.0 ZIP and checksum beside the repository
release-archive:
    @cd ..; rm -f "openclaw-cost-savings-guide-v0.1.0.zip" "openclaw-cost-savings-guide-v0.1.0.zip.sha256"; zip -rq "openclaw-cost-savings-guide-v0.1.0.zip" "openclaw-cost-savings-guide" -x "openclaw-cost-savings-guide/.git/*"; sha256sum "openclaw-cost-savings-guide-v0.1.0.zip" > "openclaw-cost-savings-guide-v0.1.0.zip.sha256"

# Agent preflight checks
agent-preflight:
    git status
    just --list
    just validate

# Agent verification after edits
agent-verify:
    git status
    git diff --stat
    just validate

# Show current package state
agent-status:
    git status
    git log --oneline -5
