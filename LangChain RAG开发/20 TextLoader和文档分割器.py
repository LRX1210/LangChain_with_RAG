from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("./wj/b.json",encoding="utf-8")
docs = loader.load()
print(docs)
print(len(docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,             #分段每段的最大字符数
    chunk_overlap=50,           #分段每段之间允许重叠的字符数
    #文本自然段落分隔的依据符号
    separators=["\n\n","\n","。","，","！","？",",",".","!","?"],
    length_function=len,     #统计字符的依据函数
)

split_docs = splitter.split_documents(docs)
print(len(split_docs))
for doc in split_docs:
    print(doc)