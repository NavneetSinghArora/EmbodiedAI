"""
This is a Setup script.
The script is used to install the project either on the Local System or a Remote System provided by University.
For local system, make changes to configuration.properties and execute the script.
For remote system, make changes to configuration.properties, connect to the Informatik VPN and execute the script.
"""

# Importing python libraries for required processing
import invoke
from fabric import Connection


def command_sequence(connection, properties):
    """
    This function helps run a sequence of commands on the remote server.
    It uses the global properties and runs the commands to create the basic directory structure on the server.

    Args:
        param connection:   Open session from the running ssh connection to the remote server.
        param properties:   Dictionary of all global properties available across the project.

    Returns:
        return:             None
    """
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
    """
    This class contains the first and foremost step to take the basic installation.
    This creates the basic infrastructure to execute the project.
    """

    def __init__(self, properties):
        """
        This is the init method.
        It receives the global properties for the project.

        Args:
            param properties:   Dictionary of all global properties available across the project.
        """

        self.properties = properties

    def authenticate(self):
        """
        This is the method which helps authenticate the user with the remote server.

        Returns:
            connection:     Open session object for the connection to the remote server
        """
        url = self.properties['url']
        username = self.properties['username']
        password = self.properties['password']
        system_name = self.properties['system_name']
        host = system_name + url

        connection = Connection(host=host, user=username, connect_kwargs={"password": password})

        return connection

    def create_infrastructure(self):
        """
        This method is the main method which call for authentication and executes the sequence of commands to
        create the base infrastructure.
        """

        connection = self.authenticate()
        command_sequence(connection, self.properties)
