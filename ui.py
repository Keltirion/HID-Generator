from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        return super().__init__()

        self.setWindowTitle('Hid Generator')
        self.setGeometry(0, 0, 100, 100)  
              
        self.QLabel = QLabel()

        self.initui()

    def initui(self):
                
        self.show()