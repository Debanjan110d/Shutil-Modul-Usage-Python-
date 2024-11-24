import shutil

# Extract a zip archive
zip_file_to_extract = 'example_directory.zip'  # The zip file to extract
extract_to_directory = 'extracted_directory'  # Directory to extract to

# Use shutil.unpack_archive() to extract the zip file
shutil.unpack_archive(zip_file_to_extract, extract_to_directory)

print(f"Extracted {zip_file_to_extract} to {extract_to_directory}")