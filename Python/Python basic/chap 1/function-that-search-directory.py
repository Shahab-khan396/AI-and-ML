import os

# Specify the directory path
directory_path = '.'  # Change this to the directory you want to list

try:
    # Get the list of files and directories in the specified directory
    entries = os.listdir(directory_path)
    
    # Print each entry
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access the directory '{directory_path}'.")
