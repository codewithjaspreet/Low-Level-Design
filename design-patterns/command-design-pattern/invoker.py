from typing import List, Optional
from command_interface import Command


class RemoteControl:
    def __init__(self) -> None:
        self.commands: List[Optional[Command]] = []
        self.executed: List[bool] = []

    def set_commands(self, commands: List[Command]) -> None:
        self.commands = commands
        self.executed = [False] * len(commands)

    def press_button(self, button_index: int) -> None:
        if 0 <= button_index < len(self.commands):
            command = self.commands[button_index]
            if command:
                command.execute()
                self.executed[button_index] = True

    def press_undo(self, button_index: int) -> None:
        if 0 <= button_index < len(self.commands):
            if self.executed[button_index]:
                command = self.commands[button_index]
                if command:
                    command.undo()
                    self.executed[button_index] = False
