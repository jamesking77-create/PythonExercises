from pathlib import Path

new_file = Path.cwd() / "future_dates.py"
new_file.touch()
print(new_file.exists())