import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 directory dialogs'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openDirDialog()
        #self.show()

    def openDirDialog(self):
        options = QFileDialog.Options()
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory", options=options))
        if file:
            print(file)
            return file

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

