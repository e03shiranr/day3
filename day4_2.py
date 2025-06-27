import os
new_folder_name = "my_new"
try:
    os.mkdir(new_folder_name)
    print(f"Directory {new_folder_name} created successfully")
except FileExistsError:
    print(f"Directory {new_folder_name} already exists.")
except Exception as e:
    print(f"An error occured: {e}")
