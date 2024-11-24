import shutil

# Copy an entire directory
source_dir = 'example_directory'  # The directory you want to copy
destination_dir = 'copy_of_example_directory'  # The destination path

# Use shutil.copytree() to copy the directory
shutil.copytree(source_dir, destination_dir)

print(f"Copied directory {source_dir} to {destination_dir}")