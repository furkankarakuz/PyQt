from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Home(QDialog):
    def __init__(self,this=None):
        super(Home,self).__init__(this)

        self.title='<center><font size="+3" color="blue">CAESAR ALGORITHM</font><center>'
        self.label=QLabel(self.title)


        self.rd1=QRadioButton("PLAINTEXT -> ENCRYPTED")
        self.rd1.setChecked(True)
        self.rd2=QRadioButton("ENCRYPTED -> PLAINTEXT")

        self.hbox=QHBoxLayout()
        self.hbox.addWidget(self.rd1)
        self.hbox.addWidget(self.rd2)

        self.input=QLineEdit()

        self.step=QSpinBox()
        self.step.setRange(1,len(characters)-1)
        self.step.setValue(1)

        self.output=QLineEdit()
        self.output.setEnabled(False)

        button=QPushButton()
        button.clicked.connect(self.click)
        button.setMaximumHeight(100)
        button.setFixedWidth(50)
        button.setIcon(QIcon("key.png"))
        button.setIconSize(QSize(30,30))


        box=QGridLayout()
        box.addWidget(self.label,0,0,1,5)
        box.addLayout(self.hbox,1,0,1,4)
        box.addWidget(QLabel("INPUT : "),2,0)
        box.addWidget(self.input,2,1,1,3)
        box.addWidget(QLabel("STEP : "),3,0)
        box.addWidget(self.step,3,1)
        box.addWidget(button,1,4,4,1)
        box.addWidget(QLabel("OUTPUT : "),4,0)
        box.addWidget(self.output,4,1,1,3)

        self.setFixedSize(380,250)
        self.setWindowTitle("CAESAR ALGORITHM")
        self.setLayout(box)
        self.show()
    
    def click(self):
        self.input.setText(self.input.text().upper())
        metin = self.input.text()

        if(self.rd1.isChecked()):
            newtext =""
            for i in metin:
                if i not in characters:
                    self.input.setText("You Entered Another Character")
                if i in characters:
                    i = characters[(characters.index(i) + self.step.value())%len(characters)]
                    newtext += i
            self.output.setText(newtext)

        else:
            newtext=""
            for i in metin:
                if i not in characters:
                    self.input.setText("You Entered Another Character")
                if i in characters:
                    i=characters[(characters.index(i)-self.step.value())%len(characters)]
                    newtext+=i
            self.output.setText(newtext)



app=QApplication(sys.argv)
window=Home()
sys.exit(app.exec())
