from abc import ABCMeta, abstractmethod


class BaseTransport(metaclass=ABCMeta):
    mark: str
    model: str
    year_created: int
    speed: int

    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def stop(self):
        pass
