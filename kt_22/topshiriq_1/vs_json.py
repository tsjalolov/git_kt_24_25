import json

new_data = {'new_key': 'new_value'}

with open('data.json', 'r+') as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError:
        data = {}  # Initialize as an empty dict if file is empty or invalid
    print(data)
    # Update the data
    data.update(new_data)

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Write the updated data back to the file
    json.dump(data, file, indent=4)
