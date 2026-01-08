class Settings:
    """
    Global configuration holder.
    """

    def __init__(
        self,
        device: str = "cpu",
        verbose: bool = False,
    ):
        self.device = device
        self.verbose = verbose

    def as_dict(self) -> dict:
        return {
            "device": self.device,
            "verbose": self.verbose,
        }
