from app.car import Car
from app.plane import Plane
from app.base import BaseTransport


#  polymorphism
def set_up(transports: list[BaseTransport]):
    for transport in transports:
        transport.set_up()


#  polymorphism
def stop(transports: list[BaseTransport]):
    for transport in transports:
        transport.stop()


def app():
    transports = [
        Car(
            mark="Zxc cars",
            model="Zxc model 2.0",
            year_created=2023,
            speed=40,
            doors=69,
        ),
        Car(
            mark="Zxc cars",
            model="Zxc model 3.0",
            year_created=2024,
            speed=60,
            doors=2,
        ),
        Plane(
            mark="Zxc cars",
            model="Zxc model 34.0",
            year_created=2024,
            speed=160,
            max_height=2,
        ),
    ]
    set_up(transports)
    stop(transports)


if __name__ == "__main__":
    app()
