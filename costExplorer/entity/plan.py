from enum import Enum

# class PlayType(Enum):
#     BASIC = 1
#     STANDARD = 2
#     PREMIUM = 3

class Plan(object):
    def __init__(self, planType: str, monthlyCost: float):
        self.planType = planType
        self.monthlyCost = monthlyCost
