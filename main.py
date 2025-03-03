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


print("Приложение для добавления, удаления и изменения заметок.")

exit = False

while exit != True:
    print("Что вы хотите сделать?")
    answer = input("> ")

    
    if answer == "exit":
        print("Вы закончили работу программы")
        exit = True



def search(mtrx):
    search_word = input("введите слово для поиски")
    has_found = []
    

    for row  in mtrx:
      for value in row:
        if mtrx[row][value] == search_word:
           has_found.append(mtrx[row])
    print(f'по вашему запросу найдено: \n {has_found}')
    return search_word,has_found
