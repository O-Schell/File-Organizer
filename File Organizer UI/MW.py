# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main-Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileOrganizer(object):
    def setupUi(self, FileOrganizer):
        FileOrganizer.setObjectName("FileOrganizer")
        FileOrganizer.resize(800, 227)
        FileOrganizer.setAcceptDrops(False)
        FileOrganizer.setLayoutDirection(QtCore.Qt.LeftToRight)
        FileOrganizer.setAnimated(True)
        FileOrganizer.setDockNestingEnabled(False)
        FileOrganizer.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(FileOrganizer)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(170, 0, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Selectyourfolderbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Selectyourfolderbutton.setGeometry(QtCore.QRect(300, 80, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.Selectyourfolderbutton.setFont(font)
        self.Selectyourfolderbutton.setAutoDefault(True)
        self.Selectyourfolderbutton.setDefault(True)
        self.Selectyourfolderbutton.setFlat(False)
        self.Selectyourfolderbutton.setObjectName("Selectyourfolderbutton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 150, 711, 23))
        self.progressBar.setProperty("value", 24)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileOrganizer = QtWidgets.QMainWindow()
    ui = Ui_FileOrganizer()
    ui.setupUi(FileOrganizer)
    FileOrganizer.show()
    sys.exit(app.exec_())
