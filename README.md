# IoMBian Shutdown Service

This service handles all the shutdown, reboot and all those events for the IoMBian.
If any other service wants to shutdown the machine, it only needs to send a "shutdown" message to this service with a ZeroMQ socket (port 5558 by default).

The possible events are:
- Shutdown: "shutdown"
- Reboot: "reboot"

Any ZeroMQ client can connect to this port and send any event.

## Installation

- Define project name in environment variable:

`PROJECT_NAME=iombian-shutdown-service`

- Clone the repo into a temp folder:

`git clone https://github.com/Tknika/${PROJECT_NAME}.git /tmp/${PROJECT_NAME} && cd /tmp/${PROJECT_NAME}`

- Create the installation folder and move the appropriate files (edit the user):

`sudo mkdir /opt/${PROJECT_NAME}`

`sudo cp requirements.txt /opt/${PROJECT_NAME}`

`sudo cp -r src/* /opt/${PROJECT_NAME}`

`sudo cp systemd/${PROJECT_NAME}.service /etc/systemd/system/`

`sudo chown -R iompi:iompi /opt/${PROJECT_NAME}`

- Create virtual environment and install the dependencies:

`cd /opt/${PROJECT_NAME}`

`python3 -m venv venv`

`source venv/bin/activate`

`pip install --upgrade pip`

`pip install -r requirements.txt`

- Start the script

`sudo systemctl enable ${PROJECT_NAME}.service && sudo systemctl start ${PROJECT_NAME}.service`

## Docker

To build the docker image, from the cloned repository, execute the docker build command in the same level as the Dockerfile.
In this case replace the variables like `${IMAGE_NAME}` with a value.

`docker build -t ${IMAGE_NAME}:${IMAGE_VERSION}`

For example:
`docker build -t iombian-shutdown-service:latest .`

After building the image, execute it with docker run.

`docker run --name ${CONTAINER_NAME} --privileged --rm -d -v /run/systemd/system:/run/systemd/system -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket -v /bin/systemctl:/bin/systemctl -p 5558:5558 -e LOG_LEVEL=DEBUG iombian-shutdown-service:latest`

- **--name** is used to define the name of the created container.

- **-privileged** is for granting privileges to the docker container.
This is needed because the iombian-button-handler needs to create a thread to listen to the button events.

- **--rm** can be used to delete the container when it stops.
This parameter is optional.

- **-d** is used to run the container detached.
This way the container will run in the background.
This parameter is optional.

- **-v** is used to pass a volume to the container.
In this case it's used to give the container access to some files.
This volumes are necessary so the container can shut down the host machine.

- **-p** is used to expose the internal 5558 port to the external 5558 port.
The 5558 port is where other services will need to connect to send the event messages.
The port is exposed so the services from outside the containers network can access to this service.

- **-e** can be used to define the environment variables:
    - SHUTDOWN_EVENTS_PORT: The port where the services need to connect to send the event messages.
    Default port is 5558.
    - LOG_LEVEL: define the log level for the python logger.
    This can be NOTSET, DEBUG, INFO, WARNING, ERROR or CRITICAL.
    Default value is INFO.

## Author

(c) 2024 [Tknika](https://tknika.eus/en/)([Aitor Castaño](github.com/aitorcas23))
