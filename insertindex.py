from elasticsearch import Elasticsearch
import random
# Connect to the elastic cluster
es=Elasticsearch([{'host':'192.168.86.78','port':8240}])

stu1={
    "college":"sm-shetty",
    "roll": 79,
    "author":"kishan",

}
stu2={
    "college":"nes",
    "roll": 11,
    "author":"kishan",

}
stu3={
    "college":"wilson",
    "roll": 12,
    "author":"kishan",

}
stu4={
    "college":"vivekanand",
    "roll": 88,
    "author":"kishan",

}
stu5={
    "college":"acharya",
    "roll": 47,
    "author":"kishan",

}

l = [stu1,stu2,stu3,stu4,stu5]
print l
for i in range(100,150):
    res = es.index(index='kisha',doc_type='students',id= i,body=random.choice(l))
#res=es.get(index='school',doc_type='students',id=5)
#print res

#res = es.search(index="firdos", body={"query": {"match_all": {}}})
#print res




