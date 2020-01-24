import sys
from PyQt5.QtQml import QQmlApplicationEngine

from PySide2.QtWidgets import QApplication, QLabel
                                                     

if __name__ == "__main__":

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load("src/qml/main.qml")

    sys.exit(app.exec_())