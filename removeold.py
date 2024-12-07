import os

import time

def delete_old_files(directory, days_old):

    now = time.time()
    cutoff = now - (days_old * 86400)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_mod_time = os.path.getmtime(file_path)

            if file_mod_time < cutoff:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")

delete_old_files('/path/to/directory', 30)
