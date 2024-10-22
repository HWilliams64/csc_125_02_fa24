import random

class SmartPhone:
    weight = 10
    height = 5
    width = 5
    length = 1
    make = "Apple"
    model = "iPhone 12"
    color = "Black"
    minutes = 0
    max_minutes = 500

    def call(self, duration) -> int:
        minutes_left = self.max_minutes - self.minutes
        
        total_time = min(duration, minutes_left)

        self.minutes += total_time
        
        return total_time

    def reset(self) -> None:
        self.minutes = 0




my_iphone = SmartPhone()
your_android = SmartPhone()

your_android.make = "Samsung"
your_android.model = "S22"
your_android.color = "Black"

print(f"Weight: {my_iphone.weight} grams")
print(f"Height: {my_iphone.height} cm")
print(f"Width: {my_iphone.width} cm")
print(f"Length: {my_iphone.length} cm")
print(f"Type: {my_iphone.color} {my_iphone.make} {my_iphone.model}")
print(f"Type: {your_android.color} {your_android.make} {your_android.model}")

print("="*80)
for _ in range(50):
    expected_duration = random.randint(1, 60)
    actual_duration = your_android.call(expected_duration)
    print(f"Expected duration: {expected_duration} minutes. Actual duration: {actual_duration} minutes.")  
    print(f"Remaining minutes on your phone: {your_android.minutes}/{your_android.max_minutes} minutes")
    if actual_duration < expected_duration:
        print("You reset the phone plan!!!")
        your_android.reset()
