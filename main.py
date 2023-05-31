import json
import os
from datetime import datetime, timedelta

# Function to read the JSON file and return the data as a Python object
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to write the data to the JSON file
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to edit a specific field in the JSON data
def edit_json_entry(file_path, field, new_value):
    data = read_json_file(file_path)
    if field in data["nruPromotion"][0]:
        data["nruPromotion"][0][field] = new_value
        write_json_file(file_path, data)
        print("Field '{}' updated successfully.".format(field))
    elif field in data["nruPromotion"][1]:
        data["nruPromotion"][1][field] = new_value
        write_json_file(file_path, data)
        print("Field '{}' updated successfully.".format(field))
    else:
        print("Field '{}' not found.".format(field))

# Get the current directory
current_directory = os.getcwd()

# Set the JSON file path
file_path = os.path.join(current_directory, 'sample.json')

# Read the JSON file
json_data = read_json_file(file_path)
print("Original JSON data:")
print(json_data)

# Edit the fields

# Prompt for the new title
new_title = input("Enter the new title: ")
# Update the title field
edit_json_entry(file_path, 'title', new_title)

# Prompt for the new body text
new_body_text = input("Enter the new body text: ")
# Update the bodyText field
edit_json_entry(file_path, 'bodyText', str(new_body_text))


# Get the current datetime
current_datetime = datetime.now()
# Format the start date as year month day hour minute second
new_start_date = current_datetime.strftime("%Y %m %d %H %M %S")
# Get the start date epoch in seconds
new_start_epoch = int(current_datetime.timestamp())
# Update the startDate field
edit_json_entry(file_path, 'startDate', str(new_start_epoch))

# Calculate the end date as 3 days from the current datetime
new_end_datetime = current_datetime + timedelta(days=3)
# Format the end date as year month day hour minute second
new_end_date = new_end_datetime.strftime("%Y %m %d %H %M %S")
# Get the end date epoch in seconds
new_end_epoch = int(new_end_datetime.timestamp())
# Update the endDate field
edit_json_entry(file_path, 'endDate', str(new_end_epoch))

# Get the current datetime for last modified time
new_last_modified_time = datetime.now()
# Get the last modified time epoch in seconds
new_last_modified_epoch = new_last_modified_time.timestamp()
# Update the lastModifiedTime field
edit_json_entry(file_path, 'lastModifiedTime', str(new_last_modified_epoch))


# Prompt for the new ID
new_id = input("Enter the new ID: ")
# Update the id field
edit_json_entry(file_path, 'id', str(new_id))


# Prompt for the new promotion name
new_promotion_name = input("Enter the new promotion name: ")
# Update the promotionName field
edit_json_entry(file_path, 'promotionName', str(new_promotion_name))


# Read the updated JSON file
json_data = read_json_file(file_path)
print("\nUpdated JSON data:")
print(json_data)
