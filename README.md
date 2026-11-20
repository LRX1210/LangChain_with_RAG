基于LangChain框架开发RAG检索增强生成系统，加载并解析本地私有文档，经过文本切分、向量化、向量库存储；用户提问时检索相关片段作为上下文交给大模型，约束模型回答依据，有效减少幻觉，精准实现私有知识库问答。
 
Develop a RAG system with LangChain. It loads private documents, splits and embeds texts into vector database. Relevant context is retrieved for LLM, mitigating hallucinations and supporting knowledge-base Q&A.
