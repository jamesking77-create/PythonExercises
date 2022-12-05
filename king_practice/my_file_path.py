from pathlib import Path

my_file_path = Path.home() / "my_folder"
new_file_path = my_file_path / "my_file.txt"
new_file_path.touch()
latest_file = my_file_path / "my_files.py"
latest_file.touch()
print(my_file_path.exists())
print(new_file_path.is_file())
print(new_file_path.parent.name)
print(new_file_path.suffix)
print(new_file_path.stem)