import requests
from indiayz.core.config import BASE_URL, TIMEOUT

class BaseModule:
    @staticmethod
    def _post(endpoint: str, data: dict):
        headers = {
            "Content-Type": "application/json"
        }

        r = requests.post(
            f"{BASE_URL}{endpoint}",
            json=data,
            headers=headers,
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.json()
