def new_student(last_name, name):
    strocks=[]
    student= last_name +'' + name
    with open('students.txt', 'r',encoding = 'utf8') as file:
        for strock in file:
            strocks.append(strock.strip())
    strocks.append(student)
    strocks.sort()
    with open('students.txt', 'r',encoding = 'utf8') as file:
        for strock in strocks:
            file.write(strock + '\n')




def seek_student(last_name, name = None):
    s = 0
    with open('students.txt', 'r', encoding = 'utf8') as file:
        for strock in file:
            if last_name in strock:
                s+=1
                if name == None:
                    print(strock)
                else:
                    print("Находится в группе")
        if k==0:
            print("Не в группе")


def replace(last_name, name, new_last_name = None, new_name = None):
     student = last_name + '' + name
     s = 0
     with open('students.txt', 'r', encoding = 'utf8') as file:
         strocks = file.readlines()
         for strock in strocks:
             if student in strock:
                 k+=1
         if k > 0:
             if new_last_name == None:
                 strocks.remove(student + '\n')
                 new_student = last_name +''+ new_name
                 strock.append(new_student +'\n')

             else:
                 strocks.remove(student +'\n')
                 if new_name ==None:
                     new_student = new_last_name + '' + name
                     srocks.append(new_student + '\n')
                 else:
                     new_student = new_last_name + '' + new_name
                     srocks.append(new_student + '\n')
             strocks.sort()
             with open('students.txt', 'r', encoding = 'utf8') as file:
                 for strock in strockes:
                     file.write(strock)
         else:
              print("Не в этой группе")




def del_student(last_name, name=None):
    k=0
    students=[]
    with open('students.txt', 'r', encoding = 'utf8') as file:
        strocks = file.readlines()
    if name!= None:
        k+=1
        student= last_name+ ''+ name
        with open('students.txt', 'r', encoding = 'utf8') as file:
           for strock in strocks:
               if strock!= student + '':
                   file.write(strock)
                   k=-1
    else:
        for strock in strocks:
            if last_name in strock:
                k+=1
                students.append(strock)
    if k==0:
        print("Не в группе")
    if k>1:
        print(students)
        name = input("Name:")
        return del_student(last_name, name)
    if k==1:
        with open('students.txt', 'r', encoding = 'utf8') as file:
            for strock in strocks:
                if not(last_name in strock):
                    file.write(strock)
                 

