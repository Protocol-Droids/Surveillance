import os
import zipfile

def create_zip_archive(zip_file_name='images.zip'):
    # get the current working directory
    current_dir = os.getcwd()

    # get a list of all the JPG files in the current directory
    jpg_files = [filename for filename in os.listdir(current_dir) if filename.endswith('.jpg')]

    # create a new ZIP archive
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # add each JPG file to the archive
        for jpg_file in jpg_files:
            zip_file.write(jpg_file)

    print('Created ZIP archive: {}'.format(zip_file_name))

if __name__ == '__main__':
    create_zip_archive()