# 🧠 ModelOS

Open Source Agent Execution Framework — visual, scriptable, and model-agnostic. Built with:

- 🧰 CLI SDK with MCP schema
- ⚙️ FastAPI backend (OpenAI + Ollama)
- 🔲 Visual workflow builder (React + Tailwind)

## 📦 Structure

```
modelos/
├── modelos-visual-builder/         # Frontend (React + Tailwind)
├── ModelOS_Backend_With_Ollama/    # FastAPI backend with OpenAI & Ollama
├── ModelOS_CLI_Phase1_Complete_With_Logo/  # CLI SDK + MCP Logger
```

## 🚀 Get Started

```bash
git clone https://github.com/yourname/modelos.git
cd modelos/modelos-visual-builder
npm install && npm run dev
```

In a new terminal:

```bash
cd modelos/ModelOS_Backend_With_Ollama
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
uvicorn server:app --reload
```

## 📄 License

MIT
