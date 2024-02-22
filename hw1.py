import os
import shutil
import argparse

def parse_args():
    # Створення парсера аргументів
    parser = argparse.ArgumentParser(description="Копіює файли з однієї директорії до іншої, сортуючи їх за розширенням.")
    
    # Додавання аргументу для шляху до вихідної директорії
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії")
    
    # Додавання аргументу для шляху до директорії призначення зі значенням за замовчуванням
    parser.add_argument("destination", type=str, nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    
    return parser.parse_args()

def copy_files_recursively(src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        if os.path.isdir(s):
            copy_files_recursively(s, dest)  # Рекурсивний виклик для піддиректорій
        else:
            file_extension = os.path.splitext(item)[1].replace('.', '') or 'no_extension'
            dest_subfolder = os.path.join(dest, file_extension)
            if not os.path.exists(dest_subfolder):
                os.makedirs(dest_subfolder)
            shutil.copy2(s, dest_subfolder)  # Копіювання файлу

def main():
    args = parse_args()
    
    source_dir = args.source
    destination_dir = args.destination
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    try:
        copy_files_recursively(source_dir, destination_dir)
        print("Файли було успішно скопійовано та відсортовано.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()
