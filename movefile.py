import os
import shutil

file_to_move = "report.pdf"
target_dir = "archieve"

with open(file_to_move, 'w') as f:
    f.write("content of the file")
os.makedirs(target_dir, exist_ok=True)
print(f"Craeted {file_to_move} and {target_dir}")

try:
    shutil.move(file_to_move, target_dir)
    print(f"{file_to_move} moved to {target_dir} successfully")
    print(f"New path: {os.path.join(target_dir, file_to_move)}")
except FileNotFoundError:
    print(f"{file_to_move} does not exist.")
except FileExistsError:
    print(f"{file_to_move} is already exist.")
except Exception as e:
    print(f"An error Occurred : {e}")

if os.path.exists(target_dir):
    shutil.rmtree(target_dir)
print("Cleaned up dumy irectory")