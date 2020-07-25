from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import random


class Anasayfa(QMainWindow):
    def __init__(self,ebeveyn=None):
        super(Anasayfa,self).__init__(ebeveyn)

        butonpcoyna=QPushButton("PC İLE OYNA",self)
        butonpcoyna.setGeometry(0,0,300,500)
        butonpcoyna.clicked.connect(self.pcoynamatikla)

        butonikilioyna=QPushButton("İKİ KİŞİ OYNA",self)
        butonikilioyna.setGeometry(300,0,300,500)
        butonikilioyna.clicked.connect(self.ikilioynamatikla)

        self.show()
        self.setFixedSize(600,500)

    def ikilioynamatikla(self):
        diyalog1=ikioyunculu(self)
        diyalog1.show()

    def pcoynamatikla(self):
        diyalog2=pcoyunculu(self)
        diyalog2.show()


class pcoyunculu(QMainWindow):
    def __init__(self,ebeveyn=None):
        super(pcoyunculu,self).__init__(ebeveyn)

        tas=QPushButton("TAŞ",self)
        tas.setGeometry(75,50,50,50)
        tas.clicked.connect(self.butonsec)


        kagit=QPushButton("KAĞIT",self)
        kagit.setGeometry(125,50,50,50)
        kagit.clicked.connect(self.butonsec)


        makas=QPushButton("MAKAS",self)
        makas.setGeometry(175,50,50,50)
        makas.clicked.connect(self.butonsec)


        self.oyuncu=QLabel(self)
        self.oyuncu.setGeometry(50,100,200,200)
        self.oyuncu.setFrameShape(QFrame.Box)


        self.pc=QLabel(self)
        self.pc.setGeometry(350, 100, 200, 200)
        self.pc.setFrameShape(QFrame.Box)

        self.sonucetiket = QLabel("BAŞLA", self)
        self.sonucetiket.setFont(QFont("Verdana", 13))
        self.sonucetiket.setGeometry(200, 350, 200, 50)
        self.sonucetiket.setAlignment(Qt.AlignCenter)


        self.skor = QLabel("0-0", self)
        self.skor.setFont(QFont("Verdana", 15))
        self.skor.setGeometry(250, 150, 100, 100)
        self.skor.setAlignment(Qt.AlignCenter)

        self.oyuncutiklandi = False
        self.pctiklandi = False

        self.oyuncuskor = 0
        self.pcskor = 0

        self.setFixedSize(600, 500)

    def butonsec(self):
        secilenbuton=self.sender().text()
        self.oyuncusecilen=secilenbuton
        if secilenbuton=="TAŞ":
            self.oyuncu.setPixmap(QPixmap("image/tassol.png").scaled(200,200))
        elif secilenbuton=="KAĞIT":
            self.oyuncu.setPixmap(QPixmap("image/kagitsol.png").scaled(200,200))
        elif secilenbuton=="MAKAS":
            self.oyuncu.setPixmap(QPixmap("image/makassol.png").scaled(200,200))

        self.oyuncutiklandi=True
        self.pcsec()

    def pcsec(self):
        if(self.oyuncutiklandi==True):
            self.secilenpc = random.choice(["kagitsag", "makassag", "tassag"])
            self.pc.setPixmap(QPixmap("image/" + self.secilenpc + ".png").scaled(200, 200))
            self.tiklandimi()

    def tiklandimi(self):
        if self.oyuncutiklandi==True:
            if(self.oyuncusecilen=="KAĞIT"):
                if(self.secilenpc=="kagitsag"):
                    sonuc="BERABERE"
                elif(self.secilenpc=="makassag"):
                    sonuc="PC KAZANDI"
                    self.pcskor+=1
                else:
                    sonuc="OYUNCU KAZANDI"
                    self.oyuncuskor+=1

            elif(self.oyuncusecilen=="MAKAS"):
                if (self.secilenpc == "kagitsag"):
                    sonuc = "OYUNCU KAZANDI"
                    self.oyuncuskor += 1
                elif (self.secilenpc == "makassag"):
                    sonuc = "BERABERE"
                else:
                    sonuc = "PC KAZANDI"
                    self.pcskor += 1

            elif(self.oyuncusecilen=="TAŞ"):
                if (self.secilenpc == "kagitsag"):
                    sonuc = "PC KAZANDI"
                    self.pcskor += 1
                elif (self.secilenpc == "makassag"):
                    sonuc = "OYUNCU KAZANDI"
                    self.oyuncuskor += 1
                else:
                    sonuc = "BERABERE"

            self.sonucetiket.setText(sonuc)
            self.skor.setText(str(self.oyuncuskor)+" - "+str(self.pcskor))
        else:
            pass







class ikioyunculu(QMainWindow):
    def __init__(self,ebeveyn=None):
        super(ikioyunculu,self).__init__(ebeveyn)

        self.soloyuncu=QLabel(self)
        self.soloyuncu.setGeometry(50,100,200,200)
        self.soloyuncu.setFrameShape(QFrame.Box)

        self.sagoyuncu=QLabel(self)
        self.sagoyuncu.setGeometry(350,100,200,200)
        self.sagoyuncu.setFrameShape(QFrame.Box)

        self.solbuton=QPushButton("TIKLA",self)
        self.solbuton.setGeometry(100,50,100,50)
        self.solbuton.clicked.connect(self.soltikla)

        self.sagbuton=QPushButton("TIKLA",self)
        self.sagbuton.setGeometry(400,50,100,50)
        self.sagbuton.clicked.connect(self.sagtikla)


        self.sonucetiket=QLabel("BAŞLA",self)
        self.sonucetiket.setFont(QFont("Verdana",13))
        self.sonucetiket.setGeometry(200,350,200,50)
        self.sonucetiket.setAlignment(Qt.AlignCenter)

        self.resetbuton=QPushButton("RESETLE",self)
        self.resetbuton.setGeometry(225,450,150,50)
        self.resetbuton.setEnabled(False)
        self.resetbuton.clicked.connect(self.resetle)

        self.skor=QLabel("0-0",self)
        self.skor.setFont(QFont("Verdana", 15))
        self.skor.setGeometry(250,150,100,100)
        self.skor.setAlignment(Qt.AlignCenter)

        self.soltiklandi=False
        self.sagtiklandi=False

        self.solskor = 0
        self.sagskor = 0

        self.setFixedSize(600,500)
        self.show()

    def soltikla(self):
        self.secilensol=random.choice(["kagitsol","makassol", "tassol"])
        self.soloyuncu.setPixmap(QPixmap("image/"+self.secilensol+".png").scaled(200,200))
        self.solbuton.setEnabled(False)
        self.soltiklandi=True
        self.tiklandimi()

    def sagtikla(self):
        self.secilensag = random.choice(["kagitsag","makassag", "tassag"])
        self.sagoyuncu.setPixmap(QPixmap("image/"+self.secilensag+".png").scaled(200, 200))
        self.sagbuton.setEnabled(False)
        self.sagtiklandi = True
        self.tiklandimi()

    def tiklandimi(self):
        if self.soltiklandi and self.sagtiklandi:
            if(self.secilensol=="kagitsol"):
                if(self.secilensag=="kagitsag"):
                    sonuc="BERABERE"
                elif(self.secilensag=="makassag"):
                    sonuc="SAĞ OYUNCU KAZANDI"
                    self.sagskor+=1
                else:
                    sonuc="SOL OYUNCU KAZANDI"
                    self.solskor+=1

            elif(self.secilensol=="makassol"):
                if (self.secilensag == "kagitsag"):
                    sonuc = "SOL OYUNCU KAZANDI"
                    self.solskor += 1
                elif (self.secilensag == "makassag"):
                    sonuc = "BERABERE"
                else:
                    sonuc = "SAĞ OYUNCU KAZANDI"
                    self.sagskor += 1

            elif(self.secilensol=="tassol"):
                if (self.secilensag == "kagitsag"):
                    sonuc = "SAĞ OYUNCU KAZANDI"
                    self.sagskor += 1
                elif (self.secilensag == "makassag"):
                    sonuc = "SOL OYUNCU KAZANDI"
                    self.solskor += 1
                else:
                    sonuc = "BERABERE"

            self.sonucetiket.setText(sonuc)
            self.resetbuton.setEnabled(True)
            self.skor.setText(str(self.solskor)+" - "+str(self.sagskor))
        else:
            pass

    def resetle(self):
        self.soltiklandi = False
        self.sagtiklandi = False

        self.soloyuncu.setPixmap(QPixmap(""))
        self.sagoyuncu.setPixmap(QPixmap(""))

        self.solbuton.setEnabled(True)
        self.sagbuton.setEnabled(True)

        self.resetbuton.setEnabled(False)
        self.sonucetiket.setText("BAŞLA")



uyg=QApplication(sys.argv)
pencere=Anasayfa()
sys.exit(uyg.exec())