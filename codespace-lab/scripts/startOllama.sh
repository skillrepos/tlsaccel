#!/usr/bin/env bash
# Make sure the Ollama server is running (runs each time you reconnect)
if ! command -v ollama > /dev/null 2>&1; then
    echo "Ollama is not installed yet. Run: bash codespace-lab/scripts/startup_ollama.sh"
    exit 1
fi
if ! pgrep -x ollama > /dev/null; then
    (ollama serve > /tmp/ollama.log 2>&1 &)
fi
for i in $(seq 1 15); do
    if curl -s http://localhost:11434/api/version > /dev/null; then
        echo "Ollama is running."
        exit 0
    fi
    sleep 1
done
echo "Ollama did not start - see /tmp/ollama.log"
exit 1
