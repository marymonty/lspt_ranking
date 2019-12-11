# Ranking -- Large Scale Programming & Testing -- Fall 2019

## Team Members
* Alex Garten
* Mary Montgomery
* Billy Pedoto
* Chris Tang

## Hostname: lspt-rank2.cs.rpi.edu
## Port: 80

## Overview
* Main repository for the Ranking team to store their project component for Large Scale Programming & Testing's class-wide search engine.
* The ranking service is designed to take a list of URLs (in the form of document IDs), and return them in sorted order based on their rank. Each URL's rank calculation factors in its PageRank score, metadata pulled from Document Data Storage (DDS), and much more.
* Code to be reviewed is pushed to the `development` branch.
* Reviewed code is siphoned off the `development` branch into the `master` branch.
* Other services can request rankings of specific document IDs through the GET functionality.

## Instructions For Use
### To set up server from an empty directory.
```
$ mkdir lspt_ranking  
$ cd lspt_ranking  
$ virtualenv .venv  
$ source .venv/bin/activate  
$ pip install falcon  
$ git clone ...  
```

### The file hierarchy should look like this after setup:
```
lspt_ranking  
├── .venv  
└── lspt_ranking  
  ├── __init__.py  
  └── app.py  
```

#### To run the server, open up a terminal and enter the following:
```
$ source .venv/bin/activate  
$ pip install gunicorn  
$ gunicorn --reload lspt_ranking.app  
```

### To call the server, install httpie like so:
```
$ source .venv/bin/activate
$ pip install httpie
$ http localhost:8000
```
### To request the rankings for a certain query (for example, "apple banana"), call the endpoint with the request in list form.
```
$ http localhost:8000/ranking?query="apple banana"
```

### Further reading regarding Falcon:  
https://falcon.readthedocs.io/en/stable/user/tutorial.html

### To run on the server the command is:
sudo gunicorn3 lspt_ranking.app -b :80