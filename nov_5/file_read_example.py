import os
file_size = os.path.getsize("./textfile.txt")
print(f"File size: {file_size} bytes")

with open("./textfile.txt", 'r') as file:
    first_text = file.read()

    print(f" first text {len(first_text)} bytes ".center(80, "-"))
    print(first_text)

    file.seek(0)

    print(f" second text ".center(80, "-"))
    for line in file:
        print(line)
