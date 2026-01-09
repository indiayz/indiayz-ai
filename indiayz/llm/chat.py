from indiayz.core.base import BaseModule

class Chat(BaseModule):
    @staticmethod
    def ask(prompt: str):
        res = Chat._post("/api/chat", {"prompt": prompt})
        return res.get("reply", "")
