import os

# Define the file path
file_path = "data/sample.txt"

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("File Loaded Successfully! 🎉\n")
        print(content)
else:
    print("File not found! ❌")
