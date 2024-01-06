import paramiko
from loguru import logger


class SSHClient:
    def __init__(self, ssh_host, port, username, password):
        self.wordpress_host = ssh_host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = paramiko.SSHClient()

    def connect(self):
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the remote server
            self.ssh.connect(self.wordpress_host, port=self.port, username=self.username, password=self.password)

        except Exception as e:
            logger.info(f"Error: {e}")

    def run_command(self, command):
        try:
            # Run the command
            stdin, stdout, stderr = self.ssh.exec_command(command)

            # Read the command output
            output = stdout.read().decode()
            return output

        except Exception as e:
            logger.info(f"Error: {e}")

    def close(self):
        self.ssh.close()
