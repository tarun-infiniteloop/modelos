# ModelOS CLI (Phase 1)

![License](https://img.shields.io/github/license/yourusername/modelos-cli)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)

ModelOS CLI is the first component of the open-source ModelOS platform. It allows you to interact with LLMs using structured, standardized contexts via the Model Context Protocol (MCP).

## Features
- Run prompts through OpenAI's GPT models
- Log all interactions in MCP format
- Transcribe voice input via Whisper (if installed)

## Getting Started
```bash
# Clone and install dependencies
pip install typer openai pydantic

# Set your OpenAI key
export OPENAI_API_KEY=your_openai_key

# Run CLI
python modelos_core/cli.py run --prompt "What is quantum computing?"

# Or run with audio input
python modelos_core/cli.py run --audio example.wav
```

## Coming Soon
- Ollama integration (local Mistral, DeepSeek)
- Agent memory context
- Model comparison and benchmarking
- Visual workflow tool (Phase 2)

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Logo + Branding
ModelOS will include a minimalist, modular-themed logo and visual kit. Coming soon in Phase 2.
