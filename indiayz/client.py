import requests
from typing import Any, Dict, Optional


class IndiayzClientError(Exception):
    """Base exception for indiayz client errors."""


class IndiayzAPIError(IndiayzClientError):
    """Raised when the API returns an error response."""


class IndiayzClient:
    """
    Internal HTTP client for communicating with indiayz hosted APIs.
    """

    def __init__(
        self,
        base_url: str = "https://api.indiayz.com",
        timeout: int = 15,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"

        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            raise IndiayzAPIError(f"Request failed: {exc}") from exc

        try:
            data = response.json()
        except ValueError as exc:
            raise IndiayzAPIError("Invalid JSON response from API") from exc

        if not isinstance(data, dict):
            raise IndiayzAPIError("Unexpected API response format")

        return data


# Shared singleton client (simple & efficient)
_client = IndiayzClient()


def _get(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return _client.get(path, params)
