import shutil

# Create a zip archive from a directory
directory_to_zip = 'example_directory'  # The directory to zip
zip_file_name = 'example_directory.zip'  # The name of the zip file

# Use shutil.make_archive() to create a zip archive
shutil.make_archive(zip_file_name[:-4], 'zip', directory_to_zip)

print(f"Created zip archive {zip_file_name} from {directory_to_zip}")