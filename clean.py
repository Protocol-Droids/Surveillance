import os

# get the current directory
dir_path = os.getcwd()

# get a list of all files in the directory
file_list = os.listdir(dir_path)

# iterate over the files and delete all JPG files
for file_name in file_list:
    if file_name.endswith(".jpg"):
        os.remove(os.path.join(dir_path, file_name))

print("All JPG files deleted")
