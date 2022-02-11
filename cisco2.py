from sys import stderr
import paramiko
import time


class CiscoRouter:
    '''This class assumes the device type is a Cisco Router, make sure to check vendor type using other available classes before using this class'''
    
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.conn = paramiko.SSHClient()
        self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.conn.connect(hostname=self.hostname, username=self.username, password=self.password, allow_agent=False, look_for_keys=False)
        self.rtcon = self.conn.invoke_shell()
        
    def close_connection(self):
        if self.conn != None:
            self.conn.close()
    
        
    def show_cmd_ssh(self, command):
        '''Takes a single command as a string and return output in a list format'''
        stdin, stdout, stderr = self.conn.exec_command(command)
        stdout = stdout.readlines()
        return stdout
    
    def config_cmd_ssh(self, cmd_list):
        '''Takes a list of commands and push them to device, this method don't close connection by itself.'''
        self.rtcon.send('configure terminal\n')
        time.sleep(1)
        for command in cmd_list:
            self.rtcon.send(command + '\n')
            time.sleep(1)
            
        return True
        
           
        
    
    
