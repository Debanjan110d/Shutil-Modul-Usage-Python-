import shutil

# Remove an entire directory
dir_to_remove = 'copy_of_example_directory'  # The directory to remove

# Use shutil.rmtree() to remove the directory
shutil.rmtree(dir_to_remove)

print(f"Removed directory {dir_to_remove}")