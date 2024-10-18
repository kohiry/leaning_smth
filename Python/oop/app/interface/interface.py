from abc import ABCMeta, abstractmethod


class Motor(metaclass=ABCMeta):
    __fuel: int  # encapsulation

    @abstractmethod
    def refill(self, fuel):
        pass
