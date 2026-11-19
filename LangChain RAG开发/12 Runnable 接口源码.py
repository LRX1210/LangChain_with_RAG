from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
prompt = PromptTemplate.from_template("你是一个AI助手")
model = OllamaLLM(model="qwen3:4b")

chain = prompt | model | prompt | model
print(type(chain))