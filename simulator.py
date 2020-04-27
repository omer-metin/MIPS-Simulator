import time

from PyQt5 import QtWidgets

from gui.simMainScreen import SimMainScreen

app = QtWidgets.QApplication([])
simulator = SimMainScreen()
simulator.show()
app.exec_()
