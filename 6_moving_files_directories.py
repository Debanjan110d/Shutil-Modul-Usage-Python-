import shutil

# Move a file or directory
file_to_move = 'copy_of_example.txt'  # File to move
new_location = 'moved_example.txt'  # New location for the file

# Use shutil.move() to move the file
shutil.move(file_to_move, new_location)

print(f"Moved {file_to_move} to {new_location}")