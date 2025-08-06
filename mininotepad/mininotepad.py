import os

notes_folder = "notes"

os.makedirs(notes_folder, exist_ok=True)

def create_note():
    title = input("введите название файла: ")
    content = input("введите текст заметки: ")
    file_path = os.path.join(notes_folder, f"{title}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Заметка '{title}' сохранена!")

def show_notes():
    files = os.listdir(notes_folder)
    if not files:
        print("нет сохраненных заметок.")
        return
    for filename in files:
        file_path = os.path.join(notes_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"\n📄 {filename.replace('.txt','')}:")
        print(content)

while True:
    print("\n1. создать заметку")
    print("2. показать все заметки")
    print("3. выйти")

    choice = input("выбери действие: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        break
    else:
        print("Неверный выбор, попробуйте снова")