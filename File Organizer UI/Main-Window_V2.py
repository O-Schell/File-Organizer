# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main-Window_V2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileOrganizer(object):
    def setupUi(self, FileOrganizer):
        FileOrganizer.setObjectName("FileOrganizer")
        FileOrganizer.resize(800, 200)
        FileOrganizer.setAcceptDrops(False)
        FileOrganizer.setLayoutDirection(QtCore.Qt.LeftToRight)
        FileOrganizer.setAnimated(True)
        FileOrganizer.setDockNestingEnabled(False)
        FileOrganizer.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(FileOrganizer)
        self.centralwidget.setObjectName("centralwidget")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(200, 0, 450, 60))
        font = QtGui.QFont()
        font.setFamily("Panton Light Caps")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        self.Selectyourfolderbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Selectyourfolderbutton.setGeometry(QtCore.QRect(320, 80, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.Selectyourfolderbutton.setFont(font)
        self.Selectyourfolderbutton.setAutoDefault(True)
        self.Selectyourfolderbutton.setDefault(True)
        self.Selectyourfolderbutton.setFlat(False)
        self.Selectyourfolderbutton.setObjectName("Selectyourfolderbutton")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 150, 700, 20))
        self.progressBar.setObjectName("progressBar")
        FileOrganizer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FileOrganizer)
        self.statusbar.setObjectName("statusbar")
        FileOrganizer.setStatusBar(self.statusbar)

        self.retranslateUi(FileOrganizer)
        QtCore.QMetaObject.connectSlotsByName(FileOrganizer)

    def retranslateUi(self, FileOrganizer):
        _translate = QtCore.QCoreApplication.translate
        FileOrganizer.setWindowTitle(_translate("FileOrganizer", "File-Organizer"))
        self.Title.setText(_translate("FileOrganizer", "Welcome into File-Organizer !"))
        self.Selectyourfolderbutton.setText(_translate("FileOrganizer", "Select your folder"))
