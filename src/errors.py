class EndpointException(Exception):
    def __init__(self, message):
        self.message = message

class WeightNotExist(Exception):
    def __init__(self, message):
        self.message = message

class ServerErrorCode(Exception):
    def __init__(self, message):
        self.message = message