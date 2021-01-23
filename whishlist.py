#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json

class DatabaseConnector:

    def __init__(self):

        pass

    def get_all(self):

        # sql config

        return []

class WishList(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.db = DatabaseConnector()

        self.initList()

        self.initOthers()

        self.setLayout(self.grid)

    def initUI(self):

        self.setGeometry(300, 300, 500, 800)
        self.setWindowTitle('WishList')
        self.setWindowIcon(QIcon('list.png'))

        self.listwidget = QListWidget()

        self.show()

    def initList(self):
        self.listCheckBox = self.db.get_all()

        self.grid = QGridLayout()

        for i, v in enumerate(self.listCheckBox):
            self.listCheckBox[i] = QCheckBox(v)
            self.grid.addWidget(self.listCheckBox[i], i, 0)

        print(self.listCheckBox)
        print()

    def initOthers(self):

        self.button_add = QPushButton('Добавить запись', self)
        self.button_add.clicked.connect(self.new_item)

        self.item_name = QLineEdit()

        self.item_price = QLineEdit()

        self.item_link = QLineEdit()

        list_size = len(self.listCheckBox)
        self.grid.addWidget(self.item_name, list_size + 1, 0)
        self.grid.addWidget(self.item_price, list_size + 1, 1)
        self.grid.addWidget(self.item_link, list_size + 2, 0, 1, 2)
        self.grid.addWidget(self.button_add, list_size + 3, 0, 1, 2)

    @pyqtSlot()
    def new_item(self):
        all_info = {"Name": self.item_name.text(),
                    "Price": self.item_price.text(),
                    "Link": self.item_link.text()}
        for i in all_info.items():
            print(i[0], i[1])

        self.initList()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = WishList()
    sys.exit(app.exec_())
