import json

import falcon


class Resource(object):

    def on_get(self, req, resp):
        # req_json = json.loads(req)
        print(req.params)
        # for key, value in req.params.items():
        #     print(key, value)
        to_rank = req.params.get('query', '')

        # send to GET/POST
        doc = [
            {"doc" : "doc1", "ranking" : "0.5"},
            {"doc" : "doc1", "ranking" : "0.5"},
        ]
        

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200