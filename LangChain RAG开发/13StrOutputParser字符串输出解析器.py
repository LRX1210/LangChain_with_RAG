from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM
model = OllamaLLM(model="qwen3:4b")
prompt = PromptTemplate.from_template(
    "我的邻姓{age},刚生了{gender},你帮我取一个名字,简单回答."
)
parser = StrOutputParser()  #把ai的回答解析成字符串，使其可以重新放入ai里进行回答

chain = prompt | model | parser | model | parser
res = chain.invoke(input={"age":"张","gender":"女孩"})
print(res)