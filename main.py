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

    def done(number_of_note):

        file = open("tasks.txt", "r", encoding="utf8")
        list_of_tasks = file.readlines()

        for i in range(0, len(tasks.txt)):

            if i[0] == number_of_note:
                list_of_found_note = 

            else:
                print("Номер строчки, которой вы ввели не существует")
    