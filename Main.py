import ScreenController
import sys


from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScreenController.ScreenController()

    sys.exit(app.exec_())

