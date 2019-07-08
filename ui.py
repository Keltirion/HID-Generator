from functions import *
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout,
                            QFileDialog, QPushButton, QListWidget,)

photoalbum = {}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()      
        
        self.card = CardCreate()
        self.windowTitle('Samurai')
        self.addfiles = QFileDialog(self,)
        self.label = QLabel('Wybrane zdjęcia')
        self.list = QListWidget()
        self.btn = QPushButton('Browse files')
        self.delbtn = QPushButton('Delete')
        self.startbtn = QPushButton('Start')
        self.closebtn = QPushButton('Close')
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.vbox3 = QVBoxLayout()
        self.hbox = QHBoxLayout()        
        self.hbox1 = QHBoxLayout()              

        self.initui()

    def initui(self):        
        self.vbox2.addStretch()
        self.vbox2.addWidget(self.btn)
        self.vbox2.addStretch()
        self.vbox2.addWidget(self.delbtn)
        self.vbox2.addStretch()

        self.vbox1.addStretch()
        self.vbox1.addWidget(self.label)
        self.vbox1.addWidget(self.list)
        self.vbox1.addStretch()        

        self.hbox1.addStretch()
        self.hbox1.addWidget(self.closebtn)
        self.hbox1.addStretch()
        self.hbox1.addWidget(self.startbtn)
        self.hbox1.addStretch()

        self.hbox.addStretch()
        self.hbox.addLayout(self.vbox1)
        self.hbox.addLayout(self.vbox2)
        self.hbox.addStretch()        
        
        self.vbox3.addStretch()
        self.vbox3.addLayout(self.hbox)
        self.vbox3.addLayout(self.hbox1)        
        self.vbox3.addStretch()

        self.btn.clicked.connect(self.browse)
        self.delbtn.clicked.connect(self.deleteitem)
        self.startbtn.clicked.connect(self.start)

        self.setLayout(self.vbox3)        
        self.show()

    def browse(self): 
        self.addfiles = QFileDialog.getOpenFileNames(self, 'Open file', 'c\\')
        paths = self.addfiles[0]        
        for path in paths:
            folder, file = os.path.split(path)
            file = (unidecode.unidecode(file)).replace('_', ' ')            
            photoalbum[file] = path 
            self.list.addItem(file)    

    def deleteitem(self):        
        selection = self.list.currentItem().text()
        self.list.takeItem(self.list.row(self.list.currentItem()))
        photoalbum.pop(selection)

    def start(self):        

        for key, val in photoalbum.items(): 

            path, file = os.path.split(val)
            file_nodiacs = unidecode.unidecode(file)
            photo = os.path.join(path, file_nodiacs)      
            os.rename(val, photo)
            self.card.create(photo)
           
            card_RGB = cv2.cvtColor(self.card.face, cv2.COLOR_BGR2RGB)
            card = Image.fromarray(card_RGB)            
            card.save('Cards/ {}'.format(file), 'JPEG')            

            os.rename(photo, val)
           

    def close(self):
        pass
        
        

        
