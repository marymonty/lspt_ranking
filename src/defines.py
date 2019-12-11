"""Module for frequently used global definitions.

Definitions are created here that can be included in other modules.
These include the names of our metrics:
    - POPULARITY,
    - RECENCY,
    - RELEVANCY,
    - CENTRALITY,
as well as changeable paths to our team's API endpoint and weight path that 
holds the file used to calculate weights.
These need to be easily changable so we can switch out our team's API
endpoint or weight file effortlessly and without having to change code
in every file.
Also included are shortened names for calling the teams:
    - Text Transformation (TT),
    - Document Data Storage (DDS), 
    - Link Analysis (LINKAN).
"""
POPULARITY = 'popularity'
RECENCY = 'recency'
RELEVANCY = 'relevancy'
CENTRALITY = 'centrality'

ENDPOINT_PATH = 'lspt_ranking/bin/endpoints.json'
WEIGHT_PATH = 'lspt_ranking/bin/weight_file.json'
TT = "text_tranformation"
INDEXING = "indexing"
DDS = "dds"
LINKAN = "LinkAnalysis"
