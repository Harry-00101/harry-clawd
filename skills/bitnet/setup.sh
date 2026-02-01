#!/bin/bash
# BitNet Setup for Harry-001

echo "🚀 Setting up BitNet for Harry-001..."
echo ""

# Clone bitnet.cpp
cd /root/clawd
if [ ! -d "bitnet" ]; then
    git clone https://github.com/microsoft/BitNet.git
fi

cd bitnet

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt 2>&1 | tail -5

# Build
echo "🔨 Building bitnet.cpp..."
mkdir -p build
cd build
cmake ..
make -j4

echo ""
echo "✅ BitNet Setup Complete!"
echo ""
echo "Models available:"
echo "- microsoft/BitNet-b1.58-2B-4T (2.4B)"
echo "- HF1BitLLM/Llama3-8B-1.58-100B-tokens (8B)"
echo ""
echo "Run: python run.py --model <model-name>"
