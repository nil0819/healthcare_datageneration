from dataclasses import dataclass, field

@dataclass
class BaselineHealth:
    heart_rate = 70
    systolic_bp=100
    diastolic_bp=75
    body_temperature=36.8
    oxygen_saturation=99
