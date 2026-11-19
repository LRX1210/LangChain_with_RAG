from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama.llms import OllamaLLM

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一位诗人，可以作诗"),
        MessagesPlaceholder("history"),  #用来注入数据
        ("human", "好诗请再一个"),
    ]
)

history_date = [
    ("human", "你来写一首古诗"),
    ("ai", "床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗请再一个"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]

model = OllamaLLM(model="qwen3:4b")

#组成链
chain = chat_prompt_template | model

#通过链去调用invoke 或 string
res = chain.invoke({"history": history_date})
print(res)
for chunk in chain.stream({"history": history_date}):
    print(chunk,end="",flush=True)