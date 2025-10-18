from cryptography.fernet import Fernet
from config.settings import FERNET_KEY

# method to encrypt stuff (password, API key, etc.)
def encrypt(token: bytes) -> bytes:
    f = Fernet(FERNET_KEY)
    return f.encrypt(token)

# method to decrypt stuff (password, API key, etc.)
def decrypt(token: bytes) -> bytes:
    f = Fernet(FERNET_KEY)
    return f.decrypt(token)