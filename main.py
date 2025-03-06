from pathlib import Path
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
        text = f.readlines()

        try:
            num = str(int(text[-1].split('|')[0])+1)
        except:
            num = '1'

        status = 'не сделано'
        f.write(f'{num}|{title}|{description}|{status}\n')

        print('сохранено\n')

def list_tasks():
    print('список всех задач:')

    with open('tasks.txt', 'r', encoding='utf-8') as f:

        for e in f.readlines():
            print(e.replace('|', ', ')[:-1])
        print()


print("Приложение для добавления, удаления и изменения заметок.")

exit = False

while exit != True:
    print("Что вы хотите сделать?")
    answer = input("> ")

    
    if answer == "exit":
        print("Вы закончили работу программы")
        exit = True
    
    elif answer == 'list':
        list_tasks()
    
    elif answer == 'add':
        add_task(input('введите заголовок: '), input('введите обозначение: '))

def search(mtrx):
    a = open('tasks.txt','r',encoding='utf-8')
    mtrx = a.readlines()
    search_word = input("введите слово для поиска ")
    has_found = []
    

    for row  in mtrx:
      for value in row:
        if mtrx[row][value] == search_word:
           has_found.append(mtrx[row])
    print(f'по вашему запросу найдено: \n {has_found}')
    return search_word,has_found
   

def check_file_exists(file_path):
    
    path = Path(file_path)
    
    return path.is_file()