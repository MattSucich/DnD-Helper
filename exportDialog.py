# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportDialog.ui'
#
# Created: Sat Apr 18 17:44:41 2015
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

class Ui_exportDialog(object):
    def setupUi(self, exportDialog):
        exportDialog.setObjectName(_fromUtf8("exportDialog"))
        exportDialog.resize(240, 320)
        self.verticalLayout = QtGui.QVBoxLayout(exportDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listView = QtGui.QListView(exportDialog)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.buttonBox = QtGui.QDialogButtonBox(exportDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(exportDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), exportDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), exportDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(exportDialog)

    def retranslateUi(self, exportDialog):
        exportDialog.setWindowTitle(_translate("exportDialog", "Export Monsters", None))

