from sys import stderr
import paramiko
import time


class CiscoRouter:
    '''This class assumes the device type is a Cisco Router, make sure to check vendor type using other available classes before using this class'''
    
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        
    def show_cmd_ssh(self, command):
        '''Takes a single command as a string and return output in a list format'''
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(hostname=self.hostname, username=self.username, password=self.password, allow_agent=False, look_for_keys=False)
        stdin, stdout, stderr = conn.exec_command(command)
        stdout = stdout.readlines()
        return stdout
    
    def config_cmd_ssh(self, cmd_list):
        try:    
            '''Takes a list of commands and push them to device using SSH. Returns true configuration was successful.
            No capability to return error if connection was successful but command was wrong.'''
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(hostname=self.hostname, username=self.username, password=self.password, allow_agent=False, look_for_keys=False)
        except paramiko.AuthenticationException:
            return False
        except paramiko.SSHException:
            return False
        
        rtcon = conn.invoke_shell()
        time.sleep(1)
        rtcon.send('configure terminal\n')
        time.sleep(1)
        for command in cmd_list:
            rtcon.send(command + '\n')
            time.sleep(1)
            
        return True
        
           
        
    
    
