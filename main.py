"""
Пример работы:
Приложение для управления задачами.

Что вы хотите сделать? help list
Команда list нужна для того, чтобы посмотреть
список всех задач.

Что вы хотите сделать? add
Какой заголовок? Сходить в магазин
Какое описание? Купить молоко
Задач создана, еще не сделана

Что вы хотите сделать? list
1,Сходить в магазин,Купить молоко,Не сделано
"""

def add_task(title, description):
    with open('tasks.txt', 'r+', encoding='utf-8') as f:
        text = f.read()
        
        num = f.readline(-1).split(',')[0] if text != '' else '1'
        f.write(f'{num},{title},{description},не сделано')


print("Приложение для добавления, удаления и изменения заметок.")

exit = False

while exit != True:
    print("Что вы хотите сделать?")
    answer = input("> ")

    
    if answer == "exit":
        print("Вы закончили работу программы")
        exit = True
        