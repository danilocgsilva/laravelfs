class OsMocker:

    def setSystem(self, system):

        allowed_value = ['windows', 'mac']

        if not system in allowed_value:
            raise Exception('No allowed system to inject to mock!')


