import os
import shutil

source_file = "source_doc.txt"
with open(source_file, "w") as f:
    f.write("This is the original file content.")
print(f"Created {source_file} for copying")

destination_file = "copied_doc.txt"
try:
    shutil.copy(source_file, destination_file)
    print(f"{source_file} copied to {destination_file} succesfully")
    print(f"content of {destination_file} : {open(destination_file).read()}")


except FileNotFoundError:
    print(f" Eror Source File {source_file} does not exist.")
except Exception as e:
    print(f"An error Occurred : {e}")

if os.path.exists(source_file):
    os.remove(source_file)
if os.path.exists(destination_file):
    os.remove(destination_file)
print("Cleaned up the dummy files")

