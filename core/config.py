import os
from dotenv import load_dotenv

# Load all environment variables from the .env file
load_dotenv()

# --- Google ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
GOOGLE_SEARCH_API_KEY = os.getenv("GOOGLE_SEARCH_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# --- Twilio ---
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# --- Redis ---
REDIS_URL = os.getenv("REDIS_URL")

# --- Validation (Optional but Recommended) ---
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in .env file")
if not REDIS_URL:
    raise ValueError("REDIS_URL is not set in .env file")

print("Configuration loaded successfully.")