import os
path1 = "C://day3"
path2 = "tmp"
path3 = "non_existent_path.txt"

patht = os.path.join(path1, path2, path3)
print(f"{patht}")