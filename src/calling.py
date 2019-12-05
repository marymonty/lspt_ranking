import json

import falcon
from .controller import GET

CORRECT_REQUEST = """Error request format. The request must contain query=[string].
Optional fields include n_results = int"""

class Resource(object):

    def on_post(self, req, resp):
        # Extract the query and fields from the request.
        req_body = json.loads(req.stream.read().decode('ascii'))
        to_rank = req_body.get('query', '')
        n_results = int(req_body.get('results', '50'))

        # Check that the query is well-formed.
        if to_rank == '' or \
            not isinstance(to_rank, str):
            resp.body = CORRECT_REQUEST
            resp.status = falcon.HTTP_400
        else:
            results = GET(to_rank, n_results)

            # Create a JSON representation of the resource.
            resp.body = json.dumps(results, ensure_ascii=False)

            resp.status = falcon.HTTP_200
