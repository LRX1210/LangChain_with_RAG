from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path="./wj/c.json",     # 文件路径
    jq_schema=".name",            # jp schema语法 类似查看
    text_content=False,      # 抽取的是否是字符串,默认True
    json_lines=True,          # 是否是Jsonlines文件,(每一行都是一个独立的标准JSON)
)

document = loader.load()
print(document)