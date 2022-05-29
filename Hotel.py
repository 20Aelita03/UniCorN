class Hotel:
#словарь для хранения различных типов номеров + стоимость
     def __init__(self, num_rooms,stoim):
        self._rooms =  {'SGL': [[0 for _ in range(num_rooms[0])],stoim[0]],
                        'DBL': [[0 for _ in range(num_rooms[1])],stoim[1]],
                        'Junior Suite': [[0 for _ in range(num_rooms[2])],stoim[2]],
                        'Suite': [[0 for _ in range(num_rooms[3])],stoim[3]]}
# метод для бронирования номера по уникальному значению в списке

     def occypy(self, t, room_id):
        if self._rooms[t][0][room_id]==0:
            self._rooms[t][0][room_id] = 1  # бронируем номер
        else:
            raise RuntimeError("Номер занят")
        
# метод для освобождения номера по уникальному значению в списке
     def free(self,t, room_id):
         self._rooms[t][0][room_id] = 0  # освобождаем номер
              
# метод __str__ для красивой печати списка номеров
     def __str__(self):
        a = ''
        for i in self._rooms:
            for r in range(len(self._rooms[i][0])):
                if self._rooms[i][0][r]==0:
                    a+='Номер '+ i+"№"+ str(r+1) + " свободен\n"
                else:
                    a+='Номер '+ i+"№"+ str(r+1) + " занят\n"
        return a

# метод, который занимает все свободные номера в отеле
     def all_occypy(self):
          for i in self._rooms:
              for r in range(len(self._rooms[i][0])):
                  self._rooms[i][0][r] = 1

# метод, который возвращает долю занятых номеров
     def occupy_rate(self):
          summa= 0
          count= 0
          for i in self._rooms:
              summa+=sum(self._rooms[i][0])
              count+=len(self._rooms[i][0])*100
          fin=round(summa*100/count,2)
          return f"{fin} %"
          
# метод, который освобождает все занятые номера отеля
     def all_free(self):
          for i in self._rooms:
              for r in range(len(self._rooms[i][0])):
                  self._rooms[i][0][r] = 0

# метод, который возвращает выручку, исходя из занятости комнат
     def revenue(self):
          summa = 0
          for i in self._rooms:
              summa+= sum(self._rooms[i][0])*self._rooms[i][1]
          return f"revenue{summa}"
hotel = Hotel([1,2,1,3],[4,5,4,3])
print(hotel._rooms) 
hotel.occypy('SGL',0)
print(hotel._rooms)
print(hotel)
hotel.all_occypy()
print(hotel)
hotel.free('DBL',1)
print(hotel._rooms)
print(hotel.occupy_rate())
print(hotel.revenue())
