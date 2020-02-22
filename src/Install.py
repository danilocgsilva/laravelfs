import os

class Install:

    def getExecutablePath(self):
        if self.os.name == 'nt':
            return 'C:' + self.os.sep + 'Windows'
        if self.os.name == 'darwin':
            return self.os.sep + 'usr' + self.os.sep + 'local' + self.os.sep + 'bin'
        if self.os.name == 'posix':
            return self.os.sep + 'usr' + self.os.sep + 'local' + self.os.sep + 'bin'
        

    def setOs(self, os):
        self.os = os


