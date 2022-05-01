from ensurepip import bootstrap
import json
import profile
from sys import api_version
from kafka import KafkaProducer
from insta import instagram

user = instagram()
#json = json.dumps()
#profile = user.profile()
producer = KafkaProducer(bootstrap_servers = ['127.0.0.1:9092'] , api_version=(0,10,1) ,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('test_topic', value={"folower":user.followers,"folowing":user.followees})