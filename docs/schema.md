# 📐 MCP Schema

**MCP = Model Context Protocol**  
A structured format for passing context to agents.

```json
{
  "user_input": "Tell me a joke.",
  "model_name": "gpt-4",
  "temperature": 0.7,
  "memory": ["Last time we discussed philosophy"],
  "system_prompt": "You are a funny assistant."
}
```

## 🧠 Why MCP?

- Standardize prompt logging
- Interoperable across tools
- Enables versioning, eval, and feedback
---
← **[Visual Builder](./visual-builder.md)**   |   **[Contribute](./contribute.md)** →