#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui
from PySide.QtGui import QImage, QPixmap, QGraphicsScene, QMainWindow
from Ui_MainWindow import Ui_MainWindow
from pyKlicky import Helper, History

class pyKlickyQt(QMainWindow, Ui_MainWindow):
    _helper = None
    history = History()

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.connect(self.btnNext, QtCore.SIGNAL("clicked()"), self.next_clicked)
        self.connect(self.btnPrev, QtCore.SIGNAL("clicked()"), self.previous_clicked)
        self.connect(self.btnChoice1, QtCore.SIGNAL("clicked()"), self.choice1_clicked)
        self.connect(self.btnChoice2, QtCore.SIGNAL("clicked()"), self.choice2_clicked)

        try:
            self.next_clicked()
        except IOError:
            # TODO: Add Popup
            print "Unable to read data folder"

    @property
    def helper(self):
        if not self._helper:
            self._helper = Helper()

        return self._helper

    def get_optimal_size(self, image):
        return (200, 200)

    def load_img(self, img):
        print img
        image = QtGui.QImage(img)
        x, y = self.get_optimal_size(image)

        image = image.scaled(x, y, QtCore.Qt.KeepAspectRatio)

        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(image))
        self.imgView.setScene(scene)
        self.imgChoose.setScene(scene)
        self.imgWrite.setScene(scene)

    def next_clicked(self):
        if self.history.is_last():
            img = self.helper.get_random_image()
            self.history.add(img)
            self.load_img(self.history.current)
        else:
            self.load_img(self.history.next())


    def previous_clicked(self):
        if not self.history.is_first():
            self.load_img(self.history.previous())

    def choice1_clicked(self):
        self.choice_clicked(self.btnChoice1)

    def choice2_clicked(self):
        self.choice_clicked(self.btnChoice2)

    def choice_clicked(self, answer):
        raise NotImplementedError


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = pyKlickyQt()
    w.show()
    app.exec_()
