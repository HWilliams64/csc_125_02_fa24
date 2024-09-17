user_prompt = "Please type a number: "

def input_number(prompt):
    user_input = input(prompt)
    while not user_input.isdigit():
        print("Invalid input. Please enter a valid integer.")
        user_input = input(prompt)
    return int(user_input)


# user_input = input("Enter a number: ")
# while not user_input.isdigit():
#     print("Invalid input. Please enter a valid integer.")
#     user_input = input("Enter a number: ")
# num1 = input_number()
num1 = input_number("Please type your first number: ")

user_input = input("Enter a operation: ")
while not user_input in "+-*/":
    print("Invalid input. Please enter a valid operation.")
    user_input = input("Enter a operation: ")

op = user_input

# user_input = input("Enter a number: ")
# while not user_input.isdigit():
#     print("Invalid input. Please enter a valid integer.")
#     user_input = input("Enter a number: ")
# num2 = int(user_input)
num2 = input_number("Please type your second number:  ")


print(f"{num1} {op} {num2} =", eval(f"{num1} {op} {num2}"))