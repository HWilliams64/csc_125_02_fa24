
file_path = "example.txt"
with open(file_path, "w") as file:
    file.write("hello\nhow\nare\nyou")

read_file = open(file_path, "r")

print("="*80)
for line in read_file:
    print(line.strip())

var = "Text"
del var
print(f"Variable 'var' is: {var}")
print("="*80)
