from enum import Enum


class TelloResponse(Enum):
    OK = "ok"
    ERROR = "error"


class OnOff(Enum):
    ON = "on"
    OFF = "off"
