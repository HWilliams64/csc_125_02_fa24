import json

db = {
    "users" : [
        {"username":"felipejjorge"}
    ]
}

# Save 
with open('db.json', 'w') as file:
    
    json.dump(db, file)

    # convert python to a string
    # json_str = json.dumps(db)

    # print the string
    #print(json_str)

    # Write the string
    #file.write(json_str)

# Load the database
print("="*80)
with open('db.json', 'r') as file:
    json_str = json.load(file)
    # json_str = file.read()

    # print(json_str)

    # py_obj = json.loads(json_str)
