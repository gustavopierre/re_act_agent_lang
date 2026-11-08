# Copyright (c) 2025

from langchain.chat_models import init_chat_model
from rich import print

# llm = init_chat_model("ollama:qwen3.5:9b")
llm = init_chat_model("google_genai:gemma-4-31b-it")

response = llm.invoke("Hello, how are you?")

print(response)
