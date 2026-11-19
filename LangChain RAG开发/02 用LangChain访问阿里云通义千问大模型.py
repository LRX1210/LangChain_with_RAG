from langchain_community.llms.tongyi import Tongyi

#不用qwen3.7-max,因为qwen3.7-max是聊天模型，而qwen-max是大语言模型
model=Tongyi(model="qwen3.8-max")

res=model.invoke(input="你是谁能做什么？")
print(res)
