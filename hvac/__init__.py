from typing import Protocol

class HVAC(Protocol):
    def stop_heating(self):
        raise NotImplementedError

    def stop_cooling(self):
        raise NotImplementedError

    def stop_blowing(self):
        raise NotImplementedError


class Controller:
    def __init__(self, hvac: HVAC) -> None:
        hvac.stop_heating()
        hvac.stop_cooling()
        hvac.stop_blowing()
