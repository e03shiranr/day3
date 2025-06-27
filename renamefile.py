import os
old_name = "old_file.txt"
new_name = "new_file.txt"

with open(old_name, 'w') as f:
    f.write("content of the old file")

try:
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} from {new_name}")
except FileNotFoundError:
    print(f"{old_name} does not exist.")
except FileExistsError:
    print(f"{new_name} is already exist.")
except Exception as e:
    print(f"An error Occurred : {e}")