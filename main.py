from PyQt5.QtWidgets import QApplication
from urunEkle import urunEklePage

app = QApplication([])
pencere = urunEklePage()
pencere.show()
app.exec_()