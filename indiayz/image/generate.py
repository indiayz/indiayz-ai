from indiayz.core.base import BaseModule

class Image(BaseModule):
    @staticmethod
    def generate(prompt: str):
        res = Image._post("/api/image", {"prompt": prompt})
        return res.get("image_url", res)
