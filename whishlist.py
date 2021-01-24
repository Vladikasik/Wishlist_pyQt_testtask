#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3


class DatabaseConnector:

    def __init__(self):

        self.conn = sqlite3.connect("wishlist.db")
        self.c = self.conn.cursor()

    def get_all(self):

        names = self.c.execute(
            "SELECT itemname FROM wishlist ORDER BY itemname")
        names = list(names)
        prices = self.c.execute(
            "SELECT itemprice FROM wishlist ORDER BY itemname")
        prices = list(prices)
        links = self.c.execute(
            "SELECT itemlink FROM wishlist ORDER BY itemname")
        links = list(links)
        data_to_return = {
            "names": names,
            "prices": prices,
            "links": links,
        }
        return data_to_return

    def add_item(self, all_info):
        passs

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

        self.database_data = self.db.get_all()

        print(self.database_data)

        self.listNames = self.database_data["names"]
        self.listPrices = self.database_data["prices"]
        self.listLinks = self.database_data["links"]

        self.listCheckBox = []
        self.listLabelPrice = []
        self.listLabelLink = []

        self.grid = QGridLayout()

        for i, v in enumerate(self.listNames):
            self.listCheckBox.append(QCheckBox(v[0]))
            self.grid.addWidget(self.listCheckBox[i], i, 0)
            print(self.listCheckBox[i], i, 0)

        for i, v in enumerate(self.listPrices):
            self.listLabelPrice.append(QLabel(str(v[0])))
            self.grid.addWidget(self.listLabelPrice[i], i, 1)

        for i, v in enumerate(self.listLinks):
            self.listLabelLink.append(QLabel(v[0]))
            self.grid.addWidget(self.listLabelLink[i], i, 2)

        print()

    def initOthers(self):

        self.button_add = QPushButton('Добавить запись', self)
        self.button_add.clicked.connect(self.new_item)

        self.item_name = QLineEdit()

        self.item_price = QLineEdit()

        self.item_link = QLineEdit()

        list_size = len(self.listCheckBox)
        self.grid.addWidget(self.item_name, list_size + 1, 0, 1, 2)
        self.grid.addWidget(self.item_price, list_size + 1, 2)
        self.grid.addWidget(self.item_link, list_size + 2, 0, 1, 3)
        self.grid.addWidget(self.button_add, list_size + 3, 0, 1, 3)

    @ pyqtSlot()
    def new_item(self):
        all_info = {"Name": self.item_name.text(),
                    "Price": int(self.item_price.text()),
                    "Link": self.item_link.text()}
        for i in all_info.items():
            print(i[0], i[1])

        self.db.add_item(all_info)

        self.initList()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = WishList()
    sys.exit(app.exec_())
