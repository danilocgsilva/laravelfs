class OsMocker:

    def setSystem(self, system):

        allowed_value = ['windows', 'mac', 'linux']

        if not system in allowed_value:
            raise Exception('No allowed system to inject to mock!')

        if system == 'windows':
            self.sep = '\\'
            self.name = 'nt'

        if system == 'mac':
            self.sep = '/'
            self.name = 'darwin'

        if system == 'linux':
            self.sep = '/'
            self.name = 'posix'


