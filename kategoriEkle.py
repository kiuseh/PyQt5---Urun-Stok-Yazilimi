from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from kategoriEkle_python import Ui_Form

class KategoriEklePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.kategoriEkleForm = Ui_Form()
        self.kategoriEkleForm.setupUi(self)