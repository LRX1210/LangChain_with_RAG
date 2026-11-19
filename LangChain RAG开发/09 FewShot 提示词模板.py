from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi
from langchain_ollama.llms import OllamaLLM

#示例数据的模板
example_prompt = PromptTemplate.from_template("单词:{word},反义词:{antonym}")
#示例的动态数据注入
examples_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]

#框架
few_shot_template = FewShotPromptTemplate(
    example_prompt = example_prompt,                                    #示例数据的模板
    examples = examples_data,                                           #示例的数据(用来注入动态数据的)，list内套字典
    prefix="告知我单词的反义词，我提供如下数据",                             #示例之前的提示词
    suffix="基于前面的示例，告知我，{input_word}的反义词是？",               #示例之后的提示词
    input_variables=['input_word']                                     #声明前缀或后缀中说需要的变量名
)

prompt_text= few_shot_template.invoke(input={"input_word":"左"}).to_string()   #to_string()转译成字符串
#prompt_qw = few_shot_template.format(input_q="左").strip()

print(prompt_text)

# model = Tongyi(model = "qwen-max")
model = OllamaLLM(model = "qwen3:4b")

print(model.invoke(input=prompt_text))