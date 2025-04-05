from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests
from openai import OpenAI

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the MCP context schema
class MCPContext(BaseModel):
    user_input: str
    model_name: str
    temperature: float = 0.7
    memory: list[str] = []
    system_prompt: str = "You are a helpful assistant."

# Main API route for running agent
@app.post("/api/run")
async def run_agent(request: Request):
    data = await request.json()
    context = MCPContext(**data)

    messages = [{"role": "system", "content": context.system_prompt}]
    if context.memory:
        for m in context.memory:
            messages.append({"role": "user", "content": m})
    messages.append({"role": "user", "content": context.user_input})

    # Route to OpenAI or Ollama
    if context.model_name.startswith("gpt-"):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=context.model_name,
            messages=messages,
            temperature=context.temperature,
        )
        content = response.choices[0].message.content
    else:
        ollama_payload = {
            "model": context.model_name,
            "prompt": context.user_input,
            "stream": False
        }
        res = requests.post("http://localhost:11434/api/generate", json=ollama_payload)
        content = res.json().get("response", "[No response]")

    return { "output": content }
