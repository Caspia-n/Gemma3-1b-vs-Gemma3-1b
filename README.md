# clankerconv

An experimental AI conversation generator that creates emergent dialogues between two AI personas using Ollama.

## Overview

This project orchestrates a conversation between two AI instances ("Jake" and "Paul"), where each model responds to the other in turn, creating a dynamic and often surprising dialogue. The conversation is saved to a Markdown file for easy reading and sharing.

## Features

- **Dual AI Personas**: Two independent models maintain separate conversation histories
- **Emergent Dialogue**: Models respond to each other organically, creating unexpected narrative threads
- **Persistent Output**: Conversations are saved to `conversation.md` in Markdown format
- **Ollama Integration**: Uses the Ollama API for local model inference

## Requirements

- Python 3.13+
- Ollama running locally on `http://127.0.0.1:11434`
- `gemma3:1b` model installed in Ollama
- `uv` package manager

## Installation

1. Clone this repository
2. Install dependencies with `uv`:

   ```bash
   uv sync
   ```

3. Ensure Ollama is running with the `gemma3:1b` model available
4. Install Python 3.13 if not on system with `uv`:
   ```bash
   uv python install 3.13
   ```

## Usage

Run the conversation generator:

```bash
uv run main.py
```

The script will:

- Initialize two conversation histories (one per model)
- Start with "Hello!" as the opening message
- Have Jake and Paul take turns responding to each other
- Write each exchange to `conversation.md`
- Continue indefinitely until interrupted

## Project Structure

- `main.py` - Main conversation orchestration script
- `conversation.md` - Output file containing the dialogue history
- `pyproject.toml` - Project metadata and dependencies

## Configuration

Edit `main.py` to customize:

- **Model**: Change `"gemma3:1b"` to any available Ollama model
- **Initial message**: Modify the `msg = "Hello!"` line
- **Output file**: Change the `OUTPUT_FILE` variable
- **Ollama host**: Update the client initialization if running on a different address

## Notes

This is an experimental project exploring emergent AI conversation. The quality and coherence of dialogues will vary based on model selection and random factors in generation.
