#Number1
students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня":10}
for item in students:
    print(item,grades.get(item,"Контрольную работу не писал"))
for item in grades:
    if grades[item]>=8:
        print(item)
print(grades)
good=[]
bad=[]
norating=[]
for item in students:
    if item in grades:
        if grades[item]>5:
            good.append(item)
        else:
            bad.append(item)
    else:
        norating.append(item)
print(f"Хорошие и отличные оценки{good}:")
print(f"Плохие оценки:{bad}")
print(f"Не получили оценок:{norating}")
#Number2
