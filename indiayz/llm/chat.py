# indiayz/llm/chat.py

from indiayz.core.base import BaseModule


class Chat(BaseModule):
    """
    Unified chat interface (LLMs).
    """

    name = "llm.chat"

    @staticmethod
    def ask(prompt: str) -> str:
        response = Chat._post("/chat", {"prompt": prompt})
        return response.get("response", "")
