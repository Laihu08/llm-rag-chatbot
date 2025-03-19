import os
import chromadb
from sentence_transformers import SentenceTransformer

# Define file path
file_path = "data/sample.txt"

# Load the text file
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().split(". ")  # Split text into sentences for better search
        print("File Loaded Successfully! 🎉")
else:
    print("File not found! ❌")
    exit()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert text into embeddings
embeddings = model.encode(content)

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")  # Stores data persistently
collection = chroma_client.get_or_create_collection("rag_collection")

# Store each sentence and its embedding in the database
for i, sentence in enumerate(content):
    collection.add(
        ids=[str(i)],  # Unique ID for each entry
        embeddings=[embeddings[i].tolist()],  # Convert to list
        metadatas=[{"text": sentence}],  # Store original text
    )

print("\nEmbeddings Stored Successfully in ChromaDB! 🚀")
print(f"Total Sentences Stored: {len(content)}")
