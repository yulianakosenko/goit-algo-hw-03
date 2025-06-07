import os
import shutil

# ТУТ ТВОЯ ВИХІДНА ДИРЕКТОРІЯ
src = r"C:\Users\yuliy\Documents\GitHub\goit-algo-hw-03"

# ТУТ ДИРЕКТОРІЯ ПРИЗНАЧЕННЯ (де буде dist)
dest = r"C:\Users\yuliy\Documents\GitHub\goit-algo-hw-03\dist"

def recursive_copy_and_sort(src_path, dest_path):
    try:
        for entry in os.listdir(src_path):
            full_path = os.path.join(src_path, entry)
            if os.path.isdir(full_path):
                # рекурсивно опрацьовуємо підкаталоги
                recursive_copy_and_sort(full_path, dest_path)
            elif os.path.isfile(full_path):
                # визначаємо розширення файлу
                ext = os.path.splitext(entry)[1][1:]  # без крапки
                if not ext:
                    ext = 'no_extension'
                # створюємо підпапку для розширення
                ext_folder = os.path.join(dest_path, ext)
                os.makedirs(ext_folder, exist_ok=True)
                # копіюємо файл
                shutil.copy2(full_path, ext_folder)
                print(f"Скопійовано файл {full_path} -> {ext_folder}")
    except Exception as e:
        print(f"Помилка при обробці {src_path}: {e}")

if __name__ == "__main__":
    print(f"Вихідна директорія: {src}")
    print(f"Директорія призначення: {dest}")
    recursive_copy_and_sort(src, dest)
    print("✅ Завдання завершено.")
