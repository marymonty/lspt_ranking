"""Classes to handle excaptions.
Module Description:
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
    		self: the server
    		message: the message that will be returned to the user
    		endpoint: the endpoint to send the message to
    	Returns: 
    		none
    	"""
        self.message = message
        self.endpoint = endpoint

class WeightNotExist(Exception):
    """A class for WeightNotExist.
	A WeightNotExist exception will be thrown when a weights file does 
	not exist (weights file	is an internal file just for our team that 
	has our internal weighting metrics.)
	"""
    def __init__(self, message):
        """Initializes the message to send when WeightNotExist is thrown.
    	Takes the arguments and creates an informative message for the user
    	to know what exception is being thrown and why.  
    	Args:
    		self: the server
    		message: the message that will be returned to the user
    	Returns: 
    		none
    	"""
        self.message = message

class ServerErrorCode(Exception):
    """A class for ServerErrorCode.
	ServerErrorCode exception is thrown when a call to an endpoint server has failed.
	"""
    def __init__(self, message, endpoint):
        """Initializes the message to send when ServerErrorCode is thrown.
    	Takes the arguments and creates an informative message for the user
    	to know what exception is being thrown and why. 
		Args:
    		self: the server
    		message: the message that will be returned to the user
    		endpoint: the endpoint to send the message to
    	Returns: 
    		none
    	"""
        self.message = message
        self.endpoint = endpoint
