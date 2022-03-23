"""
This script offers the CLI interface for the PYETL package.
TODO: Rest of the information will be updated as and when the code is written
"""

# Importing python libraries for required processing
import sys

from src.core.config.global_variables import GlobalVariables
from src.scripts.install import Install
from pathlib import Path
import click


def get_package_root():
    """
    Thi function fetches the path to the parent directory and returns the path as a string.

    Returns:
        path ():    Path to the root directory of the project as a string.
    """

    return str(Path(__file__).parent.parent.parent)


def _init(**kwargs):
    """
    Initialize the global system properties.
    TODO: Starting point for logging the package
    """

    # Initializing the parent root directory for path configuration.
    kwargs['package_root'] = get_package_root()

    # Initializing the Global Variables which will be available throughout the project.
    global_variables = GlobalVariables(**kwargs)
    global_variables.load_configuration_properties()

    return global_variables


def update_authenticate_credentials(properties, **kwargs):
    # Based on the arguments passed, update the properties
    if kwargs['username'] and kwargs['password']:
        properties['username'] = kwargs['username']
        properties['password'] = kwargs['password']
    else:
        click.echo(click.style('ERROR: USER CREDENTIALS: Missing "username" or "password". Please enter both the username and password.', bold=True, bg='red'), err=True)
        sys.exit()


# Main code execution will start from here.
def main(global_properties):
    install = Install(global_properties)
    install.create_infrastructure()
    pass


# This is the main initialization command
@click.command()
@click.option('-s', '--system', required=True, type=click.Choice(['MacOS', 'Windows']), help='Enter your system build, MacOS or Windows')
@click.option('-c', '--config', required=True, type=click.Choice(['True', 'False']), help='If "True", all the properties will be loaded from config file. Else, you need to provide all other parameters.')
@click.option('-u', '--username', type=str, help='Enter your username, which is used to login to Computer Vision remote servers')
@click.option('-p', '--password', type=str, help='Enter your password, which is used to login to Computer Vision remote servers')
def cli(**kwargs):

    # Run the init method to load the default properties available
    global_variables = _init(**kwargs)
    global_properties = global_variables.global_properties

    # Setting up the system information
    global_properties['system'] = kwargs['system']

    if kwargs['config'] == 'False':
        # Update user credentials, if available
        update_authenticate_credentials(global_properties, **kwargs)

    # Main code execution will start from here.
    main(global_properties)


if __name__ == '__main__':
    cli()
