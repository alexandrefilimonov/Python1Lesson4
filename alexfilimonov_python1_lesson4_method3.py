#C:\Users\CA32132\AppData\Local\Programs\Python\Python37\python.exe C:\alex\_________________________________________________NewCode\_Python1Lesson4\alexfilimonov_python1_lesson4_method3.py 
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from random import *
i=0 
n=2500 
numb0=""
while (i<n) :
    numb0+=str(randint(0,9))
    i+=1
#print(numb)

fw = open("testfile.txt", "w") 
fw.write(numb0) 
fw.close()
fr = open("testfile.txt", "r")
numb=fr.read() 

k=1
max=0
ch=numb[0]
outstring=""
for i in range(1,n):
    if (ch==numb[i]) : 
        k+=1
    else : 
        if (k>max) :
            max=k
            outstring=(str(ch)*k)
        k=1
        ch=numb[i]

if (k>max) :
    max=k
fr.close()
print('Max string is ', outstring);


