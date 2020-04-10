#4.	Напишите простой класс StringFormatter для форматирования строк со следующим функционалом: 
#–	удаление всех слов из строки, длина которых меньше n букв; 
#–	замена всех цифр в строке на знак «*»; 
#–	вставка по одному пробелу между всеми символами в строке; 
#–	сортировка слов по размеру; 
#–	сортировка слов в лексикографическом порядке. 
import re
class StringFormatter(object):

    def __init__(self, line, n):
        self.__line = line
        self.__n = n

    #–	удаление всех слов из строки, длина которых меньше n букв; 
    def deleting_words(self):
        return [x for x in self.__line.split() if len(x) > 6]

    #–	замена всех цифр в строке на знак «*»; 
    def replacing_digits(self):
        return [re.sub(r'\d', '*', x) for x in self.__line.split()]

    #–	вставка по одному пробелу между всеми символами в строке; 
    def split_spaces(self):
        return [' '.join(x) for x in self.__line.split()]

    #–	сортировка слов по размеру; 
    def sort_size(self):
        return sorted(self.__line.split(), key = len)

    #–	сортировка слов в лексикографическом порядке. 
    def sort_lexicographic(self):
        return ' '.join(sorted(self.__line.split()))


s = StringFormatter("сортир41овка слов по разме14ру", 5)

print(s.deleting_words())
print(s.replacing_digits())
print(s.split_spaces())
print(s.sort_size())
print(s.sort_lexicographic())