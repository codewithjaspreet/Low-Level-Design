from command_interface import Command
from reciever import Light



class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_on()

    def undo(self) -> None:
        self._light.turn_off()



class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_off()

    def undo(self) -> None:
        self._light.turn_on()
