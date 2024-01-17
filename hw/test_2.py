import json
from datetime import datetime

def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            data = file.read()
            if data:
                notes = json.loads(data)
            else:
                notes = []
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)

def filter_notes_by_date(notes, start_date, end_date):
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")

    filtered_notes = [note for note in notes if start_datetime <= datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S") <= end_datetime]

    return filtered_notes

def display_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Timestamp: {note['timestamp']}")
    print()

def add_note(notes, title, body):
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.\n")

def edit_note(notes, note_id, title, body):
    for note in notes:
        if note['id'] == note_id:
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка изменена.\n")
            return
    print("Заметка с указанным ID не найдена.\n")

def delete_note(notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.\n")
            return
    print("Заметка с указанным ID не найдена.\n")

all_notes = load_notes()

while True:
    print("1. Показать все заметки")
    print("2. Добавить заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выход")

    choice = input("Выберите действие (введите номер): ")

    if choice == '1':
        display_notes(all_notes)
    elif choice == '2':
        title = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        add_note(all_notes, title, body)
    elif choice == '3':
        note_id = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новый текст заметки: ")
        edit_note(all_notes, note_id, title, body)
    elif choice == '4':
        note_id = int(input("Введите ID заметки для удаления: "))
        delete_note(all_notes, note_id)
    elif choice == '5':
        break
    else:
        print("Некорректный ввод. Попробуйте ещё раз.")