import logging
import os

logger = logging.getLogger(__name__)

class ShutdownCommands:
    def __init__(self):
        pass

    def shutdown(self):
        logging.debug("Shutting down the device.")
        os.system("systemctl poweroff")

    def reboot(self):
        logging.debug("Rebboting the device.")
        os.system("systemctl reboot")
