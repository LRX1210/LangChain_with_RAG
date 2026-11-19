from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_ollama.chat_models import ChatOllama

#创建所需的解析器
str_output_parser = StrOutputParser()        #把ai的回答解析成字符串
json_output_parser = JsonOutputParser()      #把ai的回答解析成字典

#创建模型
model = ChatOllama(model="qwen3:4b")

# 第一个提示词模板
fist_prompt = PromptTemplate.from_template(
    "我的邻姓{age},刚生了{gender},你帮我取一个名字,仅告知我名字，不要额外信息."
)

# 第二个提示词模板
second_prompt = PromptTemplate.from_template(
    "姓名:{name}，请帮我解析含义。"
)

#函数的入参：AImessage ->返回值
my_func = RunnableLambda(lambda  ai_msg: {"name":ai_msg.content})
#匿名函数              AImessage             AI的回答

chain = fist_prompt | model | my_func | second_prompt | model | str_output_parser

for chunk in chain.stream(input = {"age":"林","gender":"女孩"}):
    print(
        chunk,
        end = "",
        flush = True
    )