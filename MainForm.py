# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DnDForm.ui'
#
# Created: Tue Mar 24 03:27:43 2015
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 793)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.createMonsterButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createMonsterButton.sizePolicy().hasHeightForWidth())
        self.createMonsterButton.setSizePolicy(sizePolicy)
        self.createMonsterButton.setObjectName(_fromUtf8("createMonsterButton"))
        self.horizontalLayout_4.addWidget(self.createMonsterButton)
        self.editMonsterButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editMonsterButton.sizePolicy().hasHeightForWidth())
        self.editMonsterButton.setSizePolicy(sizePolicy)
        self.editMonsterButton.setObjectName(_fromUtf8("editMonsterButton"))
        self.horizontalLayout_4.addWidget(self.editMonsterButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(-1)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mobSelect = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mobSelect.sizePolicy().hasHeightForWidth())
        self.mobSelect.setSizePolicy(sizePolicy)
        self.mobSelect.setMaximumSize(QtCore.QSize(200, 16777215))
        self.mobSelect.setObjectName(_fromUtf8("mobSelect"))
        self.horizontalLayout.addWidget(self.mobSelect)
        self.addMobButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addMobButton.sizePolicy().hasHeightForWidth())
        self.addMobButton.setSizePolicy(sizePolicy)
        self.addMobButton.setObjectName(_fromUtf8("addMobButton"))
        self.horizontalLayout.addWidget(self.addMobButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.encounter = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encounter.sizePolicy().hasHeightForWidth())
        self.encounter.setSizePolicy(sizePolicy)
        self.encounter.setMinimumSize(QtCore.QSize(400, 150))
        self.encounter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.encounter.setDragEnabled(False)
        self.encounter.setDragDropOverwriteMode(False)
        self.encounter.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.encounter.setAlternatingRowColors(True)
        self.encounter.setShowGrid(False)
        self.encounter.setCornerButtonEnabled(False)
        self.encounter.setObjectName(_fromUtf8("encounter"))
        self.encounter.setColumnCount(8)
        self.encounter.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.encounter.setHorizontalHeaderItem(7, item)
        self.encounter.horizontalHeader().setCascadingSectionResizes(False)
        self.encounter.horizontalHeader().setDefaultSectionSize(60)
        self.encounter.horizontalHeader().setSortIndicatorShown(False)
        self.encounter.horizontalHeader().setStretchLastSection(True)
        self.encounter.verticalHeader().setVisible(False)
        self.encounter.verticalHeader().setDefaultSectionSize(27)
        self.encounter.verticalHeader().setMinimumSectionSize(10)
        self.verticalLayout.addWidget(self.encounter)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.deleteButton = QtGui.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_6.addWidget(self.deleteButton)
        self.reorderButton = QtGui.QPushButton(self.centralwidget)
        self.reorderButton.setObjectName(_fromUtf8("reorderButton"))
        self.horizontalLayout_6.addWidget(self.reorderButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.hitValue = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hitValue.sizePolicy().hasHeightForWidth())
        self.hitValue.setSizePolicy(sizePolicy)
        self.hitValue.setMaximum(999999999)
        self.hitValue.setObjectName(_fromUtf8("hitValue"))
        self.gridLayout_2.addWidget(self.hitValue, 0, 0, 1, 2)
        self.damageButton = QtGui.QPushButton(self.groupBox)
        self.damageButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.damageButton.sizePolicy().hasHeightForWidth())
        self.damageButton.setSizePolicy(sizePolicy)
        self.damageButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.damageButton.setCheckable(False)
        self.damageButton.setFlat(False)
        self.damageButton.setObjectName(_fromUtf8("damageButton"))
        self.gridLayout_2.addWidget(self.damageButton, 3, 0, 1, 1)
        self.hitDescription = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hitDescription.sizePolicy().hasHeightForWidth())
        self.hitDescription.setSizePolicy(sizePolicy)
        self.hitDescription.setObjectName(_fromUtf8("hitDescription"))
        self.gridLayout_2.addWidget(self.hitDescription, 1, 0, 1, 2)
        self.healButton = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.healButton.sizePolicy().hasHeightForWidth())
        self.healButton.setSizePolicy(sizePolicy)
        self.healButton.setObjectName(_fromUtf8("healButton"))
        self.gridLayout_2.addWidget(self.healButton, 3, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.status1Box = QtGui.QComboBox(self.groupBox_2)
        self.status1Box.setObjectName(_fromUtf8("status1Box"))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.setItemText(0, _fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.status1Box.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.status1Box)
        self.status2Box = QtGui.QComboBox(self.groupBox_2)
        self.status2Box.setObjectName(_fromUtf8("status2Box"))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.setItemText(0, _fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.status2Box.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.status2Box)
        self.status3Box = QtGui.QComboBox(self.groupBox_2)
        self.status3Box.setObjectName(_fromUtf8("status3Box"))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.setItemText(0, _fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.status3Box.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.status3Box)
        self.status4Box = QtGui.QComboBox(self.groupBox_2)
        self.status4Box.setObjectName(_fromUtf8("status4Box"))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.setItemText(0, _fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.status4Box.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.status4Box)
        self.rechargeBox = QtGui.QCheckBox(self.groupBox_2)
        self.rechargeBox.setObjectName(_fromUtf8("rechargeBox"))
        self.verticalLayout_2.addWidget(self.rechargeBox)
        self.effectButton = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.effectButton.sizePolicy().hasHeightForWidth())
        self.effectButton.setSizePolicy(sizePolicy)
        self.effectButton.setObjectName(_fromUtf8("effectButton"))
        self.verticalLayout_2.addWidget(self.effectButton)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mobInfo = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mobInfo.sizePolicy().hasHeightForWidth())
        self.mobInfo.setSizePolicy(sizePolicy)
        self.mobInfo.setMinimumSize(QtCore.QSize(0, 150))
        self.mobInfo.setMaximumSize(QtCore.QSize(16777215, 250))
        self.mobInfo.setObjectName(_fromUtf8("mobInfo"))
        self.verticalLayout.addWidget(self.mobInfo)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.battleLog = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battleLog.sizePolicy().hasHeightForWidth())
        self.battleLog.setSizePolicy(sizePolicy)
        self.battleLog.setBaseSize(QtCore.QSize(150, 0))
        self.battleLog.setProperty("isWrapping", False)
        self.battleLog.setResizeMode(QtGui.QListView.Adjust)
        self.battleLog.setWordWrap(True)
        self.battleLog.setObjectName(_fromUtf8("battleLog"))
        self.horizontalLayout_3.addWidget(self.battleLog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 788, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.createMonsterButton.setText(_translate("MainWindow", "Create Monster", None))
        self.editMonsterButton.setText(_translate("MainWindow", "Edit Monster", None))
        self.addMobButton.setText(_translate("MainWindow", "Add mob", None))
        self.encounter.setSortingEnabled(False)
        item = self.encounter.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.encounter.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Health", None))
        item = self.encounter.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rech.", None))
        item = self.encounter.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stat", None))
        item = self.encounter.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stat", None))
        item = self.encounter.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Stat", None))
        item = self.encounter.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Stat", None))
        self.deleteButton.setText(_translate("MainWindow", "Delete Mob", None))
        self.reorderButton.setText(_translate("MainWindow", "Toggle Sorting", None))
        self.groupBox.setTitle(_translate("MainWindow", "Damage and Healing", None))
        self.damageButton.setText(_translate("MainWindow", "Damage", None))
        self.hitDescription.setPlaceholderText(_translate("MainWindow", "Description", None))
        self.healButton.setText(_translate("MainWindow", "Heal", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status Effects", None))
        self.status1Box.setItemText(1, _translate("MainWindow", "Blinded", None))
        self.status1Box.setItemText(2, _translate("MainWindow", "Charmed", None))
        self.status1Box.setItemText(3, _translate("MainWindow", "Frightened", None))
        self.status1Box.setItemText(4, _translate("MainWindow", "Grappled", None))
        self.status1Box.setItemText(5, _translate("MainWindow", "Incapacitated", None))
        self.status1Box.setItemText(6, _translate("MainWindow", "Incorporeal", None))
        self.status1Box.setItemText(7, _translate("MainWindow", "Paralyzed", None))
        self.status1Box.setItemText(8, _translate("MainWindow", "Petrified", None))
        self.status1Box.setItemText(9, _translate("MainWindow", "Prone", None))
        self.status1Box.setItemText(10, _translate("MainWindow", "Restrained", None))
        self.status1Box.setItemText(11, _translate("MainWindow", "Stunned", None))
        self.status2Box.setItemText(1, _translate("MainWindow", "Blinded", None))
        self.status2Box.setItemText(2, _translate("MainWindow", "Charmed", None))
        self.status2Box.setItemText(3, _translate("MainWindow", "Frightened", None))
        self.status2Box.setItemText(4, _translate("MainWindow", "Grappled", None))
        self.status2Box.setItemText(5, _translate("MainWindow", "Incapacitated", None))
        self.status2Box.setItemText(6, _translate("MainWindow", "Incorporeal", None))
        self.status2Box.setItemText(7, _translate("MainWindow", "Paralyzed", None))
        self.status2Box.setItemText(8, _translate("MainWindow", "Petrified", None))
        self.status2Box.setItemText(9, _translate("MainWindow", "Prone", None))
        self.status2Box.setItemText(10, _translate("MainWindow", "Restrained", None))
        self.status2Box.setItemText(11, _translate("MainWindow", "Stunned", None))
        self.status3Box.setItemText(1, _translate("MainWindow", "Blinded", None))
        self.status3Box.setItemText(2, _translate("MainWindow", "Charmed", None))
        self.status3Box.setItemText(3, _translate("MainWindow", "Frightened", None))
        self.status3Box.setItemText(4, _translate("MainWindow", "Grappled", None))
        self.status3Box.setItemText(5, _translate("MainWindow", "Incapacitated", None))
        self.status3Box.setItemText(6, _translate("MainWindow", "Incorporeal", None))
        self.status3Box.setItemText(7, _translate("MainWindow", "Paralyzed", None))
        self.status3Box.setItemText(8, _translate("MainWindow", "Petrified", None))
        self.status3Box.setItemText(9, _translate("MainWindow", "Prone", None))
        self.status3Box.setItemText(10, _translate("MainWindow", "Restrained", None))
        self.status3Box.setItemText(11, _translate("MainWindow", "Stunned", None))
        self.status4Box.setItemText(1, _translate("MainWindow", "Blinded", None))
        self.status4Box.setItemText(2, _translate("MainWindow", "Charmed", None))
        self.status4Box.setItemText(3, _translate("MainWindow", "Frightened", None))
        self.status4Box.setItemText(4, _translate("MainWindow", "Grappled", None))
        self.status4Box.setItemText(5, _translate("MainWindow", "Incapacitated", None))
        self.status4Box.setItemText(6, _translate("MainWindow", "Incorporeal", None))
        self.status4Box.setItemText(7, _translate("MainWindow", "Paralyzed", None))
        self.status4Box.setItemText(8, _translate("MainWindow", "Petrified", None))
        self.status4Box.setItemText(9, _translate("MainWindow", "Prone", None))
        self.status4Box.setItemText(10, _translate("MainWindow", "Restrained", None))
        self.status4Box.setItemText(11, _translate("MainWindow", "Stunned", None))
        self.rechargeBox.setText(_translate("MainWindow", "Recharge", None))
        self.effectButton.setText(_translate("MainWindow", "Set Conditions", None))
        self.mobInfo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.Helvetica Neue DeskInterface\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dragon</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AC: 26</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">STR</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CON<br />DEX</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">INT</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CHA</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WIS</p></body></html>", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionSave.setText(_translate("MainWindow", "Save...", None))
        self.actionLoad.setText(_translate("MainWindow", "Load...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

