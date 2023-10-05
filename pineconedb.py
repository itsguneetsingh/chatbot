from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import constants
import pinecone

print("Pinecone setup started")
pinecone.init(
    api_key= constants.PINECONE_API_KEY,
    environment= constants.PINECONE_ENVIRONMENT
)
print("Pinecone setup completed")

print("Creating index")
index = pinecone.Index(constants.PINECONE_INDEX_NAME)
print("Index: \n")
print(index.describe_index_stats())

print("creating vectorstore")
embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Pinecone(index, embed_model, "text")

print("Pinccone setup completed")

def search(query):
    query_vector = embed_model.encode(query)
    
    results = index.query(query_vector, top_k=5)
    
    return [result.id for result in results]