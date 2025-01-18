from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont, QGuiApplication
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        
        # Get screen size
        screen = QGuiApplication.primaryScreen()
        screen_size = screen.availableGeometry()
        MainWindow.setGeometry(screen_size)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        # Create layouts
        main_layout = QVBoxLayout(self.centralwidget)
        main_layout.setAlignment(Qt.AlignCenter)

        # Create the label
        self.label = QLabel(self.centralwidget)
        font1 = QFont()
        font1.setPointSize(43)
        self.label.setFont(font1)
        self.label.setText("Welcome to my OS")
        self.label.setAlignment(Qt.AlignCenter)
        
        # Set label background to transparent
        self.label.setStyleSheet("background-color: transparent;")

        # Create the button
        self.pushButton = QPushButton(self.centralwidget)
        font = QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setText("Click")
        
        # Set button background to white
        self.pushButton.setStyleSheet("background-color: white;")

        # Add the widgets to the layout
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.pushButton)

        # Set background gradient for the central widget
        self.centralwidget.setStyleSheet(
            "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #FFA500, stop:1 #3498db);"
        )

        # Set the central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Connect button click event
        self.pushButton.clicked.connect(self.on_button_click)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

    def on_button_click(self):
        self.label.setText("Button clicked!")
