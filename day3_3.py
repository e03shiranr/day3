import os
path1 = "C://day3/my_existing_file.txt"
path2 = "C://day3"
path3 = "non_existent_path"

print(f"{path1} is a file: {os.path.isfile(path1)}")
print(f"{path1} is a dir: {os.path.isdir(path1)}")

print(f"{path2} is a file: {os.path.isfile(path2)}")
print(f"{path2} is a dir: {os.path.isdir(path2)}")

print(f"{path3} is a file: {os.path.isfile(path3)}")
print(f"{path3} is a dir: {os.path.isdir(path3)}")