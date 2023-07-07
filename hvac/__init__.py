from typing import Protocol


class HVAC(Protocol):
    def stop_heating(self) -> None:
        raise NotImplementedError

    def stop_cooling(self) -> None:
        raise NotImplementedError

    def stop_blowing(self) -> None:
        raise NotImplementedError


class Controller:
    def __init__(self, hvac: HVAC) -> None:
        hvac.stop_heating()
        hvac.stop_cooling()
        hvac.stop_blowing()
