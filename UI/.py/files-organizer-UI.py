import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileOrganizer(object):
    def setupUi(self, FileOrganizer):
        FileOrganizer.setObjectName("FileOrganizer")
        FileOrganizer.resize(800, 598)
        FileOrganizer.setAcceptDrops(False)
        FileOrganizer.setLayoutDirection(QtCore.Qt.LeftToRight)
        FileOrganizer.setAnimated(True)
        FileOrganizer.setDockNestingEnabled(False)
        FileOrganizer.setUnifiedTitleAndToolBarOnMac(False)

        self.centralwidget = QtWidgets.QWidget(FileOrganizer)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(170, 10, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")

        self.Selectyourfolderbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Selectyourfolderbutton.setGeometry(QtCore.QRect(310, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.Selectyourfolderbutton.setFont(font)
        self.Selectyourfolderbutton.setAutoDefault(True)
        self.Selectyourfolderbutton.setDefault(True)
        self.Selectyourfolderbutton.setFlat(False)
        self.Selectyourfolderbutton.setObjectName("Selectyourfolderbutton")
        FileOrganizer.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(FileOrganizer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        FileOrganizer.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(FileOrganizer)
        self.statusbar.setObjectName("statusbar")
        FileOrganizer.setStatusBar(self.statusbar)

        self.retranslateUi(FileOrganizer)
        QtCore.QMetaObject.connectSlotsByName(FileOrganizer)

        self.Selectyourfolderbutton.clicked.connect(self.click)
    def click(self):
        import FolderSelect

        self.ex = App()

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


