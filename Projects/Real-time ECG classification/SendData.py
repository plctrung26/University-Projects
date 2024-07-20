import time
import json
import pandas as pd
from kafka import KafkaProducer

TOPIC_NAME = "test_topic"
keyfolderName = "C:/Users/ASUS/jupyter_file/DS104/Send/key/"
datapath = "C:/Users/ASUS/jupyter_file/DS104/Send/data/"

producer = KafkaProducer(
    bootstrap_servers="kafka-7706a89-ds104.a.aivencloud.com:25429",
    security_protocol="SSL",
    ssl_cafile=keyfolderName+"ca.pem",
    ssl_certfile=keyfolderName+"service.cert",
    ssl_keyfile=keyfolderName+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda v: json.dumps(v).encode('ascii'),
    api_version = (2, 12, 0)
)
data = pd.read_csv(datapath + "mitbih_train.csv", header= None)

for i in range(data.shape[0]):
    val = data.iloc[i,:-1].values.tolist()
    message = {
            'val': val
        }
    key = {'key':i}
    producer.send(topic = TOPIC_NAME,key = key, value = message)
    print(f"Message sent: {i+1}")
    time.sleep(1)
producer.close()