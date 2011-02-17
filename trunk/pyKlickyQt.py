#!/usr/bin/env python

import sys
import os
import time
import logging
from random import randint
from PySide import QtCore, QtGui
from PySide.QtGui import QImage, QPixmap, QGraphicsScene, QMainWindow, QSound
from Ui_MainWindow import Ui_MainWindow
from pyKlicky import Helper, History
from sound import Sound
from stats import Stats
import settings


class pyKlickyQt(QMainWindow, Ui_MainWindow):
    _helper = None
    history = History()
    border = 5
    stat = Stats()

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.connect(self.btnNext, QtCore.SIGNAL("clicked()"), self.next_clicked)
        self.connect(self.btnPrev, QtCore.SIGNAL("clicked()"), self.previous_clicked)

        self.connect(self.btnChoice1, QtCore.SIGNAL("clicked()"), self.choice1_clicked)
        self.connect(self.btnChoice2, QtCore.SIGNAL("clicked()"), self.choice2_clicked)
        self.connect(self.editAnswer, QtCore.SIGNAL("returnPressed()"), self.answer_typed)
        # TODO: FIX
        # self.connect(self.imgView, QtCore.SIGNAL("XXX()"), self.img_resized)
        self.connect(self.labelAnswer, QtCore.SIGNAL("clicked()"), self.labelAnswer_clicked)

        self.sound = Sound()

        try:
            self.next_clicked()
        except IOError:
            # TODO: Add Popup
            print "Unable to read data folder", settings.Folder.data

    @property
    def helper(self):
        if not self._helper:
            self._helper = Helper()

        return self._helper

    def get_optimal_size(self):
        return (self.imgView.size().width() - self.border, \
                self.imgView.size().height() - self.border)

    def img_resized(self):
        print "resized"

    def labelAnswer_clicked(self):
        self.sound.read_word(self.answer)
        self.sound.spell(self.answer)

    def load_img(self, img):
        image = QtGui.QImage(img)
        x, y = self.get_optimal_size()
        image = image.scaled(x, y, QtCore.Qt.KeepAspectRatio)
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(image))
        self.imgView.setScene(scene)
        self.imgChoose.setScene(scene)
        self.imgWrite.setScene(scene)

        cur = self.helper.extract_word(self.history.current)

        self.labelAnswer.setText(cur)
        self.progressBar.setValue(self.stat.mean_percent)

        if randint(0, 1):
            self.btnChoice1.setText(self.helper.get_random_word())
            self.btnChoice2.setText(cur)
        else:
            self.btnChoice1.setText(cur)
            self.btnChoice2.setText(self.helper.get_random_word())

        if self.tabWidget.currentIndex() == 0:
            self.sound.read_word(self.answer)
            self.sound.spell(self.answer)

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
        correct = self.is_correct_answer(answer.text())
        answer.setText(str(correct))
        if correct:
            self.correct_answer()
        else:
            self.incorrect_answer()

    def answer_typed(self):
        correct = self.is_correct_answer(self.editAnswer.text())

        if correct:
            self.editAnswer.setText('')
            self.correct_answer()
        else:
            self.incorrect_answer()

    @property
    def answer(self):
        return self.helper.extract_word(self.history.current)

    def is_correct_answer(self, answer):
        return answer == self.answer

    def correct_answer(self):
        if self.sound:
            self.sound.play_correct()

        self.stat.correct += 1

        # TODO add some visual feedback
        self.next_clicked()


    def incorrect_answer(self):
        if self.sound:
            self.sound.play_incorrect()

        self.stat.incorrect += 1

        # TODO add some visual feedback
        self.next_clicked()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = pyKlickyQt()
    w.show()
    app.exec_()
