class OsMocker:

    def __init__(self, system):

        allowed_value = ['windows']

        if not system in allowed_value:
            raise Exception('No allowed system to inject to mock!')
