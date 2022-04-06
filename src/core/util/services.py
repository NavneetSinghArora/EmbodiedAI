"""

"""

# Importing python libraries for required processing
import invoke
from invoke.watchers import Responder
import git


def setup_directory_structure(connection, properties):
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
            connection.run('ls -ltr | grep ' + properties['username'])
        except invoke.exceptions.UnexpectedExit:
            connection.run('mkdir ' + properties['username'])


def setup_conda_environment(connection, properties):
    temporary_directory = '/tmp'
    conda_environment = properties['conda_git']
    conda_script = properties['conda_script']

    system_type = properties['system_type']
    conda_large_path = properties['conda_large_path']
    conda_small_path = properties['conda_small_path']
    username = properties['username']
    if system_type == 'large':
        environment_path = conda_large_path + '/home/' + username + '/anaconda3/bin/conda'
    else:
        environment_path = conda_small_path + '/home/' + username + '/anaconda3/bin/conda'

    installation_watchers = [
        Responder(pattern=r'Please, press ENTER to continue', response='\n'),
        Responder(pattern=r'Do you accept the license terms? *', response='yes\n'),
        Responder(pattern=r'Press ENTER to confirm the location *', response='\n'),
        Responder(pattern=r'Do you wish the installer to initialize Anaconda3 *', response='yes\n')
    ]

    try:
        connection.run(environment_path + ' list')
        print("Conda is already available")
    except invoke.exceptions.UnexpectedExit:
        try:
            with connection.cd(temporary_directory):
                connection.run('curl -O ' + conda_environment)
                connection.run('sha256sum ' + conda_script)
                connection.run('bash ' + conda_script, watchers=installation_watchers)
                print("Conda installed successfully.")
        except invoke.exceptions.UnexpectedExit:
            print("Error installing conda on the remote server.")
            print("Please check the connection or Contact Administrator or Install Manually")

        try:
            with connection.cd(temporary_directory):
                # connection.run('~/.bashrc')
                connection.run('source ~/.bashrc')
                connection.run(environment_path + ' list')
                print("Conda setup successfully.")
        except invoke.exceptions.UnexpectedExit:
            print("Error setting up conda on the remote server.")
            print("Please check the connection or Contact Administrator or Install Manually")


def setup_main_code(connection, properties):
    system_type = properties['system_type']
    conda_large_path = properties['conda_large_path']
    conda_small_path = properties['conda_small_path']
    username = properties['username']
    main_code = properties['main_code']
    code_directory = properties['code_directory']

    if system_type == 'large':
        environment_path = conda_large_path + '/home/' + username
    else:
        environment_path = conda_small_path + '/home/' + username

    with connection.cd(environment_path):
        try:
            connection.run('ls -ltr | grep ' + code_directory)
        except invoke.exceptions.UnexpectedExit:
            try:
                connection.run('git clone ' + main_code)
            except invoke.exceptions.UnexpectedExit:
                print("Error cloning the main repository.")
                print("Reach out to the Administrator or Do it Manually")


def setup_virtual_environment(connection, properties):
    system_type = properties['system_type']
    conda_large_path = properties['conda_large_path']
    conda_small_path = properties['conda_small_path']
    username = properties['username']
    code_directory = properties['code_directory']

    if system_type == 'large':
        environment_path = conda_large_path + '/home/' + username + '/anaconda3/envs'
        conda_path = conda_large_path + '/home/' + username + '/anaconda3/bin/'
    else:
        environment_path = conda_small_path + '/home/' + username + '/anaconda3/envs'
        conda_path = conda_small_path + '/home/' + username + '/anaconda3/bin/'

    with connection.cd(environment_path):
        try:
            connection.run('ls -ltr | grep ' + code_directory)
            print('Conda Environment already exists')

            print('Updating the conda environment with new dependencies, if any')
            connection.run(conda_path + 'conda env update --prefix ./' + code_directory + ' --file ../../' + code_directory + '/resources/environment.yml --prune')
            # connection.run(conda_path + 'conda install --name ' + code_directory + ' --file ../../' + code_directory + '/resources/linux64.txt')
            # connection.run('rm -rf ' + code_directory)
            # connection.run(conda_path + 'conda env create -f ../../' + code_directory + '/resources/environment.yml')
        except invoke.exceptions.UnexpectedExit:
            try:
                # connection.run(conda_path + 'conda create --name ' + code_directory + ' --file ../../' + code_directory + '/resources/linux64.txt')
                # connection.run(conda_path + 'conda env export --no-builds -n ' + code_directory + ' > ../../' + code_directory + '/resources/environment.yml')
                # connection.run('rm -rf ' + code_directory)
                connection.run(conda_path + 'conda env create -f ../../' + code_directory + '/resources/environment.yml')
            except invoke.exceptions.UnexpectedExit:
                print("Error while creating the conda virtual environment")
                print("Reach out to the Administrator or Do it Manually")
