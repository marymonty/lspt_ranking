# lspt_ranking
Main repository for the Ranking team (Mary Montgomery, Bill Pedoto, Chris Tang, and Alex Garten) to store their project for Large Scale Programming & Testing.

Code to be reviewed is pushed to the `development` branch.

# To set up server from an empty directory.
```
$ mkdir lspt_ranking  
$ cd lspt_ranking  
$ virtualenv .venv  
$ source .venv/bin/activate  
$ pip install falcon  
$ git clone ...  
```

# The file hierarchy should look like this after setup:
```
lspt_ranking  
├── .venv  
└── lspt_ranking  
  ├── __init__.py  
  └── app.py  
```

# To run the server, open up a terminal and enter the following:
```
$ source .venv/bin/activate  
$ pip install gunicorn  
$ gunicorn --reload lspt_ranking.app  
```

# To call the server, install httpie like so:
```
$ source .venv/bin/activate
$ pip install httpie
$ http localhost:8000
```
# To request the rankings for a certain query (for example, "apple banana"), call the endpoint with the request in list form.
```
$ http localhost:8000/ranking?query=[\"apple\",\"banana\"]
```

# Further reading regarding Falcon:  
https://falcon.readthedocs.io/en/stable/user/tutorial.html