from typing import Protocol


class HVAC(Protocol):
    def stop_heating(self) -> None:
        raise NotImplementedError

    def stop_cooling(self) -> None:
        raise NotImplementedError

    def stop_blowing(self) -> None:
        raise NotImplementedError

    def start_cooling(self) -> None:
        raise NotImplementedError

    def start_blowing(self) -> None:
        raise NotImplementedError

    def start_heating(self) -> None:
        raise NotImplementedError

    def get_temperature(self) -> int:
        raise NotImplementedError


class Controller:
    def __init__(self, hvac: HVAC) -> None:
        self.hvac = hvac
        self.hvac.stop_heating()
        self.hvac.stop_cooling()
        self.hvac.stop_blowing()
        self.desired_temperature = 0
        self.temperature_delta = 0

    def check_temperature(self) -> None:
        self.hvac.start_cooling()
        self.hvac.start_blowing()
        self.hvac.stop_heating()

        its_too_cold = self.hvac.get_temperature() < self.desired_temperature + self.temperature_delta
        if (its_too_cold):
            self.hvac.stop_cooling()
            self.hvac.start_heating()
