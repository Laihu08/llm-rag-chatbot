import os
from sentence_transformers import SentenceTransformer

# Define file path
file_path = "data/sample.txt"

# Load the text file
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("File Loaded Successfully! 🎉")
else:
    print("File not found! ❌")
    exit()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # A lightweight, efficient model

# Convert text into embeddings
embedding = model.encode(content)

# Print embedding shape and sample values
print("\nEmbedding Generated Successfully! 🚀")
print(f"Embedding Shape: {embedding.shape}")
print(f"Sample Values: {embedding[:5]}")  # Print first 5 values of the embedding
