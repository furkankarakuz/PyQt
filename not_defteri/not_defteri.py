#Kodların büyük bir kısmı Mustafa Başer (Python) kitabından alınmıştır

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog


import sys,os

class Anapencere(QMainWindow):
    def __init__(self,ebeveyn=None):
        super(Anapencere,self).__init__(ebeveyn)



        self.bdeger={
            "yazitipi":"Arial",
            "yaziboyu":10,
            "kalin":False,
            "italik":False,
            "alticizili":False,
            "hizalama":Qt.AlignLeft
        }

        self.kaydedildi=False
        self.dosyaAdi=None
        self.kayitklasoru=QDir().homePath()

        self.anametin=QTextEdit()
        self.anametin.setFontFamily(self.bdeger['yazitipi'])
        self.anametin.setFontPointSize(self.bdeger['yaziboyu'])
        self.anametin.textChanged.connect(self.yapisikpencereguncelle)

        self.durumcubugu=self.statusBar()
        self.durumcubugu.showMessage("PROGRAM KULLANILMAYA HAZIR",3000)

        yapisikpencere=QDockWidget("İstatistik",self)
        self.istatistiketiket=QLabel()
        yapisikpencere.setWidget(self.istatistiketiket)
        yapisikpencere.setAllowedAreas(Qt.RightDockWidgetArea)
        yapisikpencere.setObjectName("yapisik/istatistik")
        self.addDockWidget(Qt.RightDockWidgetArea,yapisikpencere)
        self.setCentralWidget(self.anametin)
        self.resize(500,300)
        self.show()


        self.pencerebasligiguncelle()
        self.yapisikpencereguncelle()
        self.aksiyonlarihazirla()
        self.araccubuklari()
        self.menuler()


    def pencerebasligiguncelle(self):
        dosya=self.dosyaAdi if self.dosyaAdi else "Yeni Dosya"
        yildiz="*" if not self.kaydedildi else ""
        self.setWindowTitle("%s - [%s]"%(uyg.applicationName(),(dosya)+yildiz))

    def yapisikpencereguncelle(self):
        metin=self.anametin.toPlainText()
        bilgi='''<table><tr><td><b>HARF : </b></td><td>%d</td></tr>
                <tr><td><b>KELİME : </td><td>%d</td></tr>
                <tr><td><b>SATIR : </td><td>%d</td></tr>'''%(len(metin),len(metin.split()),metin.count("\n"))
        self.istatistiketiket.setText(bilgi)
        self.kaydedildi=False

        self.pencerebasligiguncelle()
        self.aksiyonlarihazirla()

    def aksiyonlarihazirla(self):
        self.solahizalaaksiyon=QAction(QIcon("icon/solhizala.png"),"&SOLA HİZALA",self)
        self.solahizalaaksiyon.setStatusTip("PARAGRAFI SOLA HİZALAR")
        self.solahizalaaksiyon.triggered.connect(self.solahizalayap)
        self.solahizalaaksiyon.setCheckable(True)
        self.solahizalaaksiyon.setShortcut("ALT+Z")

        self.ortalaaksiyon=QAction(QIcon("icon/ortala.png"),"&ORTALA",self)
        self.ortalaaksiyon.setStatusTip("PARAGRAFI ORTALAR")
        self.ortalaaksiyon.triggered.connect(self.ortalayap)
        self.ortalaaksiyon.setCheckable(True)
        self.ortalaaksiyon.setShortcut("ALT+X")

        self.sagahizalaaksiyon=QAction(QIcon("icon/saghizala.png"),"&SAĞA HİZALA",self)
        self.sagahizalaaksiyon.setStatusTip("PARAGRAFI SAĞA HİZALAR")
        self.sagahizalaaksiyon.triggered.connect(self.sagahizalayap)
        self.sagahizalaaksiyon.setCheckable(True)
        self.sagahizalaaksiyon.setShortcut("ALT+C")


        self.kalinaksiyon=QAction(QIcon("icon/kalin.png"),"&KALIN",self)
        self.kalinaksiyon.setStatusTip("METNİ KALIN YAPAR")
        self.kalinaksiyon.triggered.connect(self.kalinyap)
        self.kalinaksiyon.setCheckable(True)
        self.kalinaksiyon.setShortcut("Ctrl+B")

        self.italikaksiyon=QAction(QIcon("icon/italik.png"),"&İTALİK",self)
        self.italikaksiyon.setStatusTip("METNİ İTALİK YAPAR")
        self.italikaksiyon.triggered.connect(self.italikyap)
        self.italikaksiyon.setCheckable(True)
        self.italikaksiyon.setShortcut("Ctrl+I")

        self.alticiziliaksiyon=QAction(QIcon("icon/alticizili.png"),"&ALTI ÇİZİLİ",self)
        self.alticiziliaksiyon.setStatusTip("METNİN ALTINI ÇİZER")
        self.alticiziliaksiyon.triggered.connect(self.alticiziliyap)
        self.alticiziliaksiyon.setCheckable(True)
        self.alticiziliaksiyon.setShortcut("Ctrl+U")

        self.yazitipiaksiyon=QAction(QIcon(""),"&YAZI TİPİ",self)
        self.yazitipiaksiyon.setStatusTip("Yazı Tipi Ayarları")
        self.yazitipiaksiyon.triggered.connect(self.yazitipidegistir)
        self.yazitipiaksiyon.setShortcut("Alt+Y")

        self.renkayarlaaksiyon=QAction(QIcon(""),"&Renk Ayarla",self)
        self.renkayarlaaksiyon.setStatusTip("Yazı Tipi Rengini Ayarlar")
        self.renkayarlaaksiyon.triggered.connect(self.yazirengi)
        self.renkayarlaaksiyon.setShortcut("F5")

        self.kaydetaksiyon=QAction(QIcon(""),"&Kaydet",self)
        self.kaydetaksiyon.setStatusTip("Dosyayı Kaydeder")
        self.kaydetaksiyon.triggered.connect(self.kaydet)
        self.kaydetaksiyon.setShortcut(QKeySequence.Save)

        self.farklikaydetaksiyon=QAction(QIcon(""),"&Farklı Kaydet",self)
        self.farklikaydetaksiyon.setStatusTip("Dosyayı Başka İsimle Kaydeder")
        self.farklikaydetaksiyon.triggered.connect(self.farklikaydet)
        self.farklikaydetaksiyon.setShortcut(QKeySequence.SaveAs)

        self.dosyaacaksiyon=QAction(QIcon(""),"&Dosya Aç",self)
        self.dosyaacaksiyon.setStatusTip("Daha Önce Kaydedilmiş Dosyayı Açar")
        self.dosyaacaksiyon.triggered.connect(self.dosyaac)
        self.dosyaacaksiyon.setShortcut(QKeySequence.Open)

        self.yaziciyadokaksiyon=QAction(QIcon(""),"Yazdır",self)
        self.yaziciyadokaksiyon.setStatusTip("Açık Dökümanı Yazıcıya Döker")
        self.yaziciyadokaksiyon.triggered.connect(self.kagidadok)

        self.pdfaksiyon=QAction(QIcon(""),"PDF DÖNÜŞTÜR",self)
        self.pdfaksiyon.setStatusTip("YAZIYI PDF FORMATINA DÖNÜŞTÜRÜR")
        self.pdfaksiyon.triggered.connect(self.pdfdonustur)

    def araccubuklari(self):
        paragrafaraci=self.addToolBar("PARAGRAF")
        paragrafaraci.setObjectName("arac/paragraf")
        paragrafaraci.addAction(self.solahizalaaksiyon)
        self.solahizalaaksiyon.setChecked(True)

        paragrafaraci.addAction(self.ortalaaksiyon)
        paragrafaraci.addAction(self.sagahizalaaksiyon)

        paragrafgrup=QActionGroup(self)
        paragrafgrup.addAction(self.solahizalaaksiyon)
        paragrafgrup.addAction(self.ortalaaksiyon)
        paragrafgrup.addAction(self.sagahizalaaksiyon)



        yazitipiaraci=QToolBar("DÜZENLE")
        yazitipiaraci.setObjectName("arac/duzen")
        yazitipiaraci.addAction(self.kalinaksiyon)
        yazitipiaraci.addAction(self.italikaksiyon)
        yazitipiaraci.addAction(self.alticiziliaksiyon)

        self.addToolBar(yazitipiaraci)

    def menuler(self):
        menubar=QMenuBar()

        self.setMenuBar(menubar)

        dosyamenusu=menubar.addMenu("&DOSYA")
        bicimmenusu=menubar.addMenu("&BİÇİM")
        yardimmenusu=menubar.addMenu("&YARDIM")

        hizalamenusu=bicimmenusu.addMenu("&Hizalama")
        hizalamenusu.addAction(self.solahizalaaksiyon)
        hizalamenusu.addAction(self.ortalaaksiyon)
        hizalamenusu.addAction(self.sagahizalaaksiyon)

        bicimmenusu.addAction(self.yazitipiaksiyon)
        bicimmenusu.addSeparator()
        bicimmenusu.addAction(self.renkayarlaaksiyon)

        dosyamenusu.addAction(self.kaydetaksiyon)
        dosyamenusu.addAction(self.farklikaydetaksiyon)
        dosyamenusu.addSeparator()
        dosyamenusu.addAction(self.dosyaacaksiyon)
        dosyamenusu.addSeparator()
        dosyamenusu.addAction(self.yaziciyadokaksiyon)
        dosyamenusu.addSeparator()
        dosyamenusu.addAction(self.pdfaksiyon)



    def solahizalayap(self):
        self.anametin.setAlignment(Qt.AlignLeft)

    def ortalayap(self):
        self.anametin.setAlignment(Qt.AlignCenter)

    def sagahizalayap(self):
        self.anametin.setAlignment(Qt.AlignRight)

    def kalinyap(self):
        if self.sender().isChecked():
            self.anametin.setFontWeight(QFont.Bold)
        else:
            self.anametin.setFontWeight(QFont.Normal)

    def italikyap(self):
        if self.sender().isChecked():
            self.anametin.setFontItalic(True)
        else:
            self.anametin.setFontItalic(False)


    def alticiziliyap(self):
        if self.sender().isChecked():
            self.anametin.setFontUnderline(True)
        else:
            self.anametin.setFontUnderline(False)

    def diskeyaz(self):
        F=open(self.dosyaAdi,"w")

        F.write(self.anametin.toPlainText())

        F.close()

        self.durumcubugu.showMessage("DOSYA BAŞARIYLA KAYDEDİLDİ",1000)
        self.kaydedildi=True
        self.pencerebasligiguncelle()

    def farklikaydet(self):
        dosya=self.dosyaAdi if self.dosyaAdi else self.kayitklasoru
        secilendosya=QFileDialog.getSaveFileName(self,uyg.applicationName()+" -Dosya Kaydet",dosya,"*.txt")
        if secilendosya:
            self.dosyaAdi=secilendosya[0]
            self.diskeyaz()
            self.kayitklasoru=secilendosya[0]

            return True
        else:
            return False

    def kaydet(self):
        if not self.dosyaAdi:
            return  self.farklikaydet()
        else:
            self.diskeyaz()
            return True

    def dosyayukle(self,dosya):
        F=open(dosya).read()
        self.anametin.setText(F)

        self.kaydedildi=True
        self.dosyaAdi=dosya

    def dosyaac(self):
        if not self.kaydedildi:
            if len(self.anametin.toPlainText())>0:
                kaydetcevabi=self.kaydedilsinmisor()
                if kaydetcevabi=="yes":
                    self.kaydet()
                else:
                    return
        secilendosya=QFileDialog.getOpenFileName(self,uyg.applicationName()+"-Dosya Aç",self.kayitklasoru,
                                                 "*.txt")
        if secilendosya:
            self.kayitklasoru=secilendosya
            self.dosyayukle(secilendosya[0])

    def kaydedilsinmisor(self):
        cevap=QMessageBox.question(self,uyg.applicationName(),"-DOSYA KAYDEDİLMEMİŞ \n Değişiklikler Kaydedilsin mi?",
                                   QMessageBox.Yes,QMessageBox.No)

        if cevap==QMessageBox.Yes:
            return "yes"
        elif cevap==QMessageBox.No:
            return "no"

    def yazirengi(self):
        renkdlg=QColorDialog()
        renkdlg.setCurrentColor(self.anametin.textColor())
        if(renkdlg.exec()):
            self.anametin.setTextColor(renkdlg.selectedColor())

    def kagidadok(self):
        diyalog = QPrintPreviewDialog()
        diyalog.paintRequested.connect(self.ciktial)
        diyalog.exec()

    def ciktial(self, yaz):
        self.anametin.print(yaz)

    def pdfdonustur(self):
        document=self.anametin.document()
        printer=QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("dosya.pdf")
        document.print(printer)



    def yazitipidegistir(self):
        diyalog=yazitipiDlg(self)
        diyalog.show()


class yazitipiDlg(QDialog):
    def __init__(self,ebeveyn=None):
        super(yazitipiDlg,self).__init__(ebeveyn)

        self.ebeveyn=ebeveyn
        self.setAttribute(Qt.WA_DeleteOnClose)

        izgara=QGridLayout()
        yetiket=QLabel("&Yazı Tipi : ")
        izgara.addWidget(yetiket,0,0)

        self.yazitipi=QFontComboBox()
        izgara.addWidget(self.yazitipi,0,1)
        yetiket.setBuddy(self.yazitipi)

        betiket=QLabel("&Boyut : ")
        izgara.addWidget(betiket,1,0)
        self.yaziboyu=QSpinBox()
        self.yaziboyu.setRange(1,50)
        izgara.addWidget(self.yaziboyu,1,1)
        betiket.setBuddy(self.yaziboyu)

        ozellikyerlesimi=QHBoxLayout()

        self.yazikalin=QCheckBox("&Kalın")
        ozellikyerlesimi.addWidget(self.yazikalin)

        self.yaziitalik=QCheckBox("&İtalik")
        ozellikyerlesimi.addWidget(self.yaziitalik)

        self.alticizili=QCheckBox("&Altı Çizili")
        ozellikyerlesimi.addWidget(self.alticizili)

        izgara.addLayout(ozellikyerlesimi,2,0,1,2)

        dugmekutusu=QDialogButtonBox(
            QDialogButtonBox.Ok|
            QDialogButtonBox.Cancel)

        dugmekutusu.button(QDialogButtonBox.Ok).setText("Tamam")
        dugmekutusu.button(QDialogButtonBox.Cancel).setText("Vazgeç")

        dugmekutusu.accepted.connect(self.kabul)
        dugmekutusu.rejected.connect(self.reject)

        izgara.addWidget(dugmekutusu,3,0,1,2)
        self.setLayout(izgara)

        self.setWindowTitle("YazıTipini Ayarla")
        self.yazitipi.setCurrentFont(self.ebeveyn.anametin.currentFont())
        self.yaziboyu.setValue(self.ebeveyn.anametin.fontPointSize())
        self.yazikalin.setChecked(True if self.ebeveyn.anametin.fontWeight()==QFont.Bold else False)
        self.yaziitalik.setChecked(self.ebeveyn.anametin.fontItalic())
        self.alticizili.setChecked(self.ebeveyn.anametin.fontUnderline())

    def kabul(self):
        self.ebeveyn.anametin.setCurrentFont(self.yazitipi.currentFont())
        self.ebeveyn.anametin.setFontPointSize(self.yaziboyu.value())
        self.ebeveyn.anametin.setFontItalic(self.yaziitalik.isChecked())
        self.ebeveyn.anametin.setFontUnderline(self.alticizili.isChecked())
        self.ebeveyn.anametin.setFontWeight(
            QFont.Bold if self.yazikalin.isChecked() else QFont.Normal)
        QDialog.accept(self)



uyg=QApplication(sys.argv)
uyg.setOrganizationName("PYTHON ÖĞRENİYORUM")
uyg.setApplicationName("PYQT NOT DEFTERİ")
pencere=Anapencere()
sys.exit(uyg.exec())
