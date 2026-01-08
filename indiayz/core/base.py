class BaseModule:
    """
    Base class for all indiayz modules.
    Every domain module should inherit this.
    """

    name: str = "base"

    def __init__(self, **kwargs):
        self.config = kwargs

    def info(self) -> dict:
        return {
            "module": self.name,
            "config": self.config,
        }
