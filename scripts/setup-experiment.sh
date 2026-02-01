#!/bin/bash
# Setup Experiment Environment in Codespace

echo "=== Setting up Experiment Environment ==="

# Create experiment directory
mkdir -p /root/clawd/experiments
cd /root/clawd/experiments

# Clone OpenClaw (or create a test version)
echo "Cloning test environment..."
if [ -d "test-openclaw" ]; then
  echo "Test environment exists"
else
  echo "Creating test environment structure..."
  mkdir -p test-openclaw/{skills,scripts,notes}
fi

# Create experiment log
echo "=== $(date) ===" >> /root/clawd/experiments/experiment-log.md
echo "Experiment started: Test instance" >> /root/clawd/experiments/experiment-log.md
echo "" >> /root/clawd/experiments/experiment-log.md

echo "✓ Experiment environment: READY"
echo "Location: /root/clawd/experiments/"
