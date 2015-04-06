# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editDialog.ui'
#
# Created: Mon Apr  6 04:47:28 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_monsterEdit(object):
    def setupUi(self, monsterEdit):
        monsterEdit.setObjectName(_fromUtf8("monsterEdit"))
        monsterEdit.resize(297, 382)
        self.verticalLayout = QtGui.QVBoxLayout(monsterEdit)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.monsterSelect = QtGui.QComboBox(monsterEdit)
        self.monsterSelect.setObjectName(_fromUtf8("monsterSelect"))
        self.verticalLayout.addWidget(self.monsterSelect)
        self.label_3 = QtGui.QLabel(monsterEdit)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.nameLine = QtGui.QLineEdit(monsterEdit)
        self.nameLine.setObjectName(_fromUtf8("nameLine"))
        self.verticalLayout.addWidget(self.nameLine)
        self.label_2 = QtGui.QLabel(monsterEdit)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.numDice = QtGui.QLineEdit(monsterEdit)
        self.numDice.setBaseSize(QtCore.QSize(12, 0))
        self.numDice.setObjectName(_fromUtf8("numDice"))
        self.horizontalLayout.addWidget(self.numDice)
        self.label_4 = QtGui.QLabel(monsterEdit)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.dieSize = QtGui.QLineEdit(monsterEdit)
        self.dieSize.setBaseSize(QtCore.QSize(12, 0))
        self.dieSize.setObjectName(_fromUtf8("dieSize"))
        self.horizontalLayout.addWidget(self.dieSize)
        self.label_5 = QtGui.QLabel(monsterEdit)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.hitDiceMod = QtGui.QLineEdit(monsterEdit)
        self.hitDiceMod.setObjectName(_fromUtf8("hitDiceMod"))
        self.horizontalLayout.addWidget(self.hitDiceMod)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(monsterEdit)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.descriptionBox = QtGui.QPlainTextEdit(monsterEdit)
        self.descriptionBox.setObjectName(_fromUtf8("descriptionBox"))
        self.verticalLayout.addWidget(self.descriptionBox)
        self.buttonBox = QtGui.QDialogButtonBox(monsterEdit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(monsterEdit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), monsterEdit.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), monsterEdit.reject)
        QtCore.QMetaObject.connectSlotsByName(monsterEdit)

    def retranslateUi(self, monsterEdit):
        monsterEdit.setWindowTitle(_translate("monsterEdit", "Edit Monster", None))
        self.label_3.setText(_translate("monsterEdit", "Name:", None))
        self.label_2.setText(_translate("monsterEdit", "Hit Dice", None))
        self.label_4.setText(_translate("monsterEdit", "d", None))
        self.label_5.setText(_translate("monsterEdit", "+", None))
        self.label.setText(_translate("monsterEdit", "Description", None))

