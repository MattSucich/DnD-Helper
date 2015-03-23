import sys
from PyQt4 import QtCore, QtGui
from MainForm import Ui_MainWindow, _translate
from monsterDialog import Ui_monsterDialog
from monster import Monster, Mob

class StartQT4(QtGui.QMainWindow):
    statDict = {
    0   :   " ",
    1   :   "Blinded",
    2   :   "Charmed",
    3   :   "Frightened",
    4   :   "Grappled",
    5   :   "Incapacitated",
    6   :   "Incorporeal",
    7   :   "Paralyzed",
    8   :   "Petrified",
    9   :   "Prone",
    10  :   "Restrained",
    11  :   "Stunned"
    }
    sortVisibility = False

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.addMobButton,QtCore.SIGNAL("clicked()"), self.add_mob)
        QtCore.QObject.connect(self.ui.createMonsterButton,QtCore.SIGNAL("clicked()"), self.add_monster)
        QtCore.QObject.connect(self.ui.effectButton,QtCore.SIGNAL("clicked()"), self.set_effects)
        QtCore.QObject.connect(self.ui.reorderButton,QtCore.SIGNAL("clicked()"), self.toggle_sort)
        QtCore.QObject.connect(self.ui.healButton,QtCore.SIGNAL("clicked()"), self.heal_hp)
        QtCore.QObject.connect(self.ui.damageButton,QtCore.SIGNAL("clicked()"), self.damage_hp)
        QtCore.QObject.connect(self.ui.encounter, QtCore.SIGNAL("itemSelectionChanged()"), self.get_effects)
        #QtCore.QObject.connect(self.ui.encounter.verticalHeader(), QtCore.SIGNAL("sectionClicked(int)"), self.get_effect)
        self.ui.encounter.horizontalHeader().setMovable(True)
        self.ui.encounter.horizontalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setMovable(True)

    def add_mob(self):
        currRow = self.ui.encounter.rowCount()
        self.ui.encounter.insertRow(currRow)
        theMonster = self.ui.mobSelect.currentIndex()
    	mobs.append(monsters[theMonster].addMob(theMonster))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 0, item)
        item.setText(_translate("MainWindow", mobs[-1].name, None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 1, item)
        item.setText(_translate("MainWindow", str(mobs[-1].health), None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 2, item)
        item.setText(_translate("MainWindow", str(mobs[-1].maxHP), None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 3, item)
        item.setText(_translate("MainWindow", 'yes', None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 4, item)
        item.setText(_translate("MainWindow", ' ', None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 5, item)
        item.setText(_translate("MainWindow", ' ', None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 6, item)
        item.setText(_translate("MainWindow", ' ', None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 7, item)
        item.setText(_translate("MainWindow", ' ', None))
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setVerticalHeaderItem(currRow, item)
        item.setText(_translate("MainWindow", " -> ", None))
    
    def heal_hp(self):
        healnum = self.ui.hitValue.value()
        row = self.ui.encounter.currentRow()
        mobs[row].health += healnum
        item = self.ui.encounter.item(row, 1)
        item.setText(_translate("MainWindow", str(mobs[row].health), None))
        self.ui.battleLog.addItem(_translate("MainWindow", "%s healed for %s hp - %s" % (mobs[row].name, healnum, str(self.ui.hitDescription.text())), None))

    def damage_hp(self):
        hitnum = self.ui.hitValue.value()
        row = self.ui.encounter.currentRow()
        mobs[row].health -= hitnum
        item = self.ui.encounter.item(row, 1)
        item.setText(_translate("MainWindow", str(mobs[row].health), None))
        self.ui.battleLog.addItem(_translate("MainWindow", "%s took %s damage - %s" % (mobs[row].name, hitnum, str(self.ui.hitDescription.text())), None))
    """
    def get_effect(self, row):
        self.get_effects(row, 0)
    """
    def get_effects(self):
        ranges = self.ui.encounter.selectedRanges()
        self.ui.rechargeBox.setChecked(False)
        self.ui.status1Box.setCurrentIndex(0)
        self.ui.status2Box.setCurrentIndex(0)
        self.ui.status3Box.setCurrentIndex(0)
        self.ui.status4Box.setCurrentIndex(0)
        self.ui.mobInfo.setPlainText(" ")
        for rows in ranges:
            self.ui.encounter.setRangeSelected(QtGui.QTableWidgetSelectionRange(rows.topRow(), 0, rows.bottomRow(), 8), True)
        if len(ranges) == 1 and ranges[0].rowCount() == 1:
            row = ranges[0].topRow()
            if mobs[row].recharge == 1:
                self.ui.rechargeBox.setChecked(True)
            else:
                self.ui.rechargeBox.setChecked(False)
            self.ui.status1Box.setCurrentIndex(mobs[row].statuses[0])
            self.ui.status2Box.setCurrentIndex(mobs[row].statuses[1])
            self.ui.status3Box.setCurrentIndex(mobs[row].statuses[2])
            self.ui.status4Box.setCurrentIndex(mobs[row].statuses[3])
            self.ui.mobInfo.setPlainText(monsters[mobs[row].parent].desc)

    def toggle_sort(self):
        self.sortVisibility = not self.sortVisibility
        self.ui.encounter.verticalHeader().setVisible(self.sortVisibility)


    def set_effects(self):
        row = self.ui.encounter.currentRow()
        if self.ui.rechargeBox.isChecked():
            mobs[row].recharge = 1
            item = self.ui.encounter.item(row, 3)
            item.setText(_translate("MainWindow", 'yes', None))
            print "noo"
        else:
            mobs[row].recharge = 0
            item = self.ui.encounter.item(row, 3)
            item.setText(_translate("MainWindow", 'no', None))
            print "yesss"
    	mobs[row].statuses[0] = self.ui.status1Box.currentIndex()
        mobs[row].statuses[1] = self.ui.status2Box.currentIndex()
        mobs[row].statuses[2] = self.ui.status3Box.currentIndex()
        mobs[row].statuses[3] = self.ui.status4Box.currentIndex()
        y = ''
        for x in range(4):
            item = self.ui.encounter.item(row, x+4)
            item.setText(_translate("MainWindow", self.statDict[mobs[row].statuses[x]], None))
            if mobs[row].statuses[x]:
                if y == '':
                    y = self.statDict[mobs[row].statuses[x]]
                else:
                    y = y + ", " + self.statDict[mobs[row].statuses[x]]
        if y == '':
            self.ui.battleLog.addItem(_translate("MainWindow", "%s no longer has any ongoing effects" % (mobs[row].name), None))
        else:
            self.ui.battleLog.addItem(_translate("MainWindow", "%s is now: %s." % (mobs[row].name, y), None))

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


    