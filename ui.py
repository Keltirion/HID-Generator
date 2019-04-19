from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout,
                            QFileDialog, QPushButton, QListWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()         
        
        self.file = QFileDialog(self, )
        self.label = QLabel('Test')
        self.list = QListWidget()
        self.btn = QPushButton('Browse files')
        self.delbtn= QPushButton('Delete')
        self.hbox = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()        
        
        self.initui()

    def initui(self):
        self.hbox.addStretch()
        self.hbox.addWidget(self.label)
        self.hbox.addStretch()

        self.hbox2.addStretch()
        self.hbox2.addWidget(self.btn)
        self.hbox2.addWidget(self.list)
        self.hbox2.addStretch()

        self.vbox.addStretch()        
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addStretch()

        self.btn.clicked.connect(self.browse)

        self.setLayout(self.vbox)        
        self.show()

    def browse(self): 
        self.file = QFileDialog.getOpenFileNames(self, 'Open file', 'c\\')
        items = self.file[0]
        print(items)
        for photo in items:
            print(photo)
            self.list.addItem(photo)
        return items

    def deleteitem(self):
        
        pass

        
