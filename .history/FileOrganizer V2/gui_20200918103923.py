import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from lib import organize_folder


class MainWindow(QtWidgets.QMainWindow):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(self.tr("File-Organizer"))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 200)
        MainWindow.setAcceptDrops(False)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)

        font = QtGui.QFont()
        font.setFamily("Panton Light Caps")
        font.setPointSize(20)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(200, 0, 450, 60))

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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File-Organizer"))
        self.Title.setText(_translate("MainWindow", "Welcome into File-Organizer !"))
        self.Selectyourfolderbutton.setText(_translate("MainWindow", "Select your folder"))
