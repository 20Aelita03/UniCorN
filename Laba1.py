documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
def p(num:str)->None:
    for item in documents:
        if item['number'] == num:
            print(item['name'])
            break
    else:
            print("Документ не найден в базе")
print(p(input()))
            

  
def s(num:str)-> str:
    for item in directories:
        if num in directories[item]:
            print(item)
            break
print(s(input()))

def l()-> None:
    for item in documents:
        print(
            f"№ {item['number']},тип:{item['type']},владелец:{item['name']}, полка хранения:{s(item['number'])}")
print(l())
  
  
def ads(num:str)->None:
    if num in directories.keys():
        print("Такая полка уже существует")
    directories[num]=[]
    print("Полка добавлена")
print(ads(input()))


