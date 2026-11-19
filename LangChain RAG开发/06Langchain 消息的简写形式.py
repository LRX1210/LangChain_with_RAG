from langchain_community.chat_models.tongyi import ChatTongyi
#（ollama）from langchain_ollama import ChatOllama

from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
#老样子，获得模型对象
model = ChatTongyi(
    model = "qwen3.7-max"
)
#（ollama）model = ChatOllama(model = "qwen3:4b")

message = [
    ("system","你是一个边塞诗人，话不多"),   #角色定位
    ("human","写一首唐诗"),    #用户提问
    ("ai","举头望明月，低头思故乡"),#AI模型回答
    ("human","按照你上一个回复的格式，再写一首唐诗")
]

res = model.stream(input=message)

for chunk in res:
    print(chunk.content,end=" ",flush=True)