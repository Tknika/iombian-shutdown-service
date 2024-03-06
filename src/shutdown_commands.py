import os


class ShutdownCommands:
    def __init__(self):
        pass

    def shutdown(self):
        os.system("systemctl poweroff")

    def reboot(self):
        os.system("systemctl reboot")
