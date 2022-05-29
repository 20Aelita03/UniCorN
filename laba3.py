def todo():
    import json
    print("Простой todo:")
    print("1. Добавить задачу.")
    print("2. Вывести список задач.")
    print("3. Выход.")
    num= int(input("Укажите число: "))
    while(num!=3):
        if num==1:
            task1= input("Сформулируйте задачу:")
            cat1= input("Добавьте категорию к задаче:")
            time = input("Добавьте время к задаче:")
            pri="""задача:{z} категория:{k} время:{t}"""
            one = pri.replace('{z}',task1)
            one = one.replace('{k}',cat1)
            one = one.replace('{t}',time)
            with open('todo.json', 'w') as file:
                json.dump(one,file)
        elif num==2:
            try:
                with open('todo.json')as file:
                    number=json.load(file)
                print(number)
            except Exception as ap:
                print(ap)
        else:
            print("WRONG")
        num=int(input("Укажите число:"))
    print("задачи сохранены в файл!")
