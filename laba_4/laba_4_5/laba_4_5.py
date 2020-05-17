#5.	Напишите приложение для загрузки файлов из интернета. 
#В главном окне должно быть три текстовых поля, в которые 
#можно вводить URL файла на закачку; под каждым из текстовых 
#полей должны быть индикаторы загрузки и рядом поля с процентом 
#загрузки каждого файла. Необходимо организовать возможность 
#качать от одного до трех файлов параллельно (использовать потоки 
#обязательно, файлы загружать фрагментами по 4 Кб). Загрузка 
#должна инициироваться нажатием кнопки «Start downloading!». 
#По окончанию загрузки последнего файла должно появиться окно 
#со столбчатой диаграммой со значениями времени загрузки каждого 
#файла в формате «2s 322ms» и размерами файлов (используйте библиотеку matplotlib). 
#Рисунок 5 – Вид окна загрузки файлов 

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests 
from bs4 import BeautifulSoup 
import os
import urllib3
from threading import Thread
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

class DownloadThread(Thread):
    def __init__(self, DOWNLOAD_FOLDER, WEBSITE):
        """Инициализация потока"""
        Thread.__init__(self)
        self.__DOWNLOAD_FOLDER = DOWNLOAD_FOLDER
        self.__WEBSITE = WEBSITE
    
    def run(self):
        """Запуск потока"""
        self.dowload_link()
       
    def download_file(self):
        local_path = os.path.join(self.__DOWNLOAD_FOLDER,  self.__DOWNLOAD_FOLDER.split('/')[-1])
        r = requests.get(self.__DOWNLOAD_FOLDER, stream=True)
        with open(local_path, 'wb') as f:         
            for chunk in r.iter_content(chunk_size=4096):              
                if chunk: 
                    f.write(chunk)  
        return local_path 

    def dowload_link(self):
        content = requests.get(self.__WEBSITE) 
        soup = BeautifulSoup(content.text, 'html.parser') 
        links = soup.find_all('a') 
        links = filter(lambda a: a.get('href'), links) 
        links = filter(lambda a: a.get('href').endswith('mp3')
                       and not a.get('href').startswith('?'), links) 
        for link in links:
            print('Downloading: {}'.format(link.get('href')))
            download_file(link.get('href')) 



class Example(QMainWindow):
    def __init__(self):
        super().__init__()
         # Создадим виджет и сохраним ссылку на него
        
        self.initUI()
        #Основное окно
    def initUI(self):
        #Первые два параметра х и у - это позиция окна. Третий - ширина, и четвертый - высота окна
        self.setGeometry(200, 200, 900, 500)
        self.setWindowTitle('Files info')
        self.setWindowIcon(QIcon('ls.jpg'))
        
        tb = self.addToolBar("File")
        tb.setMovable(False)
        home = QAction(QIcon("home.png"),"home",self)
        tb.addAction(home)
        back = QAction(QIcon("back.png"),"back",self)
        tb.addAction(back)
        forward = QAction(QIcon("forward.png"),"forward",self)
        tb.addAction(forward)
        size = QAction(QIcon("size.png"),"size",self)
        tb.addAction(size)
        conservation = QAction(QIcon("conservation.jpg"),"conservation",self)
        tb.addAction(conservation)
        then = QAction(QIcon("then.png"),"then",self)
        tb.addAction(then)
        save = QAction(QIcon("save.png"),"save",self)
        tb.addAction(save)
        okey = QAction(QIcon("okey.png"),"okey",self)
        tb.addAction(okey)
        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.line1 = QLineEdit(self)
        self.line1.setGeometry(20,90,700,20)

        self.line2 = QLineEdit(self)
        self.line2.setGeometry(20,120,700,20)

        self.line3 = QLineEdit(self)
        self.line3.setGeometry(20,150,700,20)

        self.label1 = QLabel("Вставьте сыллки на скачивания", self)
        self.label1.setGeometry(20,70,700,20)


        self.show()
        
    def toolbtnpressed(self,q):
        
        if q.text() == "home":
            print(self.line1.text())
        elif q.text() == "back":
            print(self.line1.text())
        elif q.text() == "forward":
            print(self.line1.text())

        elif q.text() == "size":
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

        elif q.text() == "conservation":
            self.DOWNLOAD_FOLDER = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            print(self.DOWNLOAD_FOLDER)

        elif q.text() == "then":
            m = PlotCanvas(self, width=5, height=4)
            m.move(40,40)
            m.show()
                
            
        elif q.text() == "save":
            print(self.DOWNLOAD_FOLDER)
        elif q.text() == "okey":
            urls = []
            if self.line1:
                urls.append(self.line1.text())
            if self.line2:
                urls.append(self.line2.text())
            if self.line3:
                urls.append(self.line3.text())

            for item, url in enumerate(urls):
                name = "Поток %s" % (item+1)
                thread = DownloadThread(self.DOWNLOAD_FOLDER, "http://www.somesite.foo/audio/")
                thread.start()
            
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

    


 

        
    

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
