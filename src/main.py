import sys

from PySide2.QtCore import QObject, Signal, Property
from PySide2.QtWidgets import QApplication, QLabel
from PySide2.QtQml import QQmlApplicationEngine
                                                     

if __name__ == "__main__":

    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load("src/qml/main.qml")

    sys.exit(app.exec_())