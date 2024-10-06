my_set = {"apple", "orange", "banana", "grape", "grape"}

print("Length of the set:", len(my_set))
print(f"Set elements: {my_set}")
for e in my_set:
    print(f"Value: {e} Hash: {hash(e)} Modulo {hash(e) % 10}")
