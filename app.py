<<<<<<< HEAD
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
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
>>>>>>> 23e1aa0c6f1b523bb622e1679e70ecf5797d3722
