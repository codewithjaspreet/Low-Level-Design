from reciever import Light
from concrete_command import LightOnCommand, LightOffCommand
from invoker import RemoteControl

def main() -> None:
    light = Light()

    on_command = LightOnCommand(light)
    off_command = LightOffCommand(light)

    remote = RemoteControl()
    remote.set_commands([on_command, off_command])

    # Press ON (index 0)
    remote.press_button(0)

    # Press OFF (index 1)
    remote.press_button(1)

    # Undo OFF
    remote.press_undo(1)

    # Undo ON
    remote.press_undo(0)


if __name__ == "__main__":
    main()
