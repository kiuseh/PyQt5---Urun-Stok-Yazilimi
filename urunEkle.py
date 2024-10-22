from PyQt5.QtWidgets import *
from urunEkle_python import Ui_MainWindow
from urunListele import urunListelePage
from kategoriEkle import KategoriEklePage
from productDatabese import *
import dataModule as dm


class urunEklePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.urunEkleForm = Ui_MainWindow()
        self.urunEkleForm.setupUi(self)
        self.urunListeleForm = urunListelePage()
        self.kategoriEkleForm = KategoriEklePage()

        #Eylemler
        self.urunEkleForm.ekle.clicked.connect(self.pbUrunEkle)
        self.urunEkleForm.urunListele.triggered.connect(self.urunListele)
        self.urunEkleForm.kategoriEkle.triggered.connect(self.kategoriEkle)
        
        
    
    def pbUrunEkle(self):
        dm.urunAdi = self.urunEkleForm.urunAdi.text()
        dm.miktari = self.urunEkleForm.miktari.text()
        dm.aciklama = self.urunEkleForm.aciklama.toPlainText()

        insert(dm.urunAdi, dm.miktari, dm.aciklama)

        self.close()
    
    def urunListele(self):
        self.urunListeleForm.show()
    
    def kategoriEkle(self):
        self.kategoriEkleForm.show()