import sys
from pprint import pprint
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class TutorialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test')
        menuBar = self.menuBar()
        

        file_menu = menuBar.addMenu('&File')
        exit_action = QAction(QIcon('icon_exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)
        self.setGeometry(600, 200, 800, 800)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())