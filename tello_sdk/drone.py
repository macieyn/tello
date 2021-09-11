from enum import Enum
from . import commands
from .enums import TelloResponse, OnOff
from .objects import Point3D, WifiConfig


class Commander:

    def takeoff(self) -> TelloResponse:
        pass

    def land(self) -> TelloResponse:
        pass

    def set_stream_status(self, status: OnOff) -> TelloResponse:
        pass

    def is_streaming(self) -> bool:
        pass

    def stop_motors_immediatly(self) -> TelloResponse:
        pass

    def move_up(self, value: int) -> TelloResponse:
        pass

    def move_down(self, value: int) -> TelloResponse:
        pass

    def move_left(self, value: int) -> TelloResponse:
        pass

    def move_right(self, value: int) -> TelloResponse:
        pass

    def move_forward(self, value: int) -> TelloResponse:
        pass

    def move_backward(self, value: int) -> TelloResponse:
        pass

    def rotate_clockwise(self, value: int) -> TelloResponse:
        pass

    def rotate_counter_clockwise(self, value: int) -> TelloResponse:
        pass

    def flip_to_left(self) -> TelloResponse:
        pass

    def flip_to_right(self) -> TelloResponse:
        pass

    def flip_forward(self) -> TelloResponse:
        pass

    def flip_backward(self) -> TelloResponse:
        pass

    def go_to_point_at_speed(self, point: Point3D, speed: int) -> TelloResponse:
        pass

    def stop(self) -> TelloResponse:
        pass

    def hoover_in_place(self) -> TelloResponse:
        self.stop()

    def move_from_point_to_point_in_curve_movement_at_speed(self, starting_point: Point3D, target_point: Point3D, speed: int):
        pass

    def jump_to_mission_pad(self) -> TelloResponse:
        """
        Not going to implement this as I don't use Mission Pads
        """
        raise NotImplementedError

    def set_speed(self, value: int) -> TelloResponse:
        pass

    def set_remote_controller_control(self, x: int, y: int, z: int, yaw: int) -> TelloResponse:
        pass

    def set_wifi_password(self, wifi: WifiConfig) -> TelloResponse:
        pass

    def enable_mission_pad_detection(self):
        """
        Not going to implement that.
        """
        raise NotImplementedError

    def disable_mission_pad_detection(self) -> TelloResponse:
        pass

    def set_mission_pad_detection_direction(self) -> TelloResponse:
        raise NotImplementedError

    def set_access_point(self, access_point: WifiConfig):
        pass

    def get_current_speed(self) -> int:
        pass

    def get_battery_level(self) -> int:
        pass

    def get_time_of_current_flight(self) -> int:
        pass

    def get_wifi_signal(self) -> str:
        pass

    def get_sdk_version(self) -> str:
        pass

    def get_serial_number(self) -> str:
        pass
