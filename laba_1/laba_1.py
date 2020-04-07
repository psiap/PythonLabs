##1

try:
 count = float(input("Введите сумму: "))
 cop = (count - int(count)) * 100 
 print(int(count)," руб.", int(cop), " коп.")
except ZeroDivisionError:
 print("Некорректрый формат!")

##2
def test(x):
    n = len(x)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if x[j] > x[j+1]:
                return "False"
    return "True"

a = input ("Введите последовательность цифр:\n")
if a.replace(' ','').isdigit() == True:
    a = a.split(" ")
    print(test(a))



##3
cart = input("Введите карту: ")
if cart.replace(' ','').isdigit() == True and len(cart) == 19:
    print(cart[0:4],'*'*4,'*'*4,cart[15:19])
else:
    print("False")

##4
str = input("Введите текст: ")
print([x for x in str.split() if len(x) > 7])
print([x for x in str.split() if len(x) <= 7 and len(x) >= 4])
print([x for x in str.split() if len(x) < 4])

##5
str = input("Введите строку: ")
print([x.upper() for x in str.replace(',',' ').split(' ') if x == x.title()])
print(str)
            

##6
mass = list(input("Введи текст\n"))
print("".join([i for i in mass if mass.count(i)==1]))

##7
str = ('www.mail.ru','google.com','www.gmail')
print([x.replace('www.','http://') + x.replace('.'[x.find('.')::],'.com') for x in str if x.find('www') == 0])
##8
from random import randint
array = [random.randint(0,100) for i in range(0,random.randint(0,10000))]
print("Было элементов",len(array))
[array.append(random.randint(0,100)) for i in range(len(array),2**math.ceil(math.log2(len(array))))]
print("Стало элементов",len(array))


##9
money = {1000:1,500:10,100:10,50:10,10:1}
user = int(input("Введите сумму: "))
if money[1000]*1000+money[500]*500+money[100]*100+money[50]*50+money[10]*10 < user:
   print("В банкомате нет столько денег")
   return 0
[print("Было ",mul,":",money[mul],"Стало",mul,":",money[mul]-i) for i, mul in Ex9_Generator(money,user)]


##10
a = input("Введите пароль: ")
count = 0
if len(a) > 6:
    print('+')
    count += 1
if a.isdigit() == False:
    print('+')
    count += 1
if a.isalpha() == False:
   print('+')
   count += 1
if a.isupper() == False:
    count += 1
    print('+')
if a.islower() == False:
    count += 1
    print('+')
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
if len(a) == len(b):
    count += 1
    print('+')

if count == 6:
    print("Пароль ВЕРИ ГУД", count)
elif count > 4 and 6 > count:
    print("Где-то между", count)
else:
    print("Не, надо придумать что-то круче",count)

##11
def frange(a,b,shag):
    c = a
    while c < b:
        yield c
        c += shag

for x in frange(1,5,0.4):
    print('%.1f' % x)
##12
[print(i) for i in get_frames(range(1,10),4,0.5)]

def get_frames(signal, size=4, overlap=0.5):
    for i in range(0, len(signal) - 1, int(size * overlap)):
        yield [x for x in signal[i : i + size] ]

##13
def extra_enumerate(x):
    i,elem,cum,frac = 0, 0, 0, 0
    for j in x:
        cum += j
        frac += j / 10
        yield j,j,cum,frac
    

 
x = [1,3,4,2]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem,cum,frac)


##14
def non_empty(fun):
    def wrapper(arg):
        for i, e in enumerate(arg):
            if e == '' or e == None:
                del arg[i]
        return fun(arg)
    return wrapper

@non_empty
def get_pages(x):
    print(x)
    return x


x = input('Введите строку: ')
get_pages(x.split(' '))

print(x)

##15
def Ex15():
    plot_signal([i for i in range(10)])
    
def pre_process(a=0.97):
    def decoratour(fn):
        def wrapper(s):
            return  fn([i-a*s[s.index(i)-1] for i in s])
        return wrapper
    return decoratour

@pre_process(a=0.93)
def plot_signal(s):
    [print(sample) for sample in s]

##16
def Ex16():
    now = datetime.datetime.now()
    start = datetime.datetime(now.year,9,14,22,45)
    teams = ["Англия","Португалия","Аргентина","Россия","Италия","Китай","Казахстан","Польша","Германия","Франция","Мадагаскар","Афганистан","Украина","Эстония","Канада","Тунис"]
    random.shuffle(teams)
    teams = [teams[i*4:i*4+4] for i in range(0,4)]
    groups = [i for i in itertools.combinations(teams, 4)]
    [print("Группа №",i+1,groups[0][i]) for i in range(0,4)]
    for i in range(1,16):
        print ("Игра #",i,start.strftime("%d/%m/%Y %H:%M"))
        start+=datetime.timedelta(days=14)

Const_NumExample = 16 #"Константа" 
