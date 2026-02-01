FROM mcr.microsoft.com/devcontainers/javascript-node:20

# Install additional tools
RUN apt-get update && apt-get install -y \
  git \
  curl \
  wget \
  && rm -rf /var/lib/apt/lists/*

# Install Node.js tools globally
RUN npm install -g \
  pnpm \
  typescript \
  ts-node \
  @types/node

WORKDIR /workspaces/openclaw-test
