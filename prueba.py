import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

# Use the variables in your application
print(f"API Key: {api_key}")
print(f"API Secret: {api_secret}")


