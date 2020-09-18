import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from lib import organize_folder


class MainWindow(QtWidgets.QMainWindow):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(self.tr("File-Organizer"))
        font = QtGui.QFont()
        font.setFamily("Panton Light Caps")
        font.setPointSize(25)

        self.title = QtWidgets.QLabel(
            self.tr("Welcome into File-Organizer !"), alignment=QtCore.Qt.AlignCenter
        )
        self.title.setFont(font)
        self.title.setGeometry(QtCore.QRect(200, 0, 450, 60))

        self.button = QtWidgets.QPushButton(self.tr("Select your folder"))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(12)
        self.button.setFont(font)
        self.button.setFixedSize(160, 40)

        self.progressbar = QtWidgets.QProgressBar()
        self.progressbar.setFixedSize(300, 40)
        self.progressbar.QtCore.QRect(50, 150, 700, 20))

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.setContentsMargins(0, 10, 0, 0)
        lay.setSpacing(60)
        lay.addWidget(self.title)
        lay.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        lay.addWidget(self.progressbar, alignment=QtCore.Qt.AlignCenter)
        lay.addStretch()

        self.resize(800, 200)

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
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())