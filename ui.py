import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.label = QLabel('TEST')      

        self.initui()

    def initui(self):

        self.hbox.addStretch()
        self.hbox.addWidget(self.label)        
        self.hbox.addStretch()

        self.vbox.addStretch()
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch()

        self.setLayout(self.vbox)
        self.show()
