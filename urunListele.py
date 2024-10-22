from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from urunListele_python import Ui_Form
from productDatabese import *

class urunListelePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.urunListeleForm = Ui_Form()
        self.urunListeleForm.setupUi(self)

        conn = sql.connect("/home/kiuseh/Masaüstü/python/stok programı/Product_Database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT rowid,* FROM PRODUCTS")
        liste  = cursor.fetchall()

        conn.commit()
        conn.close()

        self.urunListeleForm.tableWidget.setRowCount(len(liste))

        satir = 0
        for i in liste:
            self.urunListeleForm.tableWidget.setItem(int(satir),0,QTableWidgetItem(str(i[0])))
            self.urunListeleForm.tableWidget.setItem(int(satir),1,QTableWidgetItem(str(i[1])))
            self.urunListeleForm.tableWidget.setItem(int(satir),2,QTableWidgetItem(str(i[2])))
            self.urunListeleForm.tableWidget.setItem(int(satir),3,QTableWidgetItem(str(i[3])))                                                     
            satir += 1

        
        
