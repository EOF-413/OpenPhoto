<<<<<<< HEAD
from app import MainWindow
from PyQt6.QtWidgets import QApplication
=======
import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from threading import Thread
>>>>>>> 23e1aa0c6f1b523bb622e1679e70ecf5797d3722


<<<<<<< HEAD
window = MainWindow()
=======
def flask_app():
    from app import app
    app.run(host='127.0.0.1', port=5000, debug=False)
>>>>>>> 23e1aa0c6f1b523bb622e1679e70ecf5797d3722


if __name__ == '__main__':
    flask_thread = Thread(target=flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    app = QApplication(sys.argv)

    web_view = QWebEngineView()

    web_view.load(QUrl('http://127.0.0.1:5000'))

    web_view.show()

    sys.exit(app.exec())
