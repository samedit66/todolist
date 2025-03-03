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

def edit_task():
    index=input("Введите номер")
    new_title=input("Введите новый заголовок")
    new_desc=input("Введите описание для задач")
    
    if index=='' or new_title=='' or new_desc=='':
        print("Введите полностью edit")

    f=open("task.txt", 'r')
    a=[]
    oke=f.readlines()
    for ok in oke:
        if index==oke[ok]:
            a.append(new_title,new_desc)
   
    

print("Приложение для добавления, удаления и изменения заметок.")

exit = False

while exit != True:
    print("Что вы хотите сделать?")
    answer = input("> ")

    
    if answer == "exit":
        print("Вы закончили работу программы")
        exit = True
    elif answer=="edit":
        edit_task()



        
     