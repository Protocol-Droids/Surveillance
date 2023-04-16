import os
import shutil
from datetime import datetime

# Change the path to the directory where the files are located
directory_path = "/Surveillance"

# Get a list of all the files in the directory
file_list = os.listdir(directory_path)

# Loop through each file in the list
for file_name in file_list:
    try:
        # Extract the date and hour from the file name
        file_name_parts = file_name.rsplit("_", 1)
        date_str = file_name_parts[0]
        hour_str = file_name_parts[1]

        # Convert the date and hour strings to datetime objects
        date = datetime.strptime(date_str, "%Y-%m-%d")
        hour = datetime.strptime(hour_str, "%H-%M-%S-%f") if len(file_name_parts) > 1 else ""

        # Create the directory path for the day and hour
        day_path = os.path.join(directory_path, date_str)
        hour_path = os.path.join(day_path, hour_str)

        # Create the day and hour directories if they don't exist
        os.makedirs(hour_path, exist_ok=True)

        # Move the file to the hour directory
        file_path = os.path.join(directory_path, file_name)
        new_file_path = os.path.join(hour_path, file_name)
        shutil.move(file_path, new_file_path)
    except ValueError:
        # Skip files that do not match the expected format
        print("Skipping file {} because it does not match the expected format.".format(file_name))
