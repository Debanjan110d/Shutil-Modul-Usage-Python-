import shutil

# Get disk usage statistics
path = '/'  # The path to check disk usage

# Use shutil.disk_usage() to get the usage statistics
total, used, free = shutil.disk_usage(path)

print(f"Total: {total} bytes")
print(f"Used: {used} bytes")
print(f"Free: {free} bytes")