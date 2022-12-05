
from pathlib import Path

file_path = Path.cwd() / "my_folder"
print("folder exist?",file_path.exists())
new_file = file_path / " my_file.txt"
new_file.touch()
print("new_file exist?", new_file.exists())
print(new_file.name)
print(new_file.parent.name)
# print(file_path.parent)
