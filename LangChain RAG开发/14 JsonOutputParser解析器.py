from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama

#创建所需的解析器
str_output_parser = StrOutputParser()        #把ai的回答解析成字符串
json_output_parser = JsonOutputParser()      #把ai的回答解析成字典

#创建模型
model = ChatOllama(model="qwen3:4b")

# 第一个提示词模板
fist_prompt = PromptTemplate.from_template(
    "我的邻姓{age},刚生了{gender},你帮我取一个名字,并封装为JSON格式返回给我。"
    "要求key是name,value就是你起的名字,请严格遵守格式要求"
)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名:{name}，请帮我解析含义。"
)

#构建链
chain = fist_prompt |  model | json_output_parser | second_prompt | model | str_output_parser
res = chain.stream(input={"age":"张","gender":"女孩"})
for chunk in res:
    print(chunk,end="",flush=True)