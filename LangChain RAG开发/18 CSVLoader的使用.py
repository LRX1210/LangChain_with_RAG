from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./wj/asd",
    csv_args={
        "delimiter": ",",    #指定分隔符
        "quotechar": '"',    #指定带有分隔符文本的引号包围是单引号还是双引号
        #如果数据有表头，就不要下面的代码，如果没有就可以使用
        "fieldnames": ['a','s','d']
    },
    encoding="utf-8",
)

# 批量加载  .load()    ->[Document,Document,Document....]
# document = loader.load()
# for document in document:
#     print(type(document),document)

#懒加载   .lazy_load()  迭代器[Document]
for document in loader.lazy_load():
    print(document)
