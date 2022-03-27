#ex1

#ex2
import statistics
import requests
import matplotlib.pyplot as plot
r = requests.get('https://raw.githubusercontent.com/dm-fedorov/python3_intro/master/lesson_10/temper.stat')
a=r.text.split()
a = list(map(float, a))
s= statistics.mean(a)
print("Максимум:",min(a),"Минимум:",max(a),"Среднее:",s)
def unic(a):
    list_unic=[]
    new_a=set(a)
    for num in new_a:
        list_unic.append(num)
    return list_unic
print ("Кол-во уникальных температур:",len(unic(a)))
x=range(1, len(a)+1)
plot.plot(x,a)
plot.show()
