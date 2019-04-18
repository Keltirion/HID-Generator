import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        return super().__init__(parent=parent, flags=flags)

        self.setWindowTitle('Hid Generator')
        
        self.QLabel = QLabel()

    def initui(self):
        
        
        self.show()