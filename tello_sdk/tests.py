from contextlib import contextmanager

import pytest

from tello_sdk.commands import TelloSDK, ValidationError, ValueValidator


@contextmanager
def does_not_raise():
    #  https://docs.pytest.org/en/6.2.x/example/parametrize.html#parametrizing-conditional-raising
    yield


@pytest.fixture
def validator():
    validator_instance = ValueValidator()
    return validator_instance


@pytest.fixture
def tello() -> TelloSDK:
    tello_sdk = TelloSDK()
    return tello_sdk


def test_validator_boundries(validator: ValueValidator):
    validator.check_boundries(value=25, minimum=20, maximum=30)
    assert True


def test_validator_options(validator: ValueValidator):
    validator.check_options(value="a", options=["a", "b"])
    assert True


def test_validator_boundries_min_fail(validator: ValueValidator):
    with pytest.raises(ValidationError):
        validator.check_boundries(value=10, minimum=20, maximum=30)


def test_validator_boundries_max_fail(validator: ValueValidator):
    with pytest.raises(ValidationError):
        validator.check_boundries(value=40, minimum=20, maximum=30)


def test_validator_options_fail(validator: ValueValidator):
    with pytest.raises(ValidationError):
        possible_options = ["a", "b", "c"]
        validator.check_options(value="d", options=possible_options)


def test_takeoff(tello: TelloSDK):
    command = tello.takeoff()
    assert command == "takeoff"


def test_land(tello: TelloSDK):
    command = tello.land()
    assert command == "land"


def test_stream_on(tello: TelloSDK):
    command = tello.streamon()
    assert command == "streamon"


def test_stream_off(tello: TelloSDK):
    command = tello.streamoff()
    assert command == "streamoff"


def test_emergency(tello: TelloSDK):
    command = tello.emergency()
    assert command == "emergency"


@pytest.mark.parametrize(
    "value,result",
    [
        (20, "up 20"),
        (500, "up 500"),
    ],
)
def test_up(tello: TelloSDK, value, result):
    command = tello.up(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (20, "down 20"),
        (500, "down 500"),
    ],
)
def test_down(tello: TelloSDK, value, result):
    command = tello.down(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (20, "left 20"),
        (500, "left 500"),
    ],
)
def test_left(tello: TelloSDK, value, result):
    command = tello.left(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (20, "right 20"),
        (500, "right 500"),
    ],
)
def test_right(tello: TelloSDK, value, result):
    command = tello.right(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (20, "forward 20"),
        (500, "forward 500"),
    ],
)
def test_forward(tello: TelloSDK, value, result):
    command = tello.forward(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (20, "back 20"),
        (500, "back 500"),
    ],
)
def test_back(tello: TelloSDK, value, result):
    command = tello.back(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (1, "cw 1"),
        (3600, "cw 3600"),
    ],
)
def test_cw(tello: TelloSDK, value, result):
    command = tello.cw(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        (1, "ccw 1"),
        (3600, "ccw 3600"),
    ],
)
def test_ccw(tello: TelloSDK, value, result):
    command = tello.ccw(value=value)
    assert command == result


@pytest.mark.parametrize(
    "value,result",
    [
        ("l", "flip l"),
        ("r", "flip r"),
        ("f", "flip f"),
        ("b", "flip b"),
    ],
)
def test_flip(tello: TelloSDK, value, result):
    command = tello.flip(value=value)
    assert command == result


@pytest.mark.parametrize(
    "x,y,z,speed,result",
    [
        (20, 20, 20, 10, "go 20 20 20 10"),
        (500, 500, 500, 100, "go 500 500 500 100"),
    ],
)
def test_go(tello: TelloSDK, x, y, z, speed, result):
    command = tello.go(x=x, y=y, z=z, speed=speed)
    assert command == result


def test_stop(tello: TelloSDK):
    command = tello.stop()
    assert command == "stop"


@pytest.mark.parametrize(
    "x1,y1,z1,x2,y2,z2,speed,result",
    [
        (20, 20, 20, 20, 20, 20, 10, "curve 20 20 20 20 20 20 10"),
        (500, 500, 500, 500, 500, 500, 100, "curve 500 500 500 500 500 500 100"),
    ],
)
def test_curve(tello: TelloSDK, x1, y1, z1, x2, y2, z2, speed, result):
    command = tello.curve(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2, speed=speed)
    assert command == result


def test_speed(tello: TelloSDK):
    value = 20
    command = tello.speed(value=value)
    assert command == f"speed {value}"


@pytest.mark.parametrize(
    "a,b,c,d,result",
    [
        (20, 20, 20, 20, "rc 20 20 20 20"),
        (0, 0, 0, 0, "rc 0 0 0 0"),
    ],
)
def test_rc(tello: TelloSDK, a, b, c, d, result):
    command = tello.rc(a=a, b=b, c=c, d=d)
    assert command == result


def test_mon(tello: TelloSDK):
    command = tello.mon()
    assert command == "mon"


def test_moff(tello: TelloSDK):
    command = tello.moff()
    assert command == "moff"


def test_ap(tello: TelloSDK):
    ssid = "ssid"
    password = "password"
    command = tello.ap(ssid=ssid, password=password)
    assert command == f"ap {ssid} {password}"


def test_get_speed(tello: TelloSDK):
    command = tello.get_speed()
    return command == "speed?"


def test_get_time(tello: TelloSDK):
    command = tello.get_time()
    return command == "time?"


def test_get_wifi(tello: TelloSDK):
    command = tello.get_wifi()
    return command == "wifi?"


def test_get_sdk(tello: TelloSDK):
    command = tello.get_sdk()
    return command == "sdk?"


def test_get_sn(tello: TelloSDK):
    command = tello.get_sn()
    return command == "sn?"
