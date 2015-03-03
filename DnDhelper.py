import sys
from PyQt4 import QtCore, QtGui
from MainForm import Ui_MainWindow, _translate

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.addMobButton,QtCore.SIGNAL("clicked()"), self.add_mob)
        QtCore.QObject.connect(self.ui.createMonsterButton,QtCore.SIGNAL("clicked()"), self.fuckshit)
        self.ui.encounter.horizontalHeader().setMovable(True)
        self.ui.encounter.horizontalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setMovable(True)

    def add_mob(self):
    	item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(0, 5, item)
        item.setText(_translate("MainWindow", "Paralyzed123sad", None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(0, 4, item)
        item.setText(_translate("MainWindow", "Stunned", None))

    def fuckshit(self):
    	item = self.ui.encounter.item(0, 5)
        item.setText(_translate("MainWindow", " ", None))
        item = self.ui.encounter.item(0, 4)
        item.setText(_translate("MainWindow", " ", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()

    sys.exit(app.exec_())


    """
    self.encounter.horizontalHeader().setMovable(True)
    self.encounter.horizontalHeader().setResizeMode(3)
    self.encounter.verticalHeader().setMovable(True)
    """