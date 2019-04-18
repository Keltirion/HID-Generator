from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0, 0, 100, 100)  
              
        self.QLabel = QLabel()
        
        self.setLayout()
        self.initui()

    def initui(self):
                
        self.show()