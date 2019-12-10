"""Module for needed global definitions.
Module description:
	Definitions are created here that can be included in other modules.
	These include names of our metrics, POPULARITY, RECENCY, RELEVANCY, CENTRALITY,
	as well as changable paths to our team's API endpoint and weight path that 
	holds our file where we calculate weights. These need to be easily changable 
	so we can switch out our team's API endpoint or weight file effortlessly and 
	without having to change code in every file. Also included are shortened names 
	for calling teams: Text Transformation was shortened to TT, Document Data 
	Storage was shortened to DDS, and Link Analysis was shortened to LINKAN.
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
