from kafka import KafkaConsumer
import json
import mysql.connector

#mycursor = mydb.cursor()
consumer = KafkaConsumer('test_topic',
                         bootstrap_servers = ['127.0.0.1:9092'] ,
                         api_version=(0,10,1)
                         )
consumer.subscribe(['test_topic'])
for message in consumer:
    print(message)
    data=json.load(message)
    
    sql = "INSERT INTO customers(followers , followees) VALUES(%s , %s)"
    val = (
        data['folowers'],
        data['folowing']
    )
#    mycursor.execute(sql ,  val)
#    mydb.commit()