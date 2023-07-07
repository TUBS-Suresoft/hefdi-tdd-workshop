from hvac import Controller
from hvac import HVAC

class HVACTestDouble(HVAC):
    def __init__(self) -> None:
        self._heating = False
        self._blowing = False
        self._cooling = False

    def is_heating(self) -> bool:
        return self._heating

    def is_cooling(self) -> bool:
        return self._cooling

    def is_blowing(self) -> bool:
        return self._blowing

    def stop_heating(self) -> None:
        self._heating = False

    def stop_cooling(self) -> None:
        self._cooling = False

    def stop_blowing(self) -> None:
        self._blowing = False


def assert_everything_is_off(hvac: HVACTestDouble) -> None:
    assert hvac.is_heating() == False
    assert hvac.is_blowing() == False
    assert hvac.is_cooling() == False

# Given - When - Then
def test_when_starting_system__everything_is_off() -> None:

    # Arrange
    hvac = HVACTestDouble()

    # Act
    sut = Controller(hvac)

    # Assert
    assert_everything_is_off(hvac)
