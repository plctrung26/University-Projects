from kafka import KafkaConsumer
import csv 

TOPIC_NAME = "test_topic"

keyfolderName = "C:/Users/ASUS/jupyter_file/DS104/Receive/key/"
datapath = "C:/Users/ASUS/jupyter_file/DS104/Receive/data/"
consumer = KafkaConsumer(
    TOPIC_NAME,
    auto_offset_reset="earliest",
    bootstrap_servers="kafka-7706a89-ds104.a.aivencloud.com:25429",
    group_id = "ds104",
    security_protocol="SSL",
    ssl_cafile=keyfolderName+"ca.pem",
    ssl_certfile=keyfolderName+"service.cert",
    ssl_keyfile=keyfolderName+"service.key"
)



with open(datapath + 'recievedData.csv', 'a', encoding='UTF8', newline='') as f:
    for msg in consumer:
        data = msg.value.decode("utf-8").split(":")[1][2:-2].split(",")
        print("message :", msg.key)
        writer = csv.writer(f)
        writer.writerow(data)
        print("successfully saved: ", msg.key)
