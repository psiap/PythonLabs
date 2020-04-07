import ffmpeg
import os
import sys
import subprocess

class Globals:
    source = "D:\\Application\\Git\\PythonLabs\\Lab2\\TestM"
    destination= "mix.mp3"
    count= "0" # conver to int 
    frame= "10"
    log= False #
    extended= False #True
    flag = False #Flag for --source
    types = ["trim","concat","fade"]
    global_count = 0



def main():
    musics = os.listdir(Globals.source)
    if int(Globals.count) > 0:
        musics = [musics[i] for i in range(int(Globals.count))]
    else:
        Globals.count = str(len(musics))
    trim(musics)
    if Globals.extended:
        fad(musics)
    concat(musics)
    delet(musics)


def trim(musics):
    for i in musics:
        Globals.global_count+=1
        log_music(Globals.global_count,os.path.join(Globals.source,Globals.types[0]+i))
        command = "ffmpeg -loglevel quiet -i \"{0}\" -acodec copy -ss 0 -t \"{2}\"  \"{1}\"".format(os.path.join(Globals.source,i),os.path.join(Globals.source,Globals.types[0]+i),Globals.frame)
        subprocess.call(command, shell=True)


def fad(musics):
    for i in musics:
        Globals.global_count+=1
        log_music(Globals.global_count,os.path.join(Globals.source,Globals.types[2]+i))
        command = "ffmpeg -loglevel quiet -i \"{0}\" -af  \"afade=t=in:ss=0:d={3},afade=t=out:st={2}:d={3}\"  \"{1}\"".format(os.path.join(Globals.source,Globals.types[0]+i),os.path.join(Globals.source,Globals.types[2]+i),str(int(Globals.frame)/2),str(int(Globals.frame)/2))
        subprocess.call(command, shell=True)


def concat(music):#LEN(MUSICS)-2 = LAST MUSIC
    concats = 0
    pref = Globals.types[2] if Globals.extended else Globals.types[0]
    subprocess.call("ffmpeg -loglevel quiet -i \"{0}\" -i \"{1}\" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 {2}".format(os.path.join(Globals.source,pref+music[0]),os.path.join(Globals.source,pref+music[1]),os.path.join(Globals.source,Globals.types[1]+str(0)+".mp3")), shell=True)
    for i in (music):
        if i ==music[0] or i == music[1]:
            continue
        Globals.global_count+=1
        log_music(Globals.global_count,os.path.join(Globals.source,Globals.types[1]+str(concats+1)+".mp3"))
        command = "ffmpeg -loglevel quiet -i \"{0}\" -i \"{1}\" -filter_complex [0:a][1:a]concat=n=2:v=0:a=1 {2}".format(os.path.join(Globals.source,Globals.types[1]+str(concats)+".mp3"),os.path.join(Globals.source,Globals.types[0]+i),os.path.join(Globals.source,Globals.types[1]+str(concats+1)+".mp3"))
        subprocess.call(command, shell=True)
        concats+=1


def delet(musics):
    counter = 0
    for i in musics:
        if os.path.isfile(os.path.join(Globals.source,Globals.types[0]+i)):
            os.remove(os.path.join(Globals.source,Globals.types[0]+i))
        if os.path.isfile(os.path.join(Globals.source,Globals.types[2]+i)):
            os.remove(os.path.join(Globals.source,Globals.types[2]+i))
        if  counter <= int(Globals.count)-3 and os.path.isfile(os.path.join(Globals.source,Globals.types[1]+str(counter)+".mp3")):
              os.remove(os.path.join(Globals.source,Globals.types[1]+str(counter)+".mp3"))
              counter+=1
    os.rename(os.path.join(Globals.source,Globals.types[1]+str(counter)+".mp3"),os.path.join(Globals.source,Globals.destination))
    print("--- done!")
        

def log_music(i,name):
    if Globals.log:
        print("--- processing {0}: {1}".format(i,name))


def two_argument_compare(arg1,arg2,comp):
    if arg1 == comp or arg2 ==comp:
        return True
    else:
        return False


if __name__ == "__main__":
    #print(sys.argv)
    #sys.argv = ['D:\\Application\\Git\\PythonLabs\\Lab2\\trackmix.py', '-s', 'D:\\Application\\Git\\PythonLabs\\Lab2\\TestM', '-d', 'kek.mp3', '-f', '15', '-l', '--extended']
    #print(sys.argv)
    for i in range(len(sys.argv)):
        if two_argument_compare("--source", "-s", sys.argv[i]):
            Globals.source = sys.argv[i+1]
            Globals.flag= True
            continue
        if two_argument_compare("--destination", "-d", sys.argv[i]):
            Globals.destination = sys.argv[i+1]
            continue
        if two_argument_compare("--count", "-c", sys.argv[i]):
            Globals.count = sys.argv[i]
            continue
        if two_argument_compare("--frame", "-f", sys.argv[i]):
            Globals.frame = sys.argv[i+1]
            continue
        if two_argument_compare("--log", "-l", sys.argv[i]):
            Globals.log = not Globals.log
            continue
        if two_argument_compare("--extended", "-e", sys.argv[i]):
            Globals.extended = not Globals.extended
            continue
    if Globals.flag:
        main()