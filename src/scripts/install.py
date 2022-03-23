"""
This is a Setup script.
The script is used to install the project either on the Local System or a Remote System provided by University.
For local system, make changes to configuration.properties and execute the script.
For remote system, make changes to configuration.properties, connect to the Informatik VPN and execute the script.
"""


# Importing python libraries for required processing
from paramiko.ssh_exception import AuthenticationException, SSHException, BadHostKeyException
import paramiko
import click


class Install:

    def __init__(self, properties):
        self.properties = properties

    def authenticate(self):
        ssh = None
        server = self.properties['url']
        username = self.properties['username']
        password = self.properties['password']

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=server, username=username, password=password)
        except AuthenticationException as authenticationException:
            click.echo(click.style('ERROR: FAILED AUTHENTICATION: Please verify your credentials: %s' % authenticationException, bold=True, bg='red'), err=True)
        except BadHostKeyException as badHostKeyException:
            click.echo(click.style('ERROR: HOST KEY FAILURE: Unable to verify server host key: %s' % badHostKeyException, bold=True, bg='red'), err=True)
        except SSHException as sshException:
            click.echo(click.style('ERROR: FAILED CONNECTION: Unable to establish SSH connection: %s' % sshException, bold=True, bg='red'), err=True)
        finally:
            ssh.close()

        return ssh

    def create_infrastructure(self):

        ssh = self.authenticate()
        # stdin, stdout, stderr = ssh.exec_command('ls -l')
        # stdout = stdout.readlines()
        # print(stdout)
        # pass
        pass
