from indiayz.core.base import BaseModule


class Chat(BaseModule):
    """
    Unified chat interface (LLMs).
    """

    name = "llm.chat"

    @staticmethod
    def ask(prompt: str) -> str:
        # Placeholder (real LLM backend later)
        return f"[indiayz-chat] {prompt}"
