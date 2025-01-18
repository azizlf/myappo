import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showFullScreen()
    sys.exit(app.exec())