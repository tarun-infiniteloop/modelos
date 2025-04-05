from pydantic import BaseModel
from typing import List, Optional

class MCPContext(BaseModel):
    user_input: str
    system_prompt: Optional[str] = "You are a helpful AI assistant."
    model_name: str = "gpt-4"
    temperature: float = 0.7
    memory: Optional[List[str]] = []
    tools_used: Optional[List[str]] = []
    output: Optional[str] = None
