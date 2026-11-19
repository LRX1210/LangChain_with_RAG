from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

sin = model.stream(input="你是谁")         #将invoke改为stream即可变为流式

for chunk in sin:
    print(chunk,end=" ",flush=True)