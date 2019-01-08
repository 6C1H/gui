import sys
from pprint import pprint
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui,QtCore

class TutorialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test')
        self.setWindowIcon(QIcon('virus.png'))
        menuBar = self.menuBar()
        

        file_menu = menuBar.addMenu('&File')
        exit_action = QAction(QIcon('icon_exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program')
        exit_action.triggered.connect(self.close_app)
        file_menu.addAction(exit_action)
        self.setGeometry(600, 200, 800, 800)
    def close_app(self):
        choice=QMessageBox.question(self,'Quit',"Are you Sure Want to Quit?",QMessageBox.Yes | QMessageBox.No)
        if choice==QMessageBox.Yes:
            sys.exit()
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())