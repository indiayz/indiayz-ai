# indiayz/core/base.py

import requests
from indiayz.core.config import BASE_URL, TIMEOUT


class BaseModule:
    """
    Base class for all indiayz modules.
    Acts as API client.
    """

    name: str = "base"

    @staticmethod
    def _post(endpoint: str, payload: dict, timeout: int = TIMEOUT):
        try:
            r = requests.post(f"{BASE_URL}{endpoint}", json=payload, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException:
            raise RuntimeError("Indiayz backend is unavailable. Please try later.")
