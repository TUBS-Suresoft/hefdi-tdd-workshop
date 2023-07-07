from hvac import Controller
from hvac import HVAC

class HVACTestDouble(HVAC):
    def __init__(self):
        self._heating = False
        self._blowing = False
        self._cooling = False

    def is_heating(self) -> bool:
        return self._heating

    def is_cooling(self) -> bool:
        return self._cooling

    def is_blowing(self) -> bool:
        return self._blowing

    def stop_heating(self):
        self._heating = False

    def stop_cooling(self):
        self._cooling = False

    def stop_blowing(self):
        self._blowing = False


def assert_everything_is_off(hvac: HVACTestDouble):
    assert hvac.is_heating() == False
    assert hvac.is_blowing() == False
    assert hvac.is_cooling() == False

# Given - When - Then
def test_when_starting_system__everything_is_off():

    # Arrange
    hvac = HVACTestDouble()

    # Act
    sut = Controller(hvac)

    # Assert
    assert_everything_is_off(hvac)
