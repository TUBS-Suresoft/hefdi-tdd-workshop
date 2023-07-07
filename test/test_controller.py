from hvac import Controller
from hvac import HVAC

class HVACTestDouble(HVAC):
    def __init__(self) -> None:
        self._heating = False
        self._blowing = False
        self._cooling = False
        self.temperature = 0

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

    def start_cooling(self) -> None:
        self._cooling = True

    def start_blowing(self) -> None:
        self._blowing = True


    def start_heating(self) -> None:
        self._heating = True

    def get_temperature(self) -> int:
        return self.temperature



def assert_everything_is_off(hvac: HVACTestDouble) -> None:
    assert hvac.is_heating() == False
    assert hvac.is_blowing() == False
    assert hvac.is_cooling() == False

def assert_is_cooling(hvac: HVACTestDouble) -> None:
    assert hvac.is_heating() == False
    assert hvac.is_blowing() == True
    assert hvac.is_cooling() == True

# Given - When - Then
def test_when_starting_system__everything_is_off() -> None:

    # Arrange
    hvac = HVACTestDouble()

    # Act
    sut = Controller(hvac)

    # Assert
    assert_everything_is_off(hvac)


def test_when_its_too_hot__it_is_start_cooling() -> None:
    # Arrange
    hvac = HVACTestDouble()
    sut = Controller(hvac)

    # Act
    sut.check_temperature()

    # Assert
    assert_is_cooling(hvac)


def test_when_its_too_cold__it_is_start_heating() -> None:
    # Arrange
    hvac = HVACTestDouble()
    sut = Controller(hvac)

    hvac.temperature = 17
    sut.desired_temperature = 20
    sut.temperature_delta = 2

    # Act
    sut.check_temperature()

    # Assert
    assert hvac.is_heating() == True
    assert hvac.is_blowing() == True
    assert hvac.is_cooling() == False