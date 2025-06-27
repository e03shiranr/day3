import os
file_to_remove = "my_new.txt"

with open(file_to_remove, 'w') as f:
    f.write("This is temporary file")

try:
    os.remove(file_to_remove)
    print(f"file {file_to_remove} removed successfully." )

except FileNotFoundError:
    print(f"File {file_to_remove} does not exist")
except OSError as e:
    print(f"Error removing file{file_to_remove} : {e}")