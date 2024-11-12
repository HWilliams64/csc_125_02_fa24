import os, sys

def save_new_note(file_path:str, note:str):
    with open(file_path, 'a') as file:
        file.write(f"{note}\n")

def get_note(file_path:str, index:int) -> str:
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file):
                if line_number+1 == index:
                    return line
    return "Error: Note not found"

def input_number(prompt):
    user_input = input(prompt)
    while not user_input.isdigit():
        print("Invalid input. Please enter a valid integer.")
        user_input = input(prompt)
    return int(user_input)



if __name__ == "__main__":
    file_path = ""

    while True:
        print("\nChoose an option:\n1. Save a new note\n2. Get a note\n3. Change notebook\n4. Exit")
        ui = input_number("Enter your choice (1-4): ")

        if not file_path:
            file_path = input("Enter notebook: ")

        if ui == 1:
            new_note = input("Enter the new note: ")
            save_new_note(file_path, new_note)

        elif ui == 2:
            note_index = input_number("Enter the note index: ")
            result = get_note(file_path, note_index)
            print(result)

        elif ui == 3:
            file_path = input("Enter notebook: ")

        elif ui == 4:
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")
        
