import csv
from datetime import datetime


def check_file_existence():
    try:
        with open('date.csv', 'r', newline='', encoding='UTF-8'):
            return True
    except FileNotFoundError:
        return False

def create_date():
    '''Создаем файл с заголовками таблицы данных.
    '''
    with open('date.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'title', 'body', 'time'])



def add_date():
    '''Добавляем записку с программно сгенерированным id и временем.
    '''
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # Читаем файл, чтобы получить текущее количество записей
    with open('date.csv', 'r', newline='', encoding='UTF-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        lines = list(reader)

    # Получаем текущее количество записей в файле
    generated_id = len(lines)  if len(lines) > 0 else 0

    # Проверяем уникальность id
    while any(int(line[0]) == generated_id for line in lines):
        generated_id += 1

    date_list = [str(generated_id), input("Введите название записки: "), input("Введите тело записки: "), timestamp]

    with open('date.csv', 'a', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(date_list)  

def open_date():
    '''Открывает список заметок для просмотра.'''
    try:
        with open('date.csv', 'r', newline='', encoding='UTF-8') as file:
            for line in file:
                print(line.strip(';'))
    except FileNotFoundError:
        print("Файл 'date.csv' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")  



def search_date():
    search_id = input('Введите id для поиска записки: ')
    
    with open('date.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        headers = next(reader)

        found = False
        for row in reader:
            if search_id == row[0]:
                print(', '.join(row))
                found = True
                break
        
        if not found:
            print(f"Записка с id {search_id} не найдена.")




def edit_date():
    search_id = input('Введите id записки для редактирования: ')
    
    with open('date.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        headers = next(reader)

        rows = list(reader)
        
    found = False
    for i, row in enumerate(rows):
        if search_id == row[0]:
            new_title = input(f'Введите новое название для записки с id {search_id}: ')
            new_body = input(f'Введите новое тело для записки с id {search_id}: ')
            now = datetime.now()
            new_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            rows[i] = [search_id, new_title, new_body, new_timestamp]
            found = True
            break

    if not found:
        print(f"Записка с id {search_id} не найдена.")
        return
    
    with open('date.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

def delete_date():
    search_id = input('Введите id записки для удаления: ')

    with open('date.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        headers = next(reader)

        rows = list(reader)
    
    found = False
    for i, row in enumerate(rows):
        if search_id == row[0]:
            rows.pop(i)
            found = True
            print(f"Записка с id {search_id} удалена")
            break
    
    if not found:
        print(f"Записка с id {search_id} не найдена.")
        return
    
    with open('date.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        if len(rows) > 0:
            writer.writerows(rows)
        else:
            print("Последняя записка удалена.")




