"""Module to create and check the Query object.
Module description: 
    A class for a Query, used to check that the given query can be made into
    a json object and that falcon can successfully connect to the endpoint for
    further computation.
Typical usage example:
    We receive query {query: "where in new york is rpi"}
    this query can be successfully made into a json string
    and even though an n_gram is not included, we can give 
    a default 50 returned results.
"""
import json

import falcon
from .controller import GET

from .errors import EndpointException, ServerErrorCode

CORRECT_REQUEST = "ERROR: Query paramater must be a string of length greater than 0\n"


class Query(object):
    """A class to represent a Query object.
    A query is what is sent to us. We need to transform and perform computations
    on this query, so we have made it into an object to be easier dealt with here.
    We are checking to see if the Query is something that we can deal with.
    The Query class has one function, on_post.
    """
    def on_post(self, req, resp):
        """Creates a json out of the query, if possible.
        This function will put the given Query object through tests to 
        see if if this input sent to us is in the proper format of what
        we are asking for. If it is, we will convert the query into a json 
        string and use it from there.
        Args:
            self: the Query object
            req: the request, what querying sent to us
            resp: the response
        Raises:
            EndpointException if fails to connect to endpoint
            ServerErrorCode if connection to endpoint does not return 200 (success)
        Returns:
            none: unless exception is thrown, return to exit
        """
        # Extract the query and fields from the request.
        bad_req = False
        try:
            to_rank = req.get_param('query', required=True)
            n_results = req.get_param('results', required=False)
            #set the default number of results to be 50
            if n_results == None:
                n_results = 50
        except ValueError:
            bad_req = True

        # Check that the query is well-formed.
        if bad_req or to_rank == '' or \
            not isinstance(to_rank, str):
            resp.body = CORRECT_REQUEST
            resp.status = falcon.HTTP_400
        else:
            try:
                results = GET(to_rank, n_results)
            except EndpointException as e:
                resp.status = falcon.HTTP_503
                resp.body = "ERROR: Could not connect to endpoint %s\n" % e.endpoint
                return
            except ServerErrorCode as e:
                resp.status = falcon.HTTP_503
                resp.body = "ERROR: Connect to endpoint %s returned a non-200 code\n" % e.endpoint
                return

            # Create a JSON representation of the resource.
            resp.body = json.dumps(results, ensure_ascii=False)

            resp.status = falcon.HTTP_200
