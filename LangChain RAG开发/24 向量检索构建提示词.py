from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.chat_models import ChatOllama
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model="qwen")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}"),
        ("user","用户问题:{input}")
    ]
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v2"),
)

#准备一下资料（向量库的数据）
# add_text传入一个 list[str]
vector_store.add_texts(["坤会篮球","坤会唱","坤会跳","坤会rap","坤会鸡你太美"])
input_text = "坤会干嘛?"

#检索向量库
result = vector_store.similarity_search(input_text,3)
referens_text = "["
for doc in result:
    referens_text+=doc.page_content
referens_text+="]"

def print_prompt(prompt):
    print(prompt.to_string())
    print("-"*20)
    return prompt

chain = prompt | print_prompt | model | StrOutputParser()

res = chain.invoke({"input": input_text,"context": referens_text})
print(res)