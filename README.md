# lspt_ranking
repo for Mary, Bill, Chris, and Alex to store their ranking project for large scale programming and testing

code so far is in the Development branch

# To set up server from an empty directly  
```
$ mkdir lspt_ranking  
$ cd lspt_ranking  
$ virtualenv .venv  
$ source .venv/bin/activate  
$ pip install falcon  
$ git clone ...  
```

# At the end should look like: 
```
lspt_ranking  
├── .venv  
└── lspt_ranking  
  ├── __init__.py  
  └── app.py  
```

To run open up a new terminal  
```
$ source .venv/bin/activate  
$ pip install gunicorn  
$ gunicorn --reload lspt_ranking.app  
```

To call it install httpie
```
$ source .venv/bin/activate
$ pip install httpie
$ http localhost:8000
```

```
$ http localhost:8000/ranking?query=[\"apple\",\"banana\"]
```

Further reading:  
https://falcon.readthedocs.io/en/stable/user/tutorial.html