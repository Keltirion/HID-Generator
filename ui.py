from functions import *
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog, QPushButton, QListWidget,)

photoalbum = {}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.card = CardCreate()
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
        self.closebtn.clicked.connect(self.close)
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
            photo_path = os.path.join(path, file_nodiacs)
            os.rename(val, photo_path)

            image = cv2.imread(photo_path, cv2.IMREAD_COLOR)
            (h, w) = image.shape[0:2]
            if h >= 1080 or w >= 1920:
                self.card.resize(photo=photo_path, width=800)
                self.card.create(self.card.resized_photo)
            else:
                self.card.create(photo_path)
            if self.card.face is not None:
                self.card.face.save('Cards/ {}'.format(file), 'JPEG')
            else:
                print('Potwierdzam dla ' + str(photo_path))

            os.rename(photo_path, val)

    def close(self):
        sys.exit()
