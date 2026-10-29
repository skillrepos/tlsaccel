#!/usr/bin/env bash
# Re-attach: make sure the Ollama server is running
if ! pgrep -x ollama > /dev/null; then
    (ollama serve > /tmp/ollama.log 2>&1 &)
    sleep 3
fi
echo "Ollama is running."
