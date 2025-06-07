import os
import shutil
import argparse

def recursive_copy_and_sort(src_path, dest_path):
    try:
        for entry in os.listdir(src_path):
            full_path = os.path.join(src_path, entry)
            if os.path.isdir(full_path):
                # Рекурсивно обробляємо підкаталоги
                recursive_copy_and_sort(full_path, dest_path)
            elif os.path.isfile(full_path):
                # визначаємо розширення файлу та створюємо відповідну папку     
                ext = os.path.splitext(entry)[1][1:]
                if not ext:
                    ext = 'no_extension'
                # Створюємо папку для розширення
                ext_folder = os.path.join(dest_path, ext)
                os.makedirs(ext_folder, exist_ok=True)
                # Копіюємо файл 
                shutil.copy2(full_path, ext_folder)
                print(f"Скопійовано файл {full_path} -> {ext_folder}")
    except Exception as e:
        print(f"Помилка при обробці {src_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Сортування файлів за розширенням.")
    parser.add_argument("src", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням dist)")
    args = parser.parse_args()

    print(f"Вихідна директорія: {args.src}")
    print(f"Директорія призначення: {args.dest}")
    recursive_copy_and_sort(args.src, args.dest)
    print("✅ Завдання завершено.")
