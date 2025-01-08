# 导入LangChain的库
from langchain import *

# 加载数据源
loader = WebBaseLoader()
doc = loader.load("https://xxx.html")

# 分割文档对象
splitter = RecursiveCharacterTextSplitter(max_length=512)
docs = splitter.split(doc)

# 转换文档对象为嵌入，并存储到向量存储器中
embedder = OpenAIEmbeddings()
vector_store = ChromaVectorStore()
for doc in docs:
    embedding = embedder.embed(doc.page_content)
    vector_store.add(embedding, doc)

# 创建检索器
retriever = VectorStoreRetriever(vector_store, embedder)

# 创建聊天模型
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# 创建一个问答应用
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 启动应用
rag_chain.invoke("What is main purpose of xxx.html?")
