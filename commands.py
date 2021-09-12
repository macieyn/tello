from abc import abstractmethod
from typing import Optional, Protocol


class AbstractCommand(Protocol):

    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def _validate(self):
        raise NotImplementedError


class BaseCommand(AbstractCommand):

    command: str

    def __init__(self, command: Optional[str], **kwargs):
        if command:
            self.command: str = command
        for k, v in kwargs.items():
            setattr(self, k, v)
        
    def execute(self):
        pass