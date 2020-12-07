import csv
import json
import pandas as pd
from elasticsearch import Elasticsearch, helpers
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
            # create json file that can be used with CURL or Postman
            jsonfile_curl.write('{ "index" : { "_index" : "spotify-test", "_type" : "track", "_id" :'+str(id_idx) +' } } \n')
            json.dump(row, jsonfile_curl)
            jsonfile_curl.write('\n')
            id_idx += 1

            # create json file for helpers from ES-python Library
            json.dump(row, jsonfile)
            jsonfile.write('\n')

    # add data from json file to ES cluster
    es = Elasticsearch()
    with open("data.json") as json_file:
        helpers.bulk(es, json_file, index='spotify-beta', doc_type='track')