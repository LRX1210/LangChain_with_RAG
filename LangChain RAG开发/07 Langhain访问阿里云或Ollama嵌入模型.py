from langchain_community.embeddings import DashScopeEmbeddings
#(ollama)from langchain_ollama import OllamaEmbeddings

#不传model，默认用的是 text-embeddings-v1
model = DashScopeEmbeddings()
#model = OllamaEmbeddings("model="qwen3-embeddings")

#embed_query(单次转化),embed_documents(批量转化)
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你","咕咕嘎嘎","我的刀盾"]))