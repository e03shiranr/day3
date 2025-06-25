import os
new_directory = "/tmp"
if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"change directory to : {os.getcwd()}")
else:
    print(f"Directory {new_directory} does not exist or not a directory")
