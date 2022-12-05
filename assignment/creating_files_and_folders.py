from pathlib import Path
my_file = Path.cwd() / "positive_and_negative.py"
my_file.touch()
print(my_file)
print(my_file.exists())
