# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JohnnyG\Documents\CHESS\XRDproject_Python_11June2010Release\buildnewscan.ui'
#
# Created: Fri Jun 18 10:17:58 2010
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_buildnewscanDialog(object):
    def setupUi(self, buildnewscanDialog):
        buildnewscanDialog.setObjectName("buildnewscanDialog")
        buildnewscanDialog.resize(828, 323)
        self.buttonBox = QtGui.QDialogButtonBox(buildnewscanDialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 285, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.replacelistLineEdit = QtGui.QLineEdit(buildnewscanDialog)
        self.replacelistLineEdit.setGeometry(QtCore.QRect(170, 105, 521, 25))
        self.replacelistLineEdit.setObjectName("replacelistLineEdit")
        self.newlistLineEdit = QtGui.QLineEdit(buildnewscanDialog)
        self.newlistLineEdit.setGeometry(QtCore.QRect(175, 180, 536, 25))
        self.newlistLineEdit.setObjectName("newlistLineEdit")
        self.replaceimageComboBox = QtGui.QComboBox(buildnewscanDialog)
        self.replaceimageComboBox.setGeometry(QtCore.QRect(0, 105, 151, 26))
        self.replaceimageComboBox.setObjectName("replaceimageComboBox")
        self.newimageComboBox = QtGui.QComboBox(buildnewscanDialog)
        self.newimageComboBox.setGeometry(QtCore.QRect(0, 180, 151, 26))
        self.newimageComboBox.setObjectName("newimageComboBox")
        self.appendnameComboBox = QtGui.QComboBox(buildnewscanDialog)
        self.appendnameComboBox.setGeometry(QtCore.QRect(0, 255, 241, 26))
        self.appendnameComboBox.setObjectName("appendnameComboBox")
        self.appendlistLineEdit = QtGui.QLineEdit(buildnewscanDialog)
        self.appendlistLineEdit.setGeometry(QtCore.QRect(250, 255, 536, 25))
        self.appendlistLineEdit.setObjectName("appendlistLineEdit")
        self.appendPushButton = QtGui.QPushButton(buildnewscanDialog)
        self.appendPushButton.setGeometry(QtCore.QRect(90, 215, 201, 24))
        self.appendPushButton.setObjectName("appendPushButton")
        self.replacePushButton = QtGui.QPushButton(buildnewscanDialog)
        self.replacePushButton.setGeometry(QtCore.QRect(90, 140, 201, 24))
        self.replacePushButton.setObjectName("replacePushButton")
        self.label = QtGui.QLabel(buildnewscanDialog)
        self.label.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(buildnewscanDialog)
        self.label_2.setGeometry(QtCore.QRect(180, 90, 391, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(buildnewscanDialog)
        self.label_3.setGeometry(QtCore.QRect(180, 165, 541, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(buildnewscanDialog)
        self.label_4.setGeometry(QtCore.QRect(250, 240, 546, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(buildnewscanDialog)
        self.label_5.setGeometry(QtCore.QRect(0, 165, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(buildnewscanDialog)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 141, 16))
        self.label_6.setObjectName("label_6")
        self.copynameComboBox = QtGui.QComboBox(buildnewscanDialog)
        self.copynameComboBox.setGeometry(QtCore.QRect(10, 20, 501, 26))
        self.copynameComboBox.setObjectName("copynameComboBox")
        self.label_7 = QtGui.QLabel(buildnewscanDialog)
        self.label_7.setGeometry(QtCore.QRect(30, 5, 131, 16))
        self.label_7.setObjectName("label_7")
        self.radiusSpinBox = QtGui.QDoubleSpinBox(buildnewscanDialog)
        self.radiusSpinBox.setGeometry(QtCore.QRect(260, 50, 71, 25))
        self.radiusSpinBox.setMaximum(9999.0)
        self.radiusSpinBox.setObjectName("radiusSpinBox")
        self.label_8 = QtGui.QLabel(buildnewscanDialog)
        self.label_8.setGeometry(QtCore.QRect(80, 50, 181, 31))
        self.label_8.setObjectName("label_8")
        self.newnameLineEdit = QtGui.QLineEdit(buildnewscanDialog)
        self.newnameLineEdit.setGeometry(QtCore.QRect(530, 20, 121, 25))
        self.newnameLineEdit.setObjectName("newnameLineEdit")
        self.label_9 = QtGui.QLabel(buildnewscanDialog)
        self.label_9.setGeometry(QtCore.QRect(530, 5, 131, 16))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(buildnewscanDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), buildnewscanDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), buildnewscanDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(buildnewscanDialog)

    def retranslateUi(self, buildnewscanDialog):
        buildnewscanDialog.setWindowTitle(QtGui.QApplication.translate("buildnewscanDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.replacelistLineEdit.setToolTip(QtGui.QApplication.translate("buildnewscanDialog", "This is the list of spec indeces from the \"scan name to copy\" which will be will be replaced.", None, QtGui.QApplication.UnicodeUTF8))
        self.newlistLineEdit.setToolTip(QtGui.QApplication.translate("buildnewscanDialog", "These are the spec indeces from elsehwere in the .h5 file which will replace the above spec indeces. Both XRD and XRF data are replaced.", None, QtGui.QApplication.UnicodeUTF8))
        self.appendlistLineEdit.setToolTip(QtGui.QApplication.translate("buildnewscanDialog", "These are the other spec groups which will be appended to the copied spec group. In the new group, the spec indeces will be coninued from the copied spec group. The resulting list of x,z positions will not necessarily correspond to something that could be accessed with a single spec command.", None, QtGui.QApplication.UnicodeUTF8))
        self.appendPushButton.setText(QtGui.QApplication.translate("buildnewscanDialog", "Add to append scan list", None, QtGui.QApplication.UnicodeUTF8))
        self.replacePushButton.setText(QtGui.QApplication.translate("buildnewscanDialog", "Add replacement to list", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("buildnewscanDialog", "image to be replaced", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("buildnewscanDialog", "list of images to be replaced. comma-delimited list of indeces", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("buildnewscanDialog", "list of images to replace above images. comma-delimited list of scanname:index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("buildnewscanDialog", "list of comma-delimited scan names. All images from each scan will be appended", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("buildnewscanDialog", "image to replace above", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("buildnewscanDialog", "scan name to append", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("buildnewscanDialog", "scan name to copy", None, QtGui.QApplication.UnicodeUTF8))
        self.radiusSpinBox.setToolTip(QtGui.QApplication.translate("buildnewscanDialog", "When a distance is entered here, the spec group, spec index of diffraction images acquired within that distance of \"image to be replaced\" will be listed in \"image to replace above\".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("buildnewscanDialog", "search radius for finding\n"
"suitablereplacement (mm)", None, QtGui.QApplication.UnicodeUTF8))
        self.newnameLineEdit.setToolTip(QtGui.QApplication.translate("buildnewscanDialog", "This will be the name of the synthetic spec scan in the .h5 file.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("buildnewscanDialog", "new scan name", None, QtGui.QApplication.UnicodeUTF8))

