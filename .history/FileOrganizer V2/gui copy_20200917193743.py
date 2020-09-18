import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from lib import organize_folder


class Ui_FileOrganizer(object):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    central_widget = QtWidgets.QWidget()
    self.setCentralWidget(central_widget)

    def setupUi(self, FileOrganizer):
        self.setWindowTitle(self.tr("File-Organizer"))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(20)

        self.title = QtWidgets.QLabel(self.tr("Welcome into File-Organizer !"), alignment=QtCore.Qt.AlignCenter)
        self.title.setFont(font)

        self.button = QtWidgets.QPushButton(self.tr("Select your folder"))
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(300, 80, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.button.setFont(font)
        self.button.setFixedSize(160, 40)
        self.button.setFont(font)
        self.button.setAutoDefault(True)
        self.button.setDefault(True)
        self.button.setFlat(False)


        self.progressbar = QtWidgets.QProgressBar(self, alignment=QtCore.Qt.AlignCenter)
        self.progressbar.setFixedSize(300, 40)
        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setGeometry(QtCore.QRect(50, 150, 711, 23))
        self.progressBar.setObjectName("progressBar")
        self.progressbar

        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.setContentsMargins(0, 10, 0, 0)
        lay.setSpacing(60)
        lay.addWidget(self.title)
        lay.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        lay.addWidget(self.progressbar, alignment=QtCore.Qt.AlignCenter)
        lay.addStretch()

        self.resize(600, 250)

        self.button.clicked.connect(self.onClicked)
        self.started.connect(self.onStarted)
        self.finished.connect(self.onFinished)

    @QtCore.pyqtSlot()
    def onClicked(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Select Directory",
            QtCore.QStandardPaths.writableLocation(
                QtCore.QStandardPaths.DownloadLocation
            ),
        )
        if directory:
            threading.Thread(
                target=self.organize_folder, args=(directory,), daemon=True
            ).start()

    def organize_folder(self, directory):
        self.started.emit()
        organize_folder(directory)
        self.finished.emit()


    @QtCore.pyqtSlot()
    def onStarted(self):
        self.progressbar.setRange(0, 0)

    @QtCore.pyqtSlot()
    def onFinished(self):
        self.progressbar.setRange(0, 1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FileOrganizer = QtWidgets.QMainWindow()
    ui = Ui_FileOrganizer()
    ui.setupUi(FileOrganizer)
    FileOrganizer.show()
    sys.exit(app.exec_())