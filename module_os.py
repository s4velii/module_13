import os
import time

directory = os.getcwd()

for root, dirs, files in os.walk(directory):
    print(files)
    for file in files:
        filepath = os.path.join(root)
        filetime = os.path.getatime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(root)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



