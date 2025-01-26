from src.helper import text_split, load_pdf_file, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv


# Load the PDF data from the "data/" directory
extracted_data = load_pdf_file("data/")

# Split the extracted data into smaller chunks
text_chunks = text_split(extracted_data)

# Download the embeddings for the text chunks
embeddings = download_hugging_face_embeddings()

load_dotenv()


# Retrieve API keys securely from environment variables
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")



# Initialize Pinecone with the API key
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalchatbot"

# Create a new Pinecone index with specific settings
pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)


# Create a Pinecone vector store for document retrieval using embeddings
docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding = embeddings,
)