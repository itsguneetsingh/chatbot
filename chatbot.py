import sys
from langchain.chat_models import ChatOpenAI
from pineconedb import vectorstore, search
from langchain.agents import Tool, load_tools
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.chains import RetrievalQA
import constants
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=constants.OPENAI_API_KEY, temperature=0.0, streaming=True, callbacks=[StreamingStdOutCallbackHandler()])
print('llm ready')

# question-answer retrival chain
retriever = vectorstore.as_retriever()
search = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever
)


tools = [Tool(name = "VectorStore_Search", description = "Search from documents using Pinecone", func = search)]

agent = create_conversational_retrieval_agent(llm, tools, verbose=True, early_stopping_method = "generate")
print('tools ready')

print("Running agent now...")

query = None

while True:
  if not query:
    query = input("Prompt: ")
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  
  result = agent(query)
  print(result['output'])

  query = None