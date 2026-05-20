from importer import Importer

Thread = Importer.startup("threading", "Thread")

argv, exit = Importer.startup("sys", ("argv", "exit"))

Flask, render_template, send_from_directory = Importer.startup("flask", ("Flask", "render_template", "send_from_directory"))

QWebEngineView = Importer.startup("PyQt6.QtWebEngineWidgets", "QWebEngineView")

(
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
    QFrame,
    QLabel

) = Importer.startup(
    "PyQt6.QtWidgets",
    (
        "QApplication",
        "QMainWindow",
        "QWidget",
        "QPushButton",
        "QHBoxLayout",
        "QVBoxLayout",
        "QMessageBox",
        "QFrame",
        "QLabel",
    )

)

QUrl, Qt = Importer.startup(
    "PyQt6.QtCore",
    (
        "QUrl",
        "Qt"
    )
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(filename)

def run_flask():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)


class DesktopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main")
        self.setGeometry(100, 100, 1200, 800)
        self.setMinimumSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        toolbar = QFrame()
        toolbar.setFixedHeight(50)
        toolbar.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                border: none;
            }
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 0.4);
            }
        """)
        
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(10, 5, 10, 5)

        btn_refresh = QPushButton("🔄 Обновить")
        btn_refresh.clicked.connect(self.refresh_page)
        
        btn_home = QPushButton("🏠 Главная")
        btn_home.clicked.connect(self.go_home)
        
        btn_back = QPushButton("◀ Назад")
        btn_back.clicked.connect(self.go_back)
        
        btn_forward = QPushButton("Вперёд ▶")
        btn_forward.clicked.connect(self.go_forward)
        
        toolbar_layout.addWidget(btn_back)
        toolbar_layout.addWidget(btn_forward)
        toolbar_layout.addWidget(btn_refresh)
        toolbar_layout.addWidget(btn_home)
        toolbar_layout.addStretch()
        
        btn_exit = QPushButton("✖ Выход")
        btn_exit.clicked.connect(self.close)
        toolbar_layout.addWidget(btn_exit)
        
        main_layout.addWidget(toolbar)

        self.web_view = QWebEngineView()
        main_layout.addWidget(self.web_view, stretch=1)

        self.load_retry_count = 0
        self.load_local_page()
    
    def load_local_page(self):
        url = QUrl("http://127.0.0.1:5000")
        self.web_view.load(url)
    
    def refresh_page(self):
        self.web_view.reload()
    
    def go_home(self):
        self.load_local_page()
    
    def go_back(self):
        self.web_view.back()
    
    def go_forward(self):
        self.web_view.forward()
    
    def closeEvent(self, event):
        exit(0)

def main():
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()

    qt_app = QApplication(argv)
    window = DesktopApp()
    window.show()
    
    exit(qt_app.exec())

if __name__ == "__main__":
    main()
