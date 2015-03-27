import sys
import ast
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
    renameFlag = True

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
        QtCore.QObject.connect(self.ui.deleteButton,QtCore.SIGNAL("clicked()"), self.delete_mobs)
        QtCore.QObject.connect(self.ui.encounter, QtCore.SIGNAL("itemSelectionChanged()"), self.get_effects)
        QtCore.QObject.connect(self.ui.encounter, QtCore.SIGNAL("cellChanged(int,int)"), self.get_rename)
        QtCore.QObject.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.save_all)
        QtCore.QObject.connect(self.ui.actionLoad, QtCore.SIGNAL("triggered()"), self.load_all)
        self.ui.encounter.horizontalHeader().setMovable(True)
        self.ui.encounter.horizontalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setResizeMode(3)
        self.ui.encounter.verticalHeader().setMovable(True)

    def add_mob(self):
        theMonster = self.ui.mobSelect.currentIndex()
        mobs.append(monsters[theMonster].addMob(theMonster))
        self.populate_mob()

    def populate_mob(self):
        self.renameFlag = False
        currRow = self.ui.encounter.rowCount()
        self.ui.encounter.insertRow(currRow)
        #print mobs[-1].__dict__ #for use in saving/loading, it's basic json shit.
        
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 0, item)
        item.setText(mobs[-1].name)
        
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 1, item)
        item.setText("%s/%s" % (mobs[-1].health, mobs[-1].maxHP))
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )

        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 2, item)
        item.setText('yes')
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )

        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 3, item)
        item.setIcon(QtGui.QIcon('asdf.png'))
        item.setText("Fuck you")
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )

        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 4, item)
        item.setIcon(QtGui.QIcon('asdf.png'))
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )

        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 5, item)
        item.setIcon(QtGui.QIcon('asdf.png'))
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
        
        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setItem(currRow, 6, item)
        item.setIcon(QtGui.QIcon('asdf.png')) #placeholders
        item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )

        item = QtGui.QTableWidgetItem()
        self.ui.encounter.setVerticalHeaderItem(currRow, item)
        item.setText(_translate("MainWindow", " -> ", None))
        
        self.ui.encounter.verticalHeader().setVisible(self.sortVisibility)
        self.renameFlag = True
    
    def heal_hp(self):
        healnum = self.ui.hitValue.value()
        ranges = self.ui.encounter.selectedRanges()
        names = []
        for rows in ranges:
            for row in range(rows.topRow(), rows.bottomRow() +1):
                names.append(mobs[row].name)
                mobs[row].health += healnum
                item = self.ui.encounter.item(row, 1)
                item.setText("%s/%s" % (mobs[row].health, mobs[row].maxHP))
        if len(names) != 0:
            s = ', '.join(names)
            details = str(self.ui.hitDescription.text())
            if len(details) > 0:
                self.ui.battleLog.addItem("%s healed for %s hp - %s" % (mobs[row].name, healnum, details))
            else:
                self.ui.battleLog.addItem("%s healed for %s hp!" % (mobs[row].name, healnum))
    def damage_hp(self):
        hitnum = self.ui.hitValue.value()
        ranges = self.ui.encounter.selectedRanges()
        names = []
        death = [0] * len(mobs)
        for rows in ranges:
            for row in range(rows.topRow(), rows.bottomRow() +1):
                names.append(mobs[row].name)
                mobs[row].health -= hitnum
                if mobs[row].health <= 0:
                    death[row] = 1
                item = self.ui.encounter.item(row, 1)
                item.setText("%s/%s" % (mobs[row].health, mobs[row].maxHP))
        if len(names) != 0:
            s = ', '.join(names)
            details = str(self.ui.hitDescription.text())
            if len(details) > 0:
                self.ui.battleLog.addItem("%s took %s damage - %s" % (s, hitnum, details))
            else:
                self.ui.battleLog.addItem("%s took %s damage!" % (s, hitnum))
            names = []
            for x in range(0, len(death)): 
                if death[x] == 1:
                    names.append(mobs[x].name)
                    self.delete_mob(x)
            if len(names) > 0:
                s = ', '.join(names)
                self.ui.battleLog.addItem("%s died!" % (s))

    def get_rename(self, row, col):
        if col == 0 and self.renameFlag:
            mobs[row].name = str(self.ui.encounter.item(row, col).text())
    
    def get_effects(self):
        ranges = self.ui.encounter.selectedRanges()
        self.ui.rechargeBox.setChecked(False)
        self.ui.status1Box.setCurrentIndex(0)
        self.ui.status2Box.setCurrentIndex(0)
        self.ui.status3Box.setCurrentIndex(0)
        self.ui.status4Box.setCurrentIndex(0)
        self.ui.mobInfo.setPlainText("Select a mob from the table to see information here. \n\nIf you select multiple mobs, they must be the same type.")
        same = -2
        for rows in ranges:
            self.ui.encounter.setRangeSelected(QtGui.QTableWidgetSelectionRange(rows.topRow(), 0, rows.bottomRow(), 7), True)
            for row in range(rows.topRow(), rows.bottomRow() +1):
                if same == -2:
                    same = mobs[row].parent
                elif same != mobs[row].parent:
                    same = -1
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
        if same >= 0:
            self.ui.mobInfo.setPlainText(monsters[mobs[ranges[0].topRow()].parent].desc)

    def toggle_sort(self):
        self.sortVisibility = not self.sortVisibility
        self.ui.encounter.verticalHeader().setVisible(self.sortVisibility)


    def set_effects(self):
        ranges = self.ui.encounter.selectedRanges()
        names = []
        h = ["has", "have"]
        i = ["is", "are"]
        for rows in ranges:
            for row in range(rows.topRow(), rows.bottomRow() +1):
                names.append(mobs[row].name)
                if self.ui.rechargeBox.isChecked():
                    mobs[row].recharge = 1
                    item = self.ui.encounter.item(row, 2)
                    item.setText('yes')
                    print "noo"
                else:
                    mobs[row].recharge = 0
                    item = self.ui.encounter.item(row, 2)
                    item.setText('no')
                    print "yesss"
            	mobs[row].statuses[0] = self.ui.status1Box.currentIndex()
                mobs[row].statuses[1] = self.ui.status2Box.currentIndex()
                mobs[row].statuses[2] = self.ui.status3Box.currentIndex()
                mobs[row].statuses[3] = self.ui.status4Box.currentIndex()
                y = ''
                for x in range(4):
                    item = self.ui.encounter.item(row, x+3)
                    item.setText(self.statDict[mobs[row].statuses[x]])
                    if mobs[row].statuses[x]:
                        if y == '':
                            y = self.statDict[mobs[row].statuses[x]]
                        else:
                            y = y + ", " + self.statDict[mobs[row].statuses[x]]

        s = ', '.join(names)
        a = 0
        if len(names) != 0:
            if len(names) > 1:
                a = 1
            if y == '':
                self.ui.battleLog.addItem("%s no longer has any ongoing effects" % (s, h[a]))
            else:
                self.ui.battleLog.addItem("%s %s now: %s." % (s, i[a], y))

    def add_monster(self):
        dlg = StartMonsterDialog()
        dlg.__init__()
        if dlg.exec_():
            newMonster = dlg.getValues()
            monsters.append(newMonster)
            self.ui.mobSelect.addItem(newMonster.name, None)
            
            self.ui.mobInfo.setPlainText(newMonster.desc)

    def edit_monster(self):
        pass

    def delete_mobs(self):
        ranges = self.ui.encounter.selectedRanges()
        for rows in ranges:
            for row in range(rows.topRow(), rows.bottomRow() +1):
                self.delete_mob(row)

    def delete_mob(self, row):
        self.ui.encounter.removeRow(row)
        del mobs[row]

    def rename_mob(self):
        row = self.ui.encounter.currentRow()
        self.ui.encounter.item(row, 0)

    def save_all(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', './', selectedFilter='*.txt')
        if fileName:
            write = open(fileName, "w")
            write.write("%s\n" % (len(monsters)))
            for x in monsters:
                write.write("%s\n" % (x.__dict__))
            write.write("%s\n" % (len(mobs)))
            for x in mobs:
                write.write("%s\n" % (x.__dict__))
            numlog = self.ui.battleLog.count()
            write.write("%s\n" % (numlog))
            for x in range(0, numlog):
                write.write("%s\n" % (str(self.ui.battleLog.item(x).text())))
            write.close()

    def load_all(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Load From File', './', selectedFilter='*.txt')
        if fileName:
            self.ui.encounter.clearContents()
            self.ui.encounter.setRowCount(0)
            self.ui.battleLog.clear()
            self.ui.mobSelect.clear()
            load = open(fileName, "r")
            monlen = int(load.readline())
            #print monlen
            del monsters[:]
            for x in range(0, monlen):
                monsters.append(Monster())
                monsters[-1].__dict__ = ast.literal_eval(load.readline())
                self.ui.mobSelect.addItem(monsters[-1].name, None)
            moblen = int(load.readline())
            #print moblen
            del mobs[:]
            for x in range(0, moblen):
                mobs.append(Monster())
                mobs[-1].__dict__ = ast.literal_eval(load.readline())
                self.populate_mob()
            lognum = int(load.readline())
            for x in range(0, lognum):
                self.ui.battleLog.addItem(load.readline()[:-1])
            load.close()


        

class StartMonsterDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_monsterDialog()
        self.ui.setupUi(self)

    def getValues(self):
        return Monster(str(self.ui.nameLine.text()), int(self.ui.numDice.text()), int(self.ui.dieSize.text()), int(self.ui.hitDiceMod.text()), str(self.ui.descriptionBox.toPlainText()))


if __name__ == "__main__":
    monsters = []
    mobs = []

    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()


    sys.exit(app.exec_())


    