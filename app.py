from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)


load_dotenv()

# Retrieve Pinecone and OpenAI API keys
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = download_hugging_face_embeddings()


# Initialize Pinecone vector store with an existing index
index_name = "medicalchatbot"

docsearch = Pinecone.from_existing_index(
    index_name = index_name,
    embedding = embeddings
)


# Set up the retriever and Initialize OpenAI's
retriever = docsearch.as_retriever(search_type = "similarity", kwargs= {"k": 3})

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.4 , max_tokens=500)
prompt = ChatPromptTemplate(
    [
        ("system" , system_prompt),
        ("human" , "{input}")
    ]
)


# Create the question-answering chain that combines the model and prompt
question_answer_chain = create_stuff_documents_chain(llm , prompt)
rag_chain = create_retrieval_chain(retriever , question_answer_chain)


# Define the routes to render the chat page
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods = ["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response: ", response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)