# indiayz/image/generate.py

from indiayz.core.base import BaseModule


class Image(BaseModule):
    """
    Image generation & processing interface.
    """

    name = "image"

    @staticmethod
    def generate(prompt: str):
        response = Image._post("/image", {"prompt": prompt})
        return response
