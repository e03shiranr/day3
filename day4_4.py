import os
folder_to_remove = "my_new"

try:
    os.rmdir(folder_to_remove)
    print(f"Directort {folder_to_remove} removed successfully." )
except OSError as e:
    print(f"Error removing Directory {folder_to_remove} : {e}")


