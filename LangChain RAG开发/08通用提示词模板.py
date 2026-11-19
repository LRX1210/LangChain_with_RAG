#from langchain_classic.chains.question_answering.map_reduce_prompt import messages
from langchain_core.prompts import PromptTemplate

from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")  #qwen-max是专门用来回答

prompt_template = PromptTemplate.from_template(
    "我的邻姓{age},刚生了{gender},你帮我取一个名字,简单回答."
)

#调用.format方法注入信息即可
# prompt_text = prompt_template.format(age="蔡",gender="女孩")
# print(prompt_text)
#
# res=model.invoke(input=prompt_text)
# print(res)
chain = prompt_template | model      #链条
res = chain.invoke(input={"age":"蔡","gender":"女孩"})
print(res)