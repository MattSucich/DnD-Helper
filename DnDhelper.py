import sys
from PyQt4 import QtCore, QtGui
from MainForm import Ui_MainWindow, _translate
from monsterDialog import Ui_monsterDialog
from monster import Monster, Mob

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.addMobButton,QtCore.SIGNAL("clicked()"), self.add_mob)
        QtCore.QObject.connect(self.ui.createMonsterButton,QtCore.SIGNAL("clicked()"), self.show_dialog)
        QtCore.QObject.connect(self.ui.effectButton,QtCore.SIGNAL("clicked()"), self.set_effects)
        self.ui.encounter.horizontalHeader().setMovable(True)
        self.ui.encounter.horizontalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setMovable(True)

    def add_mob(self):
    	item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(0, 5, item)
        item.setText(_translate("MainWindow", "Paralyzed", None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(0, 4, item)
        item.setText(_translate("MainWindow", "Stunned", None))

    def set_effects(self):
    	item = self.ui.encounter.item(0, 5)
        item.setText(_translate("MainWindow", " ", None))
        item = self.ui.encounter.item(0, 4)
        item.setText(_translate("MainWindow", " ", None))

    def show_dialog(self):
        dlg = StartMonsterDialog()
        dlg.__init__()
        if dlg.exec_():
            newMonster = dlg.getValues()
            monsters.append(newMonster)
            self.ui.mobSelect.addItem(monsters[len(monsters)-1].name, None)
            print newMonster.name
            print newMonster.dicesize
            print newMonster.dicenum
            print newMonster.hpmod
            self.ui.mobInfo.setPlainText(newMonster.desc)
        

class StartMonsterDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_monsterDialog()
        self.ui.setupUi(self)

    def getValues(self):
        return Monster(self.ui.nameLine.text(), int(self.ui.numDice.text()), int(self.ui.dieSize.text()), int(self.ui.hitDiceMod.text()), self.ui.descriptionBox.toPlainText())


if __name__ == "__main__":
    monsters = []
    mobs = []

    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()


    sys.exit(app.exec_())


    """
    self.encounter.horizontalHeader().setMovable(True)
    self.encounter.horizontalHeader().setResizeMode(3)
    self.encounter.verticalHeader().setMovable(True)
    """