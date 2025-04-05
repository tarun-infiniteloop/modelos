# 🧠 ModelOS Documentation

Welcome to the **ModelOS** documentation site.

## 🔍 What is ModelOS?

ModelOS is an open agent execution framework with visual workflow builder, CLI SDK, and backend model orchestration (OpenAI, Ollama, etc.).

---

## 🧰 CLI SDK (modelos-cli)

- Log prompts and completions to MCP schema
- Run workflows from terminal
- Integrates with your own models or APIs

---

## 🧠 Visual Builder

- Drag-and-drop blocks
- Connect input, memory, model, output
- Add advanced nodes like Tool, Eval, ToolEval, EvalEval

### Available Blocks

| Type       | Description |
|------------|-------------|
| Input      | User text input |
| Memory     | Prior memory/context |
| Model      | AI model (OpenAI, Mistral, etc.) |
| Output     | Final model response |
| Tool       | External tool/integration |
| Eval       | Evaluation logic |
| EvalEval   | Self-check evaluation |
| ToolEval   | Tool usage analysis |

---

## 📄 MCP JSON Format

```json
{
  "user_input": "your question",
  "model_name": "gpt-4",
  "temperature": 0.7,
  "memory": ["prior message"]
}
```

---

## 🚀 Quickstart

```bash
# Frontend
cd modelos-visual-builder
npm install && npm run dev

# Backend
cd ModelOS_Backend_With_Ollama
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
uvicorn server:app --reload
```

---
Made with ❤️ by Tarun
