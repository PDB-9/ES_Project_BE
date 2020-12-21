import csv
import json
import pandas as pd
import ast
from elasticsearch import Elasticsearch, helpers
from dotenv import load_dotenv
import os
load_dotenv()
if os.environ.get('ES') is None:
    ELASTICSEARCH_HOST= "localhost:9200"
else:
    ELASTICSEARCH_HOST = os.environ.get('ES')

df = pd.read_csv (r'data.csv')
if(df.isnull().sum().sum() !=0):
    print("Error! Data has null value")
    exit()
else:
    csvfile = open(r'data.csv', 'r', encoding='utf-8')
    jsonfile = open(r'data.json', 'w', encoding='utf-8')
    jsonfile_curl = open(r'data_curl.json', 'w', encoding='utf-8')
    fieldnames = ('valence', 'year', 'acousticness', 'artists', 'danceability', 'duration_ms', 'energy', 'explicit', 'id', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'name', 'popularity', 'release_date', 'speechiness', 'tempo')
    csvReader = csv.DictReader(csvfile, fieldnames)
    id_idx=0
    for row in csvReader:
        if(id_idx==0):
            id_idx+=1
            continue
        else:
            # convert string of list to list
            artists=ast.literal_eval(row['artists'])
            row['artists']=[artist.strip() for artist in artists]

            # create json file that can be used with CURL or Postman
            jsonfile_curl.write('{ "index" : { "_index" : "spotipy", "_type" : "track", "_id" :'+str(id_idx) +' } } \n')
            json.dump(row, jsonfile_curl)
            jsonfile_curl.write('\n')
            id_idx += 1

            # create json file for helpers from ES-python Library
            json.dump(row, jsonfile)
            jsonfile.write('\n')

    # # Init ES
    es= Elasticsearch([ELASTICSEARCH_HOST])
    # es = Elasticsearch(['https://fcpai8781z:rpb78t2zu0@jasmine-450285335.us-east-1.bonsaisearch.net:443'])
    setup= {
        "settings":{
            "number_of_shards":5,
            "number_of_replicas":2
        }
    }
    # Create index
    es.indices.create(index='spotify', ignore=400,body = setup)
    # Add data from json file to ES cluster
    with open("data.json") as json_file:
        helpers.bulk(es, json_file, index='spotify', doc_type='track')