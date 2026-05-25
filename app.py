from PyQt6.QtWidgets import (
    QWidget,  # Основной класс
    QLabel,  # Текст
    QPushButton,  # Кнопка
    QLineEdit  # Поле ввода
)

from PyQt6.QtGui import (
    QPixmap  # Работа с изображениями
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("App")
        self.show()
