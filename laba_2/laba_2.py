##1
#1.Напишите скрипт, который читает текстовый файл и выводит символы в порядке убывания частоты 
#встречаемости в тексте. Регистр символа не имеет значения. Программа должна учитывать только буквенные 
#символы (символы пунктуации, цифры и служебные символы слудет игнорировать). Проверьте работу скрипта на 
#нескольких файлах с текстом на английском и русском языках, 
#сравните результаты с таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.
import re

file = open('myfile.txt','rt')
b = []
mas = []
for line in file:
    for i in line:
        b.append(i)

iter_mass = list(set(b))
a = len(list(set(b)))
for i in range(a):
    mas.append([])
    for j in range(1):
        mas[i].append(iter_mass[i])
        mas[i].append(b.count(iter_mass[i]))

mas.sort(key = lambda x: x[1], reverse=True)
print(mas)

for char_m, key_m in mas:
    math = re.search(r"[^..]",char_m)
    print(math[0] if math else 'Not found') 

##2
#2. Напишите скрипт, позволяющий искать в заданной директории и в ее подпапках 
#файлы-дубликаты на основе сравнения контрольных сумм (MD5). Файлы 
#могут иметь одинаковое содержимое, но отличаться именами. 
#Скрипт должен вывести группы имен обнаруженных файловдубликатов. 
import sys
import os
import hashlib

fileSliceLimitation = 5000000 #bytes

def getFileHashMD5(filename):
     retval = 0;
     filesize = os.path.getsize(filename)

     if filesize > fileSliceLimitation:
        with open(filename, 'rb') as fh:
          m = hashlib.md5()
          while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
          retval = m.hexdigest()

     else:
        retval = hashlib.md5(open(filename, 'rb').read()).hexdigest()

     return retval

searchdirpath = input("Type directory you wish to search: ") 
text_file = open('outPut.txt', 'w')
gener_h_md5 = []
for dirname, dirnames, filenames in os.walk(searchdirpath):
    # print path to all filenames.
    for filename in filenames:
        fullname = os.path.join(dirname, filename)
        h_md5 = getFileHashMD5 (fullname)
        print (h_md5 + " " + fullname)
        gener_h_md5.append(h_md5)
        text_file.write("\n" + h_md5 + " " + fullname)   
text_file.close()


text_file = open('outPut.txt', 'r')

myListOfHashes = text_file.read()

if h_md5 in myListOfHashes:
    print ('Match: ' + " " + fullname)


print("Повтор файлы:")
print([x for x in gener_h_md5 if gener_h_md5.count(x) > 1]) 

##3
#3Задан путь к директории с музыкальными файлами (в названии которых нет номеров
#,а только названия песен) и текстовый файл, 
#хранящий полный список песен с номерами и названиями в виде 
#строк формата «01. Freefall [6:12]». 
#Напишите скрипт, который корректирует имена файлов в директории
#на основе текста списка песен. 
import os

def replacefile(filename, listtext):
    temp_text = []
    for line in listtext:
        temp_text = line.split(' ')
        if filename in temp_text:
            os.renames('music/' + filename,'music/' + temp_text[0] + temp_text[1])

#os.renames('music/' + name,'music/Dabro1')

for lt in os.listdir('music'):
    file = open('music/myfile.txt','rt')
    replacefile(lt,file)

##4
##4
#Вариант 6: найдите все строки вида «x: type [N]», где type – это тип 
#(может принимать значение int, short или byte), 
#х – любое слово, N – любое положительное целое число. 
import re

def TestReg(lst,reg):
    for i in range(len(lst)):
        parser = re.search(reg,lst[i])
        count =0
        while parser!=None:
            yield i+1,parser.regs[0][0]+count+1,parser.group()
            count+=parser.regs[0][1]
            lst[i] = lst[i][parser.regs[0][1]:]
            parser = re.search(reg,lst[i])

lst = []
reg = "\w+[:]\s[isc]\w+[[]\d+[]]"
while True:
        t = input()
        if t == "":
            break
        else:
            lst.append(t)
            
[print("Строка,",i,"позиция",j,": найдено",res) for i, j, res in TestReg(lst,reg)]

##5
##5.	Введите с клавиатуры текст. Программно 
##найдите в нем и выведите отдельно все слова, 
##которые начинаются с большого латинского символа (от A до Z) и заканчиваются 
##2 или 4 цифрами, например «Petr93», «Johnny70», 
##«Service2002». Используйте регулярные выражения. 
import re
import subprocess
       

def TestReg(lst,reg):
    for i in range(len(lst)):
        parser = re.search(reg,lst[i])
        count =0
        while parser!=None:
            yield i+1,parser.regs[0][0]+count+1,parser.group()
            count+=parser.regs[0][1]
            lst[i] = lst[i][parser.regs[0][1]:]
            parser = re.search(reg,lst[i])
reg = "[A-ZА-ЯЁ][A-ZА-ЯЁa-zа-яё]+([0-9]{4}$|[0-9]{2}$)"
[print(res) for i, j, res in TestReg(input().split(),reg)]


##6
##6.	Напишите скрипт reorganize.py, который в директории --source создает две директории: Archive и Small. В первую директорию помещаются файлы с датой изменения, отличающейся от текущей даты на количество дней более параметра --days (т.е. относительно старые файлы). Во вторую – все файлы размером меньше параметра --size байт. Каждая директория должна создаваться только в случае, если найден хотя бы один файл, который должен быть в нее помещен. Пример вызова: 
subprocess.call("reorganize.py --source \"D:\\TestDir\" --days 2 --size 4096",shell=True)

def Ex7():
    subprocess.call("trackmix.py -s \"D:\\\" -d \"kek.mp3\" -f 15 -l --extended",shell=True)
