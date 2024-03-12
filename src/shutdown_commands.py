import logging
import os

logger = logging.getLogger(__name__)

class ShutdownCommands:
    def __init__(self):
        pass

    def shutdown(self):
        logging.debug("shutdown command recieved.")
        os.system("systemctl poweroff")

    def reboot(self):
        logging.debug("reboot command recieved.")
        os.system("systemctl reboot")
