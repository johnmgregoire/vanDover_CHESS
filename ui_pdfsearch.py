# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JohnnyG\Documents\CHESS\XRDproject_Python_11June2010Release\pdfsearch.ui'
#
# Created: Fri Jun 18 10:18:01 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_pdfsearchDialog(object):
    def setupUi(self, pdfsearchDialog):
        pdfsearchDialog.setObjectName("pdfsearchDialog")
        pdfsearchDialog.resize(591, 690)
        self.buttonBox = QtGui.QDialogButtonBox(pdfsearchDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 660, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pdfListWidget = QtGui.QListWidget(pdfsearchDialog)
        self.pdfListWidget.setGeometry(QtCore.QRect(0, 80, 471, 331))
        self.pdfListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.pdfListWidget.setObjectName("pdfListWidget")
        self.plotListWidget = QtGui.QListWidget(pdfsearchDialog)
        self.plotListWidget.setGeometry(QtCore.QRect(0, 470, 341, 181))
        self.plotListWidget.setObjectName("plotListWidget")
        self.colListWidget = QtGui.QListWidget(pdfsearchDialog)
        self.colListWidget.setGeometry(QtCore.QRect(340, 470, 41, 181))
        self.colListWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.colListWidget.setObjectName("colListWidget")
        self.searchLineEdit0 = QtGui.QLineEdit(pdfsearchDialog)
        self.searchLineEdit0.setGeometry(QtCore.QRect(10, 20, 91, 25))
        self.searchLineEdit0.setObjectName("searchLineEdit0")
        self.searchLineEdit1 = QtGui.QLineEdit(pdfsearchDialog)
        self.searchLineEdit1.setGeometry(QtCore.QRect(100, 20, 91, 25))
        self.searchLineEdit1.setObjectName("searchLineEdit1")
        self.searchLineEdit2 = QtGui.QLineEdit(pdfsearchDialog)
        self.searchLineEdit2.setGeometry(QtCore.QRect(190, 20, 91, 25))
        self.searchLineEdit2.setObjectName("searchLineEdit2")
        self.searchLineEdit3 = QtGui.QLineEdit(pdfsearchDialog)
        self.searchLineEdit3.setGeometry(QtCore.QRect(280, 20, 91, 25))
        self.searchLineEdit3.setObjectName("searchLineEdit3")
        self.label = QtGui.QLabel(pdfsearchDialog)
        self.label.setGeometry(QtCore.QRect(330, 450, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(pdfsearchDialog)
        self.label_2.setGeometry(QtCore.QRect(150, 5, 161, 16))
        self.label_2.setObjectName("label_2")
        self.findPushButton = QtGui.QPushButton(pdfsearchDialog)
        self.findPushButton.setGeometry(QtCore.QRect(10, 50, 131, 24))
        self.findPushButton.setObjectName("findPushButton")
        self.heightListWidget = QtGui.QListWidget(pdfsearchDialog)
        self.heightListWidget.setGeometry(QtCore.QRect(380, 470, 91, 181))
        self.heightListWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.heightListWidget.setObjectName("heightListWidget")
        self.label_3 = QtGui.QLabel(pdfsearchDialog)
        self.label_3.setGeometry(QtCore.QRect(400, 450, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(pdfsearchDialog)
        self.label_4.setGeometry(QtCore.QRect(10, 455, 51, 16))
        self.label_4.setObjectName("label_4")
        self.addPushButton = QtGui.QPushButton(pdfsearchDialog)
        self.addPushButton.setGeometry(QtCore.QRect(195, 420, 136, 24))
        self.addPushButton.setObjectName("addPushButton")
        self.removePushButton = QtGui.QPushButton(pdfsearchDialog)
        self.removePushButton.setGeometry(QtCore.QRect(10, 420, 171, 24))
        self.removePushButton.setObjectName("removePushButton")
        self.colLineEdit = QtGui.QLineEdit(pdfsearchDialog)
        self.colLineEdit.setGeometry(QtCore.QRect(340, 420, 41, 25))
        self.colLineEdit.setObjectName("colLineEdit")
        self.heightSpinBox = QtGui.QDoubleSpinBox(pdfsearchDialog)
        self.heightSpinBox.setGeometry(QtCore.QRect(380, 420, 91, 25))
        self.heightSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.heightSpinBox.setMaximum(99999999.0)
        self.heightSpinBox.setObjectName("heightSpinBox")
        self.plotsingleCheckBox = QtGui.QCheckBox(pdfsearchDialog)
        self.plotsingleCheckBox.setGeometry(QtCore.QRect(475, 75, 91, 51))
        self.plotsingleCheckBox.setChecked(True)
        self.plotsingleCheckBox.setObjectName("plotsingleCheckBox")
        self.labelListWidget = QtGui.QListWidget(pdfsearchDialog)
        self.labelListWidget.setGeometry(QtCore.QRect(470, 470, 121, 181))
        self.labelListWidget.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.labelListWidget.setObjectName("labelListWidget")
        self.label_5 = QtGui.QLabel(pdfsearchDialog)
        self.label_5.setGeometry(QtCore.QRect(510, 450, 51, 16))
        self.label_5.setObjectName("label_5")
        self.labelLineEdit = QtGui.QLineEdit(pdfsearchDialog)
        self.labelLineEdit.setGeometry(QtCore.QRect(470, 420, 121, 25))
        self.labelLineEdit.setObjectName("labelLineEdit")

        self.retranslateUi(pdfsearchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), pdfsearchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), pdfsearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(pdfsearchDialog)

    def retranslateUi(self, pdfsearchDialog):
        pdfsearchDialog.setWindowTitle(QtGui.QApplication.translate("pdfsearchDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pdfListWidget.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is the list of PDF entries in the .txt database</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.searchLineEdit0.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "\"Find PDF entries\" will filter the names of the PDF entries, listing only those that contain the strings in these boxes.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("pdfsearchDialog", "color str", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("pdfsearchDialog", "search strings", None, QtGui.QApplication.UnicodeUTF8))
        self.findPushButton.setText(QtGui.QApplication.translate("pdfsearchDialog", "Find PDF entries", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("pdfsearchDialog", "height", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("pdfsearchDialog", "plotted", None, QtGui.QApplication.UnicodeUTF8))
        self.addPushButton.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "Take the selected PDF entry in the list above and add it to the ploit list below. ENTER THE COLOR AND HEIGHT AND LABEL BEFORE ADDING TO PLOT LIST.", None, QtGui.QApplication.UnicodeUTF8))
        self.addPushButton.setText(QtGui.QApplication.translate("pdfsearchDialog", "add to plot list   v", None, QtGui.QApplication.UnicodeUTF8))
        self.removePushButton.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "take the PDf entry selected and put it back in the above list", None, QtGui.QApplication.UnicodeUTF8))
        self.removePushButton.setText(QtGui.QApplication.translate("pdfsearchDialog", "remove from plot list  ^", None, QtGui.QApplication.UnicodeUTF8))
        self.colLineEdit.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "See matplotlib documentation for list of color codes. Do not use quotation marks.", None, QtGui.QApplication.UnicodeUTF8))
        self.colLineEdit.setText(QtGui.QApplication.translate("pdfsearchDialog", "k", None, QtGui.QApplication.UnicodeUTF8))
        self.heightSpinBox.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "Height of tallest PDF peak in diffraction intensity units.", None, QtGui.QApplication.UnicodeUTF8))
        self.plotsingleCheckBox.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "When you click on a PDF entry in the list to the left, this check box controls whether the entry will be plotted with the color and height indicated below.", None, QtGui.QApplication.UnicodeUTF8))
        self.plotsingleCheckBox.setText(QtGui.QApplication.translate("pdfsearchDialog", "Plot\n"
"When\n"
"Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("pdfsearchDialog", "label", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLineEdit.setToolTip(QtGui.QApplication.translate("pdfsearchDialog", "Label that will appear on the figure in the PDF color", None, QtGui.QApplication.UnicodeUTF8))
