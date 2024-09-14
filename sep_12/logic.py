user_input = input("Please type a number:")

user_input = user_input.lower()

is_digit = user_input.isdigit()

if is_digit:
    print(f"{user_input} is a valid digit.")
    num = int(user_input) # converting string to integer
    is_even = num % 2 == 0 # divide by 2 and check if remainder is 0 (even)
    if is_even:
        print(f"{user_input} is even.")
    else:
        print(f"{user_input} is not even.")
elif user_input in "one two three four five six seven eight nine ten":
    if user_input.startswith("one"):
        num = 1
else:
    print(f"{user_input} is not a valid digit.")
