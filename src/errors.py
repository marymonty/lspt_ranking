"""Classes to handle frequently encountered and expected exceptions.

There are three classes included in this file, each addressing
a different failure case for the server. Within each class is 
one function, an __init__ function that creates the message
to send. 
"""
class EndpointException(Exception):
    """A class for EndpointException.

    An endpoint exception will be thrown when an invalid endpoint 
    was given or cannot be reached.
    """
    def __init__(self, message, endpoint):
        """Initializes the message to send when EndpointException is thrown.
        Takes the arguments and creates an informative message for the user
        to know what exception is being thrown and why. 
        Args:
            self: The EndpointException object.
            message: The message that will be returned to the user.
            endpoint: The endpoint to send the message to.
        Returns: 
            Does not return anything.
        """
        self.message = message
        self.endpoint = endpoint

class WeightNotExist(Exception):
    """A class for WeightNotExist.

    A WeightNotExist exception will be thrown when a weights file does 
    not exist.
    The weights file is an internal file that contains our internal
    weighting metrics.
    """
    def __init__(self, message):
        """Initializes the message to send when WeightNotExist is thrown.
        Takes the arguments and creates an informative message for the user
        to know what exception is being thrown and why.
        Args:
            self: the WeightNotExist object.
            message: The message that will be returned to the user.
        Returns: 
            Does not return anything.
        """
        self.message = message

class ServerErrorCode(Exception):
    """A class for ServerErrorCode.
    ServerErrorCode exception is thrown when a call to an endpoint server
    has failed.
    """
    def __init__(self, message, endpoint):
        """Initializes the message to send when ServerErrorCode is thrown.
        Takes the arguments and creates an informative message for the user
        to know what exception is being thrown and why. 
        Args:
            self: The ServerErrorCode object.
            message: The message that will be returned to the user.
            endpoint: The endpoint to send the message to.
        Returns: 
            Does not return anything.
        """
        self.message = message
        self.endpoint = endpoint
