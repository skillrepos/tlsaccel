#!/usr/bin/env bash
# Install Ollama and pull the lab model (runs once, during Codespace creation)
set -euo pipefail
MODEL="${OLLAMA_MODEL:-llama3.2:3b}"

# The Ollama installer needs zstd to unpack; the base image does not include it
if ! command -v zstd > /dev/null 2>&1; then
    sudo apt-get update -qq && sudo apt-get install -y -qq zstd
fi

curl -fsSL https://ollama.com/install.sh | sh
(ollama serve > /tmp/ollama.log 2>&1 &)

# Wait up to 30 seconds for the server to answer
for i in $(seq 1 30); do
    curl -s http://localhost:11434/api/version > /dev/null && break
    sleep 1
done

ollama pull "$MODEL"
ollama list | grep -q "${MODEL%%:*}" || { echo "Model download failed - see /tmp/ollama.log"; exit 1; }
echo "Ollama ready with model $MODEL"
