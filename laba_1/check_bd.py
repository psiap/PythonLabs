
def checker(id):
    with open(r'C:\Users\nikita\PycharmProjects\pythonProject\data\bd_user.csv', 'r+', newline='') as file:
        bd_user = file.readlines()
        for i in bd_user:
            if str(id) == i.split(';')[0]:
                return True
        return False

def add_bd(array):
    with open(r'C:\Users\nikita\PycharmProjects\pythonProject\data\bd_user.csv', 'a+', newline='') as file:
        file.write(array +'\n')

def checker_fio(id):
    with open(r'C:\Users\nikita\PycharmProjects\pythonProject\data\bd_user.csv', 'r+', newline='') as file:
        bd_user = file.readlines()
        for i in bd_user:
            if str(id) == i.split(';')[0]:
                return i.split(';')[1]
        return "None"

def checker_em(id):
    with open(r'C:\Users\nikita\PycharmProjects\pythonProject\data\bd_user.csv', 'r+', newline='') as file:
        bd_user = file.readlines()
        for i in bd_user:
            if str(id) == i.split(';')[0]:
                return i.split(';')[2]
        return "None"

def checker_full_id():
    with open(r'C:\Users\nikita\PycharmProjects\pythonProject\data\bd_user.csv', 'r+', newline='') as file:
        bd_user = file.readlines()
        mass_id = []
        for i in bd_user:
            mass_id.append(str(i.split(';')[0]))
        return mass_id


