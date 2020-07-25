from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys,time

class DigitalClock(QMainWindow):
    def __init__(self,parent=None):
        super(DigitalClock,self).__init__(parent)


        self.time=QTimer()
        self.time.timeout.connect(self.run)
        self.time.start(1000)

        self.number=0

        self.clock=QLCDNumber(self)
        self.clock.setDigitCount(8)

        self.setCentralWidget(self.clock)


        self.menucrate()
        self.resize(350,150)
        self.show()


    def run(self):
        self.number+=1

        self.hour = time.localtime().tm_hour
        self.minute = time.localtime().tm_min
        self.second = time.localtime().tm_sec

        if(len(str(self.hour)))==1:
            self.hour=str("0"+str(self.hour))
        if (len(str(self.minute))) == 1:
            self.minute = str("0" + str(self.minute))
        if (len(str(self.second))) == 1:
            self.second = str("0" + str(self.second))

        self.clock.display("{0}:{1}:{2}".format(str(self.hour),str(self.minute),str(self.second)))

        if self.number==60:
            self.number=0
            self.time.stop()
            self.time.start(1000)

    def menucrate(self):

        menus=QMenuBar()
        self.setMenuBar(menus)


        colorselect=QAction("COLOR SELECT",self)
        colorselect.triggered.connect(self.colorclick)

        menu=menus.addMenu("MENU")
        menu.addAction(colorselect)


    def colorclick(self):
        diyalog=QColorDialog()
        if diyalog.exec():
            self.clock.setStyleSheet("color:{};".format(diyalog.currentColor().name()))






uyg=QApplication(sys.argv)
window=DigitalClock()
sys.exit(uyg.exec())