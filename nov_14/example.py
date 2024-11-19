import random

def number_input(prompt):

    number_string = input(prompt)

    try:
        number = int(number_string)
    except ValueError as e:
        msg = str(e)
        print(f"Invalid input: {msg}")
        number = number_input(prompt)

    return number


# number = number_input("Enter a positive integer: ")
# print(number)


def save_to_db():
    errors = (
        ZeroDivisionError,
        ValueError,
        TypeError,
        KeyError,
        IndexError,
        FileNotFoundError
    )

    random_error = random.choice(errors)

    #raise random_error()

    raise ValueError("This is a custom message")


try:
    save_to_db()
except ZeroDivisionError:
    print("Specific except block: Division by zero")
except (KeyError, IndexError) as e:
    print("Specific except block: KeyError, IndexError")
except ValueError as e:
    print(f"Error Message = '{e}'")
except Exception as e:
    print(f"Error: Exception -> {e.__class__.__name__}")
finally:
    print("Finally block executed")
