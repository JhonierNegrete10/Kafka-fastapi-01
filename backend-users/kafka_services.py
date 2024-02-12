import json

from kafka import KafkaProducer

# Configuración de Kafka
KAFKA_SERVER = "kafka-1:29092"
KAFKA_TOPIC = "user_registered"


# Conectar al servidor Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def kafka_send(value):
    producer.send(KAFKA_TOPIC, value=value)
