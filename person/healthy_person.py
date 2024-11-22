from baseline_health import BaselineHealth
import random
import time
from mqtt_server_exec import MQTTServerExec

class HealthyPerson:
    def __init__(
            self,
            person_id: int
    ):
        self.person_id = person_id
        self.heart_rate = 0
        self.blood_pressure_systolic = 0
        self.blood_pressure_diastolic = 0
        self.body_temperature = 0
        self.oxygen_saturation = 0

        

    

    def generate_data(self):
        self.heart_rate = max(60, min(100, BaselineHealth.heart_rate + random.randint(-2, 2)))
        self.blood_pressure_systolic = max(90, min(120, BaselineHealth.systolic_bp + random.randint(-3, 3)))
        self.blood_pressure_diastolic =  max(60, min(80, BaselineHealth.diastolic_bp + random.randint(-3, 3)))
        self.body_temperature = round(max(36.5, min(37.2, BaselineHealth.body_temperature + random.uniform(-0.1, 0.1))), 1)
        self.oxygen_saturation = max(97, min(100, BaselineHealth.oxygen_saturation + random.randint(-1, 1)))

        data = {
            f"person{self.person_id}":{
                "heart_rate":self.heart_rate,
                "blood_pressure_systolic": self.blood_pressure_systolic,
                "blood_perssure_diastolic": self.blood_pressure_diastolic,
                "body_temperature": self.body_temperature,
                "oxygen_saturation":self.oxygen_saturation,
                "timestamp":time.strftime('%Y-%m-%d %H:%M:%S')
            }
        }
        return self.person_id,data
        


    
