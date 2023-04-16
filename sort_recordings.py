import os
import shutil
from datetime import datetime

# Change the path to the directory where the files are located
directory_path = "/Surveillance"

# Get a list of all the files in the directory
file_list = os.listdir(directory_path)

# Count the number of .jpg files in the directory
jpg_count = 0
for file_name in file_list:
    if file_name.endswith(".jpg"):
        jpg_count += 1

if jpg_count > 10:
    # Get a list of all the files in the directory
    file_list = os.listdir(directory_path)

    # Loop through each file in the list
    for file_name in file_list:
        try:
            # Extract the date and hour from the file name
            filename_without_extension = file_name.rstrip(".jpg")
            file_name_parts = filename_without_extension.rsplit("_", 1)
            date_str = file_name_parts[0]
            hour_str = file_name_parts[1] if len(file_name_parts) > 1 else ""

            # Split the date and time strings into their component parts
            year, month, day = date_str.split("-")
            hour, minute, second, microseconds = hour_str.split("-")
            hour_string = str(hour)

            # Create the directory path for the day and hour
            day_path = os.path.join(directory_path, date_str)
            hour_path = os.path.join(day_path, hour_string)

            # Create the day and hour directories if they don't exist
            os.makedirs(hour_path, exist_ok=True)

            # Move the file to the hour directory
            file_path = os.path.join(directory_path, file_name)
            new_file_path = os.path.join(hour_path, file_name)
            shutil.move(file_path, new_file_path)
        except ValueError:
            # Skip files that do not match the expected format
            print("Skipping file {} because it does not match the expected format.".format(file_name))
