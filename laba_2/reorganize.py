import sys
import os
import time
import datetime
import shutil

def main(path=sys.path[0], days=2,size=4096):
    paths = [path+"\\"+"Archive",path+"\\"+"Small",path+"\\"]
    if os.path.isdir(path):
        flagA=False
        flagS=False
        if not os.path.isdir(paths[0]):
            flagA=True
        if not os.path.isdir(paths[1]):
            flagS=True
        files = os.listdir(path)
        data = datetime.datetime.today()
        for i in files:
            if os.path.isfile(paths[2]+i) and data-datetime.datetime.fromtimestamp(os.path.getmtime(paths[2]+i)) >= datetime.timedelta(days=days):
                if flagA:
                    os.mkdir(paths[0])
                    flagA=False
                shutil.copy(paths[2]+i,paths[0]+"\\"+i)
            if os.path.isfile(paths[2]+i) and os.path.getsize(paths[2]+i) <= size:
                if flagS:
                    os.mkdir(paths[1])
                    flagS=False
                shutil.copy(paths[2]+i,paths[1]+"\\"+i)
    else:
        print("Директории не существует по пути",path)
    
    
if __name__ == "__main__":
    if len(sys.argv) == 7 and sys.argv[1] == "--source" and sys.argv[3] == "--days" and sys.argv[5]=="--size":
        main(sys.argv[2],int(sys.argv[4]),int(sys.argv[6]))
    else:
        print("Error,Example\nreorganize --source \"C:\\TestDir\" --days 2 --size 4096")