class EndpointException(Exception):
    def __init__(self, message, endpoint):
        self.message = message
        self.endpoint = endpoint

class WeightNotExist(Exception):
    def __init__(self, message):
        self.message = message

class ServerErrorCode(Exception):
    def __init__(self, message, endpoint):
        self.message = message
        self.endpoint = endpoint