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
        QtCore.QObject.connect(self.ui.createMonsterButton,QtCore.SIGNAL("clicked()"), self.add_monster)
        QtCore.QObject.connect(self.ui.effectButton,QtCore.SIGNAL("clicked()"), self.set_effects)
        QtCore.QObject.connect(self.ui.healButton,QtCore.SIGNAL("clicked()"), self.heal_hp)
        QtCore.QObject.connect(self.ui.damageButton,QtCore.SIGNAL("clicked()"), self.damage_hp)
        self.ui.encounter.horizontalHeader().setMovable(True)
        self.ui.encounter.horizontalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setMovable(True)

    def add_mob(self):
        currRow = self.ui.encounter.rowCount()
        self.ui.encounter.insertRow(currRow)
    	mobs.append(monsters[self.ui.mobSelect.currentIndex()].addMob())
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 0, item)
        item.setText(_translate("MainWindow", str(mobs[-1].health), None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 1, item)
        item.setText(_translate("MainWindow", str(mobs[-1].maxHP), None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setVerticalHeaderItem(currRow, item)
        item.setText(_translate("MainWindow", mobs[-1].name, None))

    def heal_hp(self):
        healnum = self.ui.hitValue.value()
        row = self.ui.encounter.currentRow()
        mobs[row].health += healnum
        item = self.ui.encounter.item(row, 0)
        item.setText(_translate("MainWindow", str(mobs[row].health), None))
        self.ui.battleLog.addItem(_translate("MainWindow", "%s healed for %s - %s" % (mobs[row].name, healnum, str(self.ui.hitDescription.text())), None))

    def damage_hp(self):
        hitnum = self.ui.hitValue.value()
        row = self.ui.encounter.currentRow()
        mobs[row].health -= hitnum
        item = self.ui.encounter.item(row, 0)
        item.setText(_translate("MainWindow", str(mobs[row].health), None))
        self.ui.battleLog.addItem(_translate("MainWindow", "%s took %s damage - %s" % (mobs[row].name, hitnum, str(self.ui.hitDescription.text())), None))


    def set_effects(self):
    	item = self.ui.encounter.item(0, 5)
        item.setText(_translate("MainWindow", " ", None))
        item = self.ui.encounter.item(0, 4)
        item.setText(_translate("MainWindow", " ", None))

    def add_monster(self):
        dlg = StartMonsterDialog()
        dlg.__init__()
        if dlg.exec_():
            newMonster = dlg.getValues()
            monsters.append(newMonster)
            self.ui.mobSelect.addItem(newMonster.name, None)
            
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