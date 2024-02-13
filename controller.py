
import func

if not func.check_file_existence():
    func.create_date()

while True:
    action_input = input('''
        Какое действие Вы хотите произвести?
        Введите соответствующую цифру.
        1 - Просмотр заметок
        2 - Добавление заметки
        3 - Поиск заметки
        4 - Изменение заметки
        5 - Удаление заметки
        0 - Выход
    ''')

    try:
        action = int(action_input)
    except ValueError:
        print("Введите корректное число.")
        continue

    if action == 1:
        func.open_date()
        
    elif action == 2:
        func.add_date()
        
    elif action == 3:
        func.search_date()
    
    elif action == 4:
        func.edit_date()
    
    elif action == 5:
        func.delete_date()    
        
    elif action == 0:
        print("Выход из программы.")
        break
    else:
        print("Введите корректное число из списка.")
