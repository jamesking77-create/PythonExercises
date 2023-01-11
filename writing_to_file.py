from pathlib import Path


def new_year_class_work():
    my_list = []
    file_paths = Path.cwd() / "new_year_folder"
    file_paths.mkdir(exist_ok=True)
    new_year_file = file_paths / "new_year_file.txt"
    new_year_file.touch(exist_ok=True)
    new_year_file.write_text("this is a boy")
    read_my_file = new_year_file.read_text()
    read_my_file = read_my_file.replace("boy", "girl")
    for words in read_my_file:
        my_list.append(words)
    return my_list


print(new_year_class_work())



