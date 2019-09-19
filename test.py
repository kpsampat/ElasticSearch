from elasticsearch import Elasticsearch
import json


# Connect to the elastic cluster
es=Elasticsearch([{'host':'192.168.86.78','port':8240}])

#res=es.get(index='kp_index',doc_type='students',id=5)
#print res

res = es.search(index="kp_index", body={"query": {"match_all": {}}})
abc =  res['_shards']
print abc


