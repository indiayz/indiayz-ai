import os

BASE_URL = os.getenv("INDIAYZ_BASE_URL", "https://indiayz-aebd81835b83.herokuapp.com")
TIMEOUT = int(os.getenv("INDIAYZ_TIMEOUT", "60"))
