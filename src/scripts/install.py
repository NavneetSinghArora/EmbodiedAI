"""
This is a Setup script.
The script is used to install the project either on the Local System or a Remote System provided by University.
For local system, make changes to configuration.properties and execute the script.
For remote system, make changes to configuration.properties, connect to the Informatik VPN and execute the script.
"""

# Importing python libraries for required processing
from fabric2 import Connection
from src.core.util.services import setup_directory_structure
from src.core.util.services import setup_conda_environment
from src.core.util.services import setup_main_code
from src.core.util.services import setup_virtual_environment
# from src.core.util.services import activate_virtual_environment


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
        setup_directory_structure(connection, self.properties)
        setup_conda_environment(connection, self.properties)
        setup_main_code(connection, self.properties)
        setup_virtual_environment(connection, self.properties)
        # activate_virtual_environment(connection, self.properties)
