# -*- coding: utf-8 -*- 
#1.	Напишите скрипт, читающий во всех mp3-файлах указанной 
#директории ID3v1-теги и выводящий информацию о каждом файле 
#в виде: [имя исполнителя] - [название трека] - [название альбома]. 
#Если пользователь при вызове скрипта задает ключ -d, то выведите 
#для каждого файла также 16-ричный дамп тега. Скрипт должен также 
#автоматически проставить номера треков и жанр (номер жанра задается 
#в параметре командной строки), если они не проставлены. Используйте 
#модуль struct. ID3v1-заголовки располагаются в последних 128 байтах 
#mp3-файла. Структура заголовка отражена в табл. 2. 
import os

class structuraid3(object):
    def __init__(self,path,bit):
        self.__path_list = os.listdir(path)
        self.__path = path
        self.__bit = bit
        
    def decodingMp3(self):
        self.mass = [self.__path+ "\\" + x for x in self.__path_list]
        for x in self.mass:
            with open(x, 'rb') as f:
                header = f.read(self.__bit)
                print(header.decode())
                
                
path = r'C:\Users\dom\Desktop\laba_4\laba_4_1\music'
key_d = input('Введите ключ(Если ключа нету нажмите enter):')
if key_d == '-d':
    g = structuraid3(path,16)
    g.decodingMp3()
else:
    g = structuraid3(path,30)
    g.decodingMp3()





