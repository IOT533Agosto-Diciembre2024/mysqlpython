import time

from db_manager import DBManager
import paho.mqtt.client as mqtt

db_manager = DBManager('10.48.209.159', 'proyecto_xrover', 'profe', 'andrestorres')


def on_message(client, userdata, msg):
    msg = msg.payload.decode()
    msg_split = msg.split("_")
    sensor = msg_split[0]
    valor = msg_split[1]
    #Insertar valor con db manager a la tabla del sensor
    #db_manager.insert_value(valor)
    print(f"El sensor es: {sensor} valor: {valor}")


unacked_publish = set()
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com",1883)
mqtt_client.loop_start()
mqtt_client.subscribe("weccat/ultrasonido")

try:
    print("Esperando mensajes")
    while True:
        time.sleep(1)
except:
    print(f"Ocurrio un error")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()





