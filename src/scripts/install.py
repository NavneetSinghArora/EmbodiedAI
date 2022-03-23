"""
This is a Setup script.
The script is used to install the project either on the Local System or a Remote System provided by University.
For local system, make changes to configuration.properties and execute the script.
For remote system, make changes to configuration.properties, connect to the Informatik VPN and execute the script.
"""

# Importing python libraries for required processing
import fabric
import invoke
from fabric import Connection


def command_sequence(connection, properties):
    system_type = properties['system_type']
    small_system_path = properties['small_system_path']
    large_system_path = properties['large_system_path']

    if system_type == 'large':
        directory_path = large_system_path
    else:
        directory_path = small_system_path

    with connection.cd(directory_path):
        try:
            connection.run('ls -ltr | grep 0arora')
        except invoke.exceptions.UnexpectedExit:
            connection.run('mkdir ' + properties['username'])


class Install:

    def __init__(self, properties):
        self.properties = properties

    def authenticate(self):
        ssh = None
        url = self.properties['url']
        username = self.properties['username']
        password = self.properties['password']
        system_name = self.properties['system_name']
        host = system_name + url

        connection = Connection(host=host, user=username, connect_kwargs={"password": password})

        return connection

    def create_infrastructure(self):

        connection = self.authenticate()
        command_sequence(connection, self.properties)
