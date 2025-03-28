import os

# Specify the directory path
directory = '/Python'

try:
    # List all files and directories in the specified path
    entries = os.listdir(directory)
    print(f"Contents of '{directory}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied for accessing '{directory}'.")
