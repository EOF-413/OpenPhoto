import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from threading import Thread


def flask_app():
    from app import app
    app.run(host='127.0.0.1', port=5000, debug=False)


if __name__ == '__main__':
    flask_thread = Thread(target=flask_app)
    flask_thread.daemon = True
    flask_thread.start()

    app = QApplication(sys.argv)

    web_view = QWebEngineView()

    web_view.load(QUrl('http://127.0.0.1:5000'))

    web_view.show()

    sys.exit(app.exec())
