from PyQt6.QtWidgets import QApplication, QWidget  # source -> python 3.14.5.

app = QApplication([])  #* Цикл событий

window = QWidget()
window.show()

app.exec()
