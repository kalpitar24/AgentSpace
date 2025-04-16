from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import VertexAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatVertexAI

loader = PyPDFLoader("your_docs/product_guide.pdf")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

embedding_model = VertexAIEmbeddings()
db = FAISS.from_documents(chunks, embedding_model)

llm = ChatVertexAI()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

if __name__ == "__main__":
    question = "What is the refund policy?"
    print("Q:", question)
    print("A:", qa.run(question))
