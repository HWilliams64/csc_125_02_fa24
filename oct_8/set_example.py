# Creation
my_set = set()
print(f"Type: {type(my_set)}")

my_set = {}
print(f"Type: {type(my_set)}")

my_set = set([1, 2, 3, 4, 5])

my_set = {0, 1, 2, 3, "a", "b", "c"}
print(f"Type: {type(my_set)}")

# Iteration
for element in my_set:
    print(element)

# Add new elements -> O(1)
my_set.add(4)
my_set.add("d")

print(f"After addition: {my_set}")

# Add another iterable -> O(n)
my_list = [4, 5, 6, 7]
my_set.update(my_list)

print(f"After updating: {my_set}")


# Remove an element -> O(1)
my_set.remove(4)
print(f"After removal: {my_set}")

# Safely remove
my_set.discard(5)
my_set.discard(5)
print(f"After discard: {my_set}")

# Check if elements is in set -> O(1) 
contains_value = 4 in my_set

print(f"Contains value 4: {contains_value}")


# Subset
smaller_set = {1, 2, 3}
print(f"Is subset: {smaller_set.issubset(my_set)}")

v = ["a", "b", "c", 1, 2]
difference = smaller_set.difference(v)
print(f"Difference: {difference}")

intersection = smaller_set.intersection(v)
print(f"Intersection: {intersection}")

isdisjoint = smaller_set.isdisjoint(["z", "zz", "zzz"])
print(f"isdisjoint: {isdisjoint}")

# Remove all duplicates values from a list -> O(n)
duplicate_list = [1, 2, 2, 3, 3, 3]
no_duplicate_list = list(set(duplicate_list))
print(f"No duplicate list: {no_duplicate_list}")
