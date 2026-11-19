from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="./wj/b.json",     #文件路径
    mode="page",                 #默认是page模式，每个页面形成一个Document文档对象,
                                 # single模式，不管有多少页面，只形成一个Document文档对象
    password="itheima"           #如果文档有密码，就输入
)