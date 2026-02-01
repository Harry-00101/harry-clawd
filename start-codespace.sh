#!/bin/bash
# Start OpenClaw in GitHub Codespace

echo "🚀 Starting OpenClaw Development Environment..."
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pnpm install

# Build
echo "🔨 Building OpenClaw..."
pnpm build

# Start
echo "▶️ Starting OpenClaw..."
pnpm start

echo ""
echo "✅ OpenClaw is running!"
echo "🌐 Open in Codespace terminal to use"
