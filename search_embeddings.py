import chromadb
from sentence_transformers import SentenceTransformer

# Load ChromaDB and connect to the stored collection
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection("rag_collection")

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Get user query
query = input("\nAsk a question: ")

# Convert query into an embedding
query_embedding = model.encode(query).tolist()

# Perform a similarity search in the vector database
results = collection.query(
    query_embeddings=[query_embedding],  
    n_results=3  # Retrieve top 3 most relevant text snippets
)

# Display results
print("\n🔍 Search Results:")
for i, result in enumerate(results["metadatas"][0]):
    print(f"{i+1}. {result['text']}")

