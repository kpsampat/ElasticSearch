from elasticsearch import Elasticsearch


# Connect to the elastic cluster
es=Elasticsearch([{'host':'192.168.86.78','port':8240}])

request_body = {
	    "settings" : {
	        "number_of_shards": 3,
	        "number_of_replicas": 0,
	    }
	}
print("creating 'example_index' index...", es.indices.create(index = 'kp_index', body = request_body))



