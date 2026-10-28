from langchain.chat_models import init_chat_model
from rich import print

llm = init_chat_model("ollama:qwen3.5:9b")

response = llm.invoke("Hello, how are you?")

print(response)
