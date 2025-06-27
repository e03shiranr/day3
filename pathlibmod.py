import pathlib
import os


print("\n 1. Creating Path Objects----")
print(pathlib.Path)
current_dir = pathlib.Path.cwd()
print(f"Current Working directory (path Object): {current_dir}")

relative_file = pathlib.Path('my_document.txt')
print(f"Relative file path: {relative_file}")

joined_path = current_dir / 'data' / 'reports' / 'report.csv'
print(f"Joined path using / operator: {joined_path}")

print("\n --- 2. Accesing path Components---")

print(f"Full path: {joined_path}")
print(f"File/Folder name : {joined_path.name}")
print(f"Parent Directory : {joined_path.parent}")
print(f"File System name without Suffix : {joined_path.stem}")
print(f"File sufix : {joined_path.suffix}")
print(f"All sufix : {joined_path.suffixes}")
print(f"Anchor (root of the path) : {joined_path.anchor}")
print(f"Path Parts : {joined_path.parts}")


