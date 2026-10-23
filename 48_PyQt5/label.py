import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First Python App")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), "boy.png")))

        label = QLabel("Hello", self)
        label.setFont(QFont("Ariel", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter)  # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()