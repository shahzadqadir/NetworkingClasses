import platform, subprocess
from os import devnull

class Connectivity2:

    def __init__(self, host):
        self.host = host

    def check_connectivity(self):
        if "inux" in platform.platform():
            return self.host_chk_linux()
        elif "indow" in platform.platform():
            return self.host_chk_win()

    def host_chk_win(self):
        FNULL = open(devnull, 'w')
        if subprocess.call(['ping', '-n', 3, self.host], stdout=FNULL) == 0:
            return True
        return False

    def host_chk_linux(self):
        FNULL = open(devnull, 'w')
        if subprocess.call(['ping', '-c', '3', self.host], stdout=FNULL) == 0:
            return True
        return False
