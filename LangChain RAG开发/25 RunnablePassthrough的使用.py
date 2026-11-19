from re import search

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda
from langchain_ollama.chat_models import ChatOllama
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate



#                          报错，环境冲突





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

#langchain中向量存储对象，有一个方法：as_retriever,可以返回一个Runnable接口的子类实例对象
retriever = vector_store.as_retriever(search_kwargs={"k":2})

def format_func(docs:list[Document]):
    if not docs:
        return "无参考资料"
    formatted_str = "["
    for doc in docs:
        formatted_str+=doc.page_content
    formatted_str+="]"
    return formatted_str
def print_prompt(prompt):
    print(prompt.to_string())
    print("-"*20)
    return prompt

chain = (
    {"input":RunnablePassthrough(),"context": retriever | format_func} | prompt | RunnableLambda(print_prompt) | model | StrOutputParser()
)

res = chain.invoke(input_text)
print(res)