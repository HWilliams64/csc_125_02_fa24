groceries = ("apple", "banana", "orange")

print(f"Groceries: {groceries} {type(groceries).__name__}")

# Access
for e in groceries:
    print(f"Element: {e}")


first_value = groceries[0]
last_value = groceries[-1]

print(f"First value: {first_value}")
print(f"Last value: {last_value}")

sub_tuple = groceries[1:3]
print(f"Sub-tuple: {sub_tuple}")


