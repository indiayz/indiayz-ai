from indiayz.core.base import BaseModule


class Voice(BaseModule):
    """
    Audio & voice interface.
    """

    name = "audio.voice"

    @staticmethod
    def tts(text: str):
        # Placeholder
        print(f"[indiayz-voice] Speaking: {text}")
