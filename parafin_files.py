from pathlib import Path


def list_files(directory):
    """Параметр: каталог.
    Результат: список назв файлів у каталозі.
    """
    files = []

    for file in Path(directory).iterdir():
        if file.is_file():
            files.append(file.name)

    return files


def find_files(directory, substring):
    """Параметри: каталог і підрядок для пошуку.
    Результат: список назв файлів, які містять підрядок.
    """
    files = []

    for file in Path(directory).iterdir():
        if file.is_file() and substring in file.name:
            files.append(file.name)

    return files


def create_file(path, text):
    """Параметри: шлях до файлу і текст.
    Результат: шлях до створеного файлу.
    """
    Path(path).write_text(text, encoding="utf-8")
    return path


if __name__ == "__main__":
    print(list_files("."))
    print(find_files(".", "parafin"))
