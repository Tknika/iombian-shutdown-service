#!/usr/bin/env python3

import logging
import os
import signal

from communication_server import CommunicationServer
from shutdown_commands import ShutdownCommands

LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
SHUTDOWN_PORT = int(os.environ.get("SHUTDOWN_PORT", 5558))

SHUTDOWN_HOST = "0.0.0.0"

logging.basicConfig(format="%(asctime)s %(levelname)-8s - %(name)-16s - %(message)s", level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def stop():
    logger.info("Stopping IoMBian Shutdown Service")
    server.stop()


def signal_handler(sig, frame):
    stop()


if __name__ == "__main__":
    logger.info("Starting IoMBian Shutdown Service")

    shutdown_commands = ShutdownCommands()

    server = CommunicationServer(shutdown_commans, host=SHUTDOWN_HOST, port=SHUTDOWN_PORT)
    server.start()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.pause()
