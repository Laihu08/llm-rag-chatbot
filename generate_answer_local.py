import subprocess
import chromadb
from sentence_transformers import SentenceTransformer

# Load ChromaDB and connect to stored collection
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection("rag_collection")

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Get user question
query = input("\nAsk a question: ")

# Convert query into an embedding
query_embedding = model.encode(query).tolist()

# Perform a similarity search in the vector database
results = collection.query(
    query_embeddings=[query_embedding],  
    n_results=3  # Retrieve top 3 most relevant text snippets
)

# Combine retrieved text
retrieved_text = " ".join([res["text"] for res in results["metadatas"][0]])

# Generate a final answer using Mistral via Ollama
ollama_prompt = f"Context: {retrieved_text}\n\nQuestion: {query}\nAnswer:"

# Call the local model using subprocess
response = subprocess.run(
    ["ollama", "run", "mistral", ollama_prompt],
    capture_output=True,
    text=True
)

# Print the response from Mistral
print("\n🤖 AI Answer (Generated Locally):")
print(response.stdout)
