import os
path_to_check_file = "C://day3/my_existing_file.txt"
path_to_check_dir = "C://day3"
with open(path_to_check_file, 'w') as f:
    f.write("Hello")
os.makedirs(path_to_check_dir, exist_ok=True)