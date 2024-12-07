import os

def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Каталог '{directory}' не найден.")
    
    files = [f for f in os.listdir(directory) if f.endswith(old_extension)]

    if not files:
        print("Файлы с указанным расширением не найдены.")
        return
    
    format_string = f"{{:0{num_digits}d}}"

    for index, file_name in enumerate(files, start=1):
        base_name = os.path.splitext(file_name) [0]

        if name_range:
            start, end = name_range
            extracted_name = base_name[start-1:end]
        else:
            extracted_name = base_name

        new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"

        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)

        os.rename(old_file_path, new_file_path)
        print(f"Переименован '{file_name}' в '{new_file_name}'")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 6:
        print("Usage: python file_rename.py <directory> <final_name> <num_digits> <old_extension> <new_extension>")
        sys.exit(1)

    directory = sys.argv[1]
    final_name = sys.argv[2]
    num_digits = int(sys.argv[3])
    old_extension = sys.argv[4]
    new_extension = sys.argv[5]

    name_range = [3, 6]

    batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range)

    