
import time
import datetime

database = {}

def start(): # запросы
    name = input('название: ') 
    description = input('описанеи заказа: ')
    deadline = datetime.datetime(int(input('дедлайн(год): ')), 
                                int(input('месяц: ')), 
                                int(input('день: ')), 
                                int(input('час: ')), 
                                int(input('минута: ')))
    notification = int(input('частота уведомлений: '))
    database [name] = {
        'name': name,
        'description': description,
        'deadline': deadline,
        'notification': notification
        }
    print(f"Задача '{name}' создана с дедлайном {deadline}")

def calculator(datdbase_name, deadline, notification): # калькулятор 
    while True:
        now_time = datetime.datetime.now()
        time_left = deadline - now_time
        if now_time < deadline:
            print(f'время до конца {datdbase_name}:{time_left}')
        else:
            print('конец')
            break
        time.sleep(notification)

def delete_task(): # удалить 
    task_name = input("Введите название работы, которую хотите удалить: ")
    if task_name in database:
        del database[task_name]
        print("Задача успешно удалена!")
    else:
        print("Задача не найдена!")

def edit_task(): # изменить 
    task_name = input("Введите название работы, которую хотите изменить: ")
    if task_name in database:
        er = input('что вы хотите изменить: ')
        while True:
            
            if er == 'name': # имя
                new = input('новое имя')
                database[task_name]['name'] = new
                print("Задача успешно изменена!")
                break
            
            if er == 'description': # описанеи 
                new = input('новое описанеи')
                database[task_name]['description'] = new
                print("Задача успешно изменена!")
                break
            
            if er == 'deadline': # дедлайн
                new = datetime.datetime(int(input('дедлайн(год): ')), 
                                int(input('месяц: ')), 
                                int(input('день: ')), 
                                int(input('час: ')), 
                                int(input('минута: ')))
                database[task_name]['deadline'] = new
                print("Задача успешно изменена!")
                break
            
            if er == 'notification':
                new == input('новая частота уведомлений: ')
                database[task_name]['notification'] = new
                print("Задача успешно изменена!")
                break
            
            else:
                print("Задача не найдена!")
    else:
        print("Задача не найдена!")

def list_tasks(): # функция для вывода списка задач
    for task in database.values():
        print(f"Название: {task['name']}")
        print(f"Описание: {task['description']}")
        print(f"Дедлайн: {task['deadline']}")
        print(f"Частота уведомлений: {task['notification']}")
        print()

def database_list(): # функция для вывода списка задач
    for name, task in database.items():
        print(f"Задача: {task['name']}")
        print(f"Описание: {task['description']}")
        print(f"Дедлайн: {task['deadline']}")
        print(f"Частота уведомлений: {task['notification']}")
        print()

start()

for i, deadline in database.items():
    calculator(i, deadline['deadline'], deadline['notification'])

