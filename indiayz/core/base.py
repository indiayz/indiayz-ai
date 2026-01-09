import os
import requests
from indiayz.core.config import BASE_URL, TIMEOUT

API_KEY = os.getenv("API_KEY")   # 👈 यहाँ हार्डकोड नहीं

class BaseModule:
    @staticmethod
    def _post(endpoint: str, data: dict):
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": API_KEY
        }
        r = requests.post(
            f"{BASE_URL}{endpoint}",
            json=data,
            headers=headers,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()
