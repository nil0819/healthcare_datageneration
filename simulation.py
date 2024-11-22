from paho.mqtt import client as mqtt
import time
import random
import json
import simpy
from mqtt_config import mqttConfig
from mqtt_server_exec import MQTTServerExec
from person.healthy_person import HealthyPerson




# # Create an MQTT client instance
# client = mqtt.Client("VirtualIoTDevice")

# config = mqttConfig()

# person_counter = 1

# client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

# client.tls_set()

# # Connect to the MQTT broker
# client.connect(mqtt.MQTT_BROKER, MQTT_PORT)
# client.loop_start()

# # Counter for the number of people
# person_counter = 1


# def configure_mqtt_server():
#         # Create an MQTT client instance
#     #client = mqtt.Client("VirtualIoTDevice")

#     client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)

#     client.tls_set()

#     # Connect to the MQTT broker
#     client.connect(config.MQTT_BROKER, config.MQTT_PORT)
#     client.loop_start()

#     # Counter for the number of people
#     person_counter = 1
        

def simulate_health_care():
                healthy_person=HealthyPerson(1)
                my_mqtt_sever=MQTTServerExec()
                start_time = time.time()
                while True:
                        id,data = healthy_person.generate_data()
                        my_mqtt_sever.publishData(data,id)
                        # Wait for 20 seconds before the next iteration
                        time.sleep(20)
                        if time.time()-start_time > 600:
                                print("Simulation done")
                                break


        # while True:
        #         health_data = {
        #         f"person_{1}":{
        #                 "heart_rate": random.randint(60,100),
        #                 "blood_pressure": f"{random.randint(90,120)}/{random.randint(60,80)}",
        #                 "body_temperature": round(random.uniform(36.5, 37.5),1),
        #                 "oxygen_saturation": random.randint(95,100),
        #                 "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        #         }
        # }

                # # Convert to JSON and publish the data
                # client.publish(config.TOPIC, json.dumps(health_data))
                # print(f"Published data for person_{1}: {health_data}")

                # # Increment the counter for the next person
                # #person_counter += 1

                # # Wait before generating data for the next person

        
                time.sleep(5)
                
        
                

if __name__ == "__main__":
        simulate_health_care()