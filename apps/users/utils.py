from cryptography.fernet import Fernet
from config.settings import FERNET_KEY
from google import genai

# method to encrypt stuff (password, API key, etc.)
def encrypt(token: bytes) -> bytes:
    f = Fernet(FERNET_KEY)
    return f.encrypt(token)

# method to decrypt stuff (password, API key, etc.)
def decrypt(token: bytes) -> bytes:
    f = Fernet(FERNET_KEY)
    return f.decrypt(token)

# method to validate Gemini API key
def is_valid_gemini_api_key(api_key: str) -> bool:
    