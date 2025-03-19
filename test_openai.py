import os
import openai

# Load API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("❌ OpenAI API Key not found! Set it in your environment variables.")
    exit()

# OpenAI Client
client = openai.OpenAI()

# Test API with a simple prompt (Change model to "gpt-3.5-turbo")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Change to this model
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    temperature=0.7
)

print("\n✅ OpenAI API Test Successful!")
print("Response:", response.choices[0].message.content)
