# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Feb  3 20:04:47 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 489)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnNext = QtGui.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout_2.addWidget(self.btnNext, 2, 5, 1, 1)
        self.btnPrev = QtGui.QPushButton(self.centralwidget)
        self.btnPrev.setObjectName("btnPrev")
        self.gridLayout_2.addWidget(self.btnPrev, 2, 3, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_view = QtGui.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imgView = QtGui.QGraphicsView(self.tab_view)
        self.imgView.setObjectName("imgView")
        self.verticalLayout.addWidget(self.imgView)
        self.labelAnswer = QtGui.QLabel(self.tab_view)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.labelAnswer.setFont(font)
        self.labelAnswer.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAnswer.setObjectName("labelAnswer")
        self.verticalLayout.addWidget(self.labelAnswer)
        self.tabWidget.addTab(self.tab_view, "")
        self.tab_choose = QtGui.QWidget()
        self.tab_choose.setObjectName("tab_choose")
        self.gridLayout = QtGui.QGridLayout(self.tab_choose)
        self.gridLayout.setObjectName("gridLayout")
        self.imgChoose = QtGui.QGraphicsView(self.tab_choose)
        self.imgChoose.setObjectName("imgChoose")
        self.gridLayout.addWidget(self.imgChoose, 0, 0, 1, 2)
        self.btnChoice2 = QtGui.QPushButton(self.tab_choose)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnChoice2.setFont(font)
        self.btnChoice2.setObjectName("btnChoice2")
        self.gridLayout.addWidget(self.btnChoice2, 1, 1, 1, 1)
        self.btnChoice1 = QtGui.QPushButton(self.tab_choose)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnChoice1.setFont(font)
        self.btnChoice1.setObjectName("btnChoice1")
        self.gridLayout.addWidget(self.btnChoice1, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_choose, "")
        self.tab_write = QtGui.QWidget()
        self.tab_write.setObjectName("tab_write")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_write)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imgWrite = QtGui.QGraphicsView(self.tab_write)
        self.imgWrite.setObjectName("imgWrite")
        self.verticalLayout_3.addWidget(self.imgWrite)
        self.editAnswer = QtGui.QLineEdit(self.tab_write)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.editAnswer.setFont(font)
        self.editAnswer.setInputMask("")
        self.editAnswer.setText("")
        self.editAnswer.setObjectName("editAnswer")
        self.verticalLayout_3.addWidget(self.editAnswer)
        self.tabWidget.addTab(self.tab_write, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 5)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 25))
        self.menubar.setObjectName("menubar")
        self.menuHighscore = QtGui.QMenu(self.menubar)
        self.menuHighscore.setObjectName("menuHighscore")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPackages = QtGui.QMenu(self.menubar)
        self.menuPackages.setObjectName("menuPackages")
        self.menuRecent_packages = QtGui.QMenu(self.menuPackages)
        self.menuRecent_packages.setObjectName("menuRecent_packages")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuSound = QtGui.QMenu(self.menuSettings)
        self.menuSound.setObjectName("menuSound")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIconVisibleInMenu(False)
        self.actionAbout.setObjectName("actionAbout")
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDelete_picture = QtGui.QAction(MainWindow)
        self.actionDelete_picture.setObjectName("actionDelete_picture")
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionImport_2 = QtGui.QAction(MainWindow)
        self.actionImport_2.setObjectName("actionImport_2")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionExport_2 = QtGui.QAction(MainWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionClear = QtGui.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionRead = QtGui.QAction(MainWindow)
        self.actionRead.setCheckable(True)
        self.actionRead.setChecked(True)
        self.actionRead.setObjectName("actionRead")
        self.actionSpell = QtGui.QAction(MainWindow)
        self.actionSpell.setCheckable(True)
        self.actionSpell.setChecked(True)
        self.actionSpell.setObjectName("actionSpell")
        self.actionSound_effects = QtGui.QAction(MainWindow)
        self.actionSound_effects.setCheckable(True)
        self.actionSound_effects.setChecked(True)
        self.actionSound_effects.setObjectName("actionSound_effects")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHighscore.addAction(self.actionLoad)
        self.menuHighscore.addAction(self.actionSave)
        self.menuHighscore.addSeparator()
        self.menuHighscore.addAction(self.actionImport_2)
        self.menuHighscore.addAction(self.actionExport)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuRecent_packages.addSeparator()
        self.menuRecent_packages.addAction(self.actionClear)
        self.menuPackages.addAction(self.actionOpen)
        self.menuPackages.addAction(self.menuRecent_packages.menuAction())
        self.menuPackages.addSeparator()
        self.menuPackages.addAction(self.actionImport)
        self.menuPackages.addAction(self.actionExport_2)
        self.menuPackages.addSeparator()
        self.menuPackages.addAction(self.actionQuit)
        self.menuSound.addAction(self.actionRead)
        self.menuSound.addAction(self.actionSpell)
        self.menuSound.addAction(self.actionSound_effects)
        self.menuSettings.addAction(self.menuSound.menuAction())
        self.menubar.addAction(self.menuPackages.menuAction())
        self.menubar.addAction(self.menuHighscore.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNext.setText(QtGui.QApplication.translate("MainWindow", "Next >", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPrev.setText(QtGui.QApplication.translate("MainWindow", "< Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAnswer.setText(QtGui.QApplication.translate("MainWindow", "Answer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_view), QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChoice2.setText(QtGui.QApplication.translate("MainWindow", "Choice 2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnChoice1.setText(QtGui.QApplication.translate("MainWindow", "Choice 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_choose), QtGui.QApplication.translate("MainWindow", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.editAnswer.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Type Answer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_write), QtGui.QApplication.translate("MainWindow", "Write", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHighscore.setTitle(QtGui.QApplication.translate("MainWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPackages.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRecent_packages.setTitle(QtGui.QApplication.translate("MainWindow", "Recent packages", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSound.setTitle(QtGui.QApplication.translate("MainWindow", "Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_picture.setText(QtGui.QApplication.translate("MainWindow", "Delete picture", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_2.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_2.setText(QtGui.QApplication.translate("MainWindow", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRead.setText(QtGui.QApplication.translate("MainWindow", "Read", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSpell.setText(QtGui.QApplication.translate("MainWindow", "Spell", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSound_effects.setText(QtGui.QApplication.translate("MainWindow", "Sound effects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))

