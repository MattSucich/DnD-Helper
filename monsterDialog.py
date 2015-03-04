# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monsterDialog.ui'
#
# Created: Tue Mar  3 16:30:45 2015
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

class Ui_monsterDialog(object):
    def setupUi(self, monsterDialog):
        monsterDialog.setObjectName(_fromUtf8("monsterDialog"))
        monsterDialog.resize(297, 382)
        self.verticalLayout = QtGui.QVBoxLayout(monsterDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(monsterDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit = QtGui.QLineEdit(monsterDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(monsterDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.numDice = QtGui.QLineEdit(monsterDialog)
        self.numDice.setBaseSize(QtCore.QSize(12, 0))
        self.numDice.setObjectName(_fromUtf8("numDice"))
        self.horizontalLayout.addWidget(self.numDice)
        self.label_4 = QtGui.QLabel(monsterDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.dieSize = QtGui.QLineEdit(monsterDialog)
        self.dieSize.setBaseSize(QtCore.QSize(12, 0))
        self.dieSize.setObjectName(_fromUtf8("dieSize"))
        self.horizontalLayout.addWidget(self.dieSize)
        self.label_5 = QtGui.QLabel(monsterDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.hitDiceMod = QtGui.QLineEdit(monsterDialog)
        self.hitDiceMod.setObjectName(_fromUtf8("hitDiceMod"))
        self.horizontalLayout.addWidget(self.hitDiceMod)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtGui.QLabel(monsterDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtGui.QPlainTextEdit(monsterDialog)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.buttonBox = QtGui.QDialogButtonBox(monsterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(monsterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), monsterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), monsterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(monsterDialog)

    def retranslateUi(self, monsterDialog):
        monsterDialog.setWindowTitle(_translate("monsterDialog", "New Monster", None))
        self.label_3.setText(_translate("monsterDialog", "Name:", None))
        self.label_2.setText(_translate("monsterDialog", "Hit Dice", None))
        self.label_4.setText(_translate("monsterDialog", "d", None))
        self.label_5.setText(_translate("monsterDialog", "+", None))
        self.label.setText(_translate("monsterDialog", "Description", None))

