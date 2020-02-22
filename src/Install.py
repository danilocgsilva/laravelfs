import os
from src.InstallException import InstallException

class Install:

    def setOs(self, os):
        self.os = os

    def getExecutablePath(self):

        if not hasattr(self, 'os'):
            raise InstallException('You need to set the os object inside install with setOs method.')

        if self.os.name == 'nt':
            return 'C:' + self.os.sep + 'Windows'
        if self.os.name == 'darwin' or self.os.name == 'posix':
            return self.os.sep + 'usr' + self.os.sep + 'local' + self.os.sep + 'bin'


    def getProgramEntry(self):

        if not hasattr(self, 'os'):
            raise InstallException('You need to set the os object inside install with setOs method.')
        
        if self.os.name == 'nt':
            return 'laravelfs.cmd'
        if self.os.name == 'darwin' or self.os.name == 'posix':
            return 'laravelfs'

