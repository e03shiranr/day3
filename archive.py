import shutil
import os

data_folder = "my_data_for_archieve"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "important.txt"), "w") as f:
    f.write("Important data here")
with open(os.path.join(data_folder, "docs, ""notes.md"), "w") as f:
    f.write("#meeting notes")
print(f"Created dummy folder for archieving : {data_folder} .")


archieve_name = "my_data_archieve"
try:
    archieve_path = shutil.make_archive(archieve_name, 'zip', root_dir=data_folder)
    print(f"Archieve Created: {archieve_path}")
    print(f"Does archieve exists? {os.path.exists(archieve_path)}")

except Exception as e:
    print(f"An error Ocurred during archieving : {e}")
    


