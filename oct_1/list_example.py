groceries = ["apple", "banana", "orange"]

print(
    f"Groceries: {groceries} {type(groceries).__name__} Size: {len(groceries)}")

# Access
for e in groceries:
    print(f"Element: {e}")


first_value = groceries[0]
last_value = groceries[-1]

print(f"First value: {first_value}")
print(f"Last value: {last_value}")

sub_list = groceries[1:3]
print(f"Sub-list: {sub_list}")

# Add 
groceries.append("kiwi")
print(f"Add kiwi - Groceries: {groceries}")

groceries[0] = "rice"
print(f"Replace rice - Groceries: {groceries}")

# Size
print(f"Size of groceries: {len(groceries)}")

# Remove
del groceries[0]
print(f"After delete - Groceries: {groceries}")
print(f"After delete - Size: {len(groceries)}")

groceries.remove("banana") # <- The value must be in the list
print(f"After remove - Groceries: {groceries}")
print(f"After remove - Size: {len(groceries)}")

has_banana = False

for fruit in groceries:
    if fruit == "banana":
        has_banana = True
        break

has_banana_v2 = "banana" in groceries

print(f"Has banana: {has_banana}")

print(f"Has banana v2: {has_banana_v2}")
