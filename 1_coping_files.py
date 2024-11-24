import shutil

# Copy a single file from source to destination
source_file = 'example.txt'  # The file you want to copy
destination_file = 'copy_of_example.txt'  # The destination path

try:
    # Use shutil.copy() to copy the file
    shutil.copy(source_file, destination_file)
    print(f"Copied {source_file} to {destination_file}")
except FileNotFoundError:
    print(f"File {source_file} not found.")
except PermissionError:
    print(f"Permission denied while copying {source_file} to {destination_file}.")
except Exception as e:
    print(f"An error occurred: {e}")
