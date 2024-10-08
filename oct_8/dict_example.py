
# Creations
my_dict = {}
my_dict = dict()

my_dict = {
    "breakfast": "eggs",
    "lunch": "sandwich",
    "dinner": "steak",
    "breakfast_hour": 8,
    12: "lunch time"
}

print(my_dict)

# Addition of key-value pairs
my_dict["snacks"] = "fruit salad"
print(f"After adding snacks: {my_dict}")

# Adding multiple key-value pairs
my_dict.update({"late_night_snack": "yogurt", "breakfast": "pancakes"})
print(f"After adding late night snack: {my_dict}")

# Removal
del my_dict["late_night_snack"]
print(f"After removing late night snack: {my_dict}")

my_dict.pop("snacks")
print(f"After removing snacks: {my_dict}")

# Update value
my_dict["breakfast"] = "oats"
print(f"After updating breakfast: {my_dict}")


# Retrieval
breakfast = my_dict["breakfast"]
print(f"Breakfast: {breakfast}")

snacks = my_dict.get("snacks", "no snacks found")
print(f"Snacks: {snacks}")

# same as above but using a a if statement with out get() method
if "snack" in my_dict:
    breakfast = my_dict["snack"]
    print(f"Snack: {breakfast}")
else:
    print("No snack found")

print("="*80)
# Iterate over the keys
for key in my_dict:
    v = my_dict[key]
    print(key, ":", v)

print("="*80)
for key, value in my_dict.items():  # <- items() returns a 2-tuple for each key-value pair
    print(key, ":", value)

print("="*80)
for v in my_dict.items():  # <- items() returns a 2-tuple for each key-value pair
    print(v[0], ":", v[1])

print("="*80)
for value in my_dict.values():  # <- values() returns a list of values
    print(value)
