import pinecone
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import constants


def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs


directory = 'data/'

print("Loading documents...")

documents = load_docs(directory)
docs = split_docs(documents)

print("Embedding...")
embed_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
query_result = embed_model.embed_query("Problem With iPhone")
print(len(query_result))


# using pinecone for Vector DB Indexing

print("Pinecone setup")
pinecone.init(
    api_key= constants.PINECONE_API_KEY,
    environment= constants.PINECONE_ENVIRONMENT
)

print("Creating index")
# to create a new index
index = Pinecone.from_documents(docs, embed_model, index_name=constants.PINECONE_INDEX_NAME)

# in order to add more text this should be used

# index = pinecone.Index(constants.PINECONE_INDEX_NAME)
# vectorstore = Pinecone(index, embed_model.embed_query, "text")

# vectorstore.add_texts(Docs)