from typing import Optional
from random import randint

class Network:

    def __init__(self,):
        self.__db = {}  # phone number -> SmartPhone object

    def get_phone(self, phone_number: str) -> Optional["SmartPhone"]:
        return self.__db.get(phone_number, None)

    def register_phone(self, phone_number: str, phone: "SmartPhone") -> None:
        self.__db[phone_number] = phone


class PhonePlan:
    def __init__(self, network: Network, phone_number: str, minutes: int, messages: int, data: int):
        self.__network = network
        self.__phone_number = phone_number
        self.__max_minutes = minutes
        self.__max_messages = messages
        self.__max_data = data

        self.__accum_minutes = 0
        self.__accum_messages = 0
        self.__accum_data = 0

    @property
    def minutes(self) -> int:
        return self.__accum_minutes

    @property
    def minutes_left(self) -> int:
        return max(0, self.__max_minutes - self.__accum_minutes)

    @property
    def messages(self) -> int:
        return self.__accum_messages

    @property
    def data(self) -> int:
        return self.__accum_data

    @property
    def network(self) -> Network:
        return self.__network

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    def call(self, phone_number: str, duration:int) -> int:

        other_phone = self.network.get_phone(phone_number)
        
        if other_phone is None:
            # If the other phone is not registered, we cannot make a call
            return 0
        else:
            # if the other phone is registered, we can make a call
            minutes_left = self.__max_minutes - self.__accum_minutes

            total_time = min(duration, minutes_left)

            self.__accum_minutes += total_time

            return total_time

    def message(self, phone_number: str) -> int:

        other_phone = self.network.get_phone(phone_number)

        if other_phone is None:
            # If the other phone is not registered, we cannot send the message
            return 0
        else:
            # if the other phone is registered, we send the message
            if self.__accum_messages < self.__max_messages:
                self.__accum_messages -= 1
                return 1 # We sent 1 message successfully
            else:
                return 0 # We ran out of messages


class SmartPhone:

    def __init__(self, make="unknown", model="unknown", color="black", plan: Optional[PhonePlan] = None):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__plan = plan

    def call(self,phone_number:str, duration:int) -> int:
        if self.__plan:
            return self.__plan.call(phone_number, duration)
        else:
            return 0

    @property
    def phone_plan(self) -> Optional[PhonePlan]:
        return self.__plan

    @property
    def is_callable(self) -> bool:
        return bool(self.__plan and self.__plan.minutes_left)

    def __str__(self) -> str:
        return f"{self.__make} {self.__model} ({self.__color})"


network = Network()

verizon_plan = PhonePlan(network, "+1(781)-999-888", 100, 100, 100)
t_model_plan = PhonePlan(network, "+1(617)-999-888", 100, 100, 100)

iphone = SmartPhone("Apple", "iPhone 12", "white", t_model_plan)
network.register_phone("+1(781)-999-888", iphone)

pixel = SmartPhone("Google", "Pixel 5", "black", verizon_plan)
network.register_phone("+1(617)-999-888", pixel)

print("Is the iphone callable?", iphone.is_callable)
print("Pixel's minutes left:", pixel.phone_plan.minutes_left)

for _ in range(10):
    dur = randint(10, 60)
    print("The call lasted for:", iphone.call("+1(617)-999-888", dur))
    print("iphone's minutes left:", iphone.phone_plan.minutes_left)
