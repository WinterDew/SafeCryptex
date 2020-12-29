# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Win(object):
    def setupUi(self, Win):
        Win.setObjectName("Win")
        Win.resize(608, 242)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/secured-connection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Win.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Win)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Encryption = QtWidgets.QWidget()
        self.Encryption.setObjectName("Encryption")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Encryption)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.Encryption)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Encryption)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.Browse_E_In = QtWidgets.QToolButton(self.Encryption)
        self.Browse_E_In.setObjectName("Browse_E_In")
        self.gridLayout_2.addWidget(self.Browse_E_In, 0, 2, 1, 1)
        self.Browse_E_Out = QtWidgets.QToolButton(self.Encryption)
        self.Browse_E_Out.setObjectName("Browse_E_Out")
        self.gridLayout_2.addWidget(self.Browse_E_Out, 2, 2, 1, 1)
        self.Pass = QtWidgets.QLineEdit(self.Encryption)
        self.Pass.setInputMask("")
        self.Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass.setObjectName("Pass")
        self.gridLayout_2.addWidget(self.Pass, 4, 1, 1, 1)
        self.Output_E_File = QtWidgets.QLineEdit(self.Encryption)
        self.Output_E_File.setObjectName("Output_E_File")
        self.gridLayout_2.addWidget(self.Output_E_File, 2, 1, 1, 1)
        self.Visible_E = QtWidgets.QRadioButton(self.Encryption)
        self.Visible_E.setObjectName("Visible_E")
        self.gridLayout_2.addWidget(self.Visible_E, 4, 2, 1, 1)
        self.Input_E_File = QtWidgets.QLineEdit(self.Encryption)
        self.Input_E_File.setObjectName("Input_E_File")
        self.gridLayout_2.addWidget(self.Input_E_File, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.Encryption)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.Encrypt = QtWidgets.QPushButton(self.Encryption)
        self.Encrypt.setObjectName("Encrypt")
        self.gridLayout_2.addWidget(self.Encrypt, 5, 1, 1, 1)
        self.tabWidget.addTab(self.Encryption, "")
        self.Decryption = QtWidgets.QWidget()
        self.Decryption.setObjectName("Decryption")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Decryption)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.Decryption)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.Input_D_File = QtWidgets.QLineEdit(self.Decryption)
        self.Input_D_File.setObjectName("Input_D_File")
        self.gridLayout_3.addWidget(self.Input_D_File, 0, 1, 1, 1)
        self.Browse_D_In = QtWidgets.QToolButton(self.Decryption)
        self.Browse_D_In.setObjectName("Browse_D_In")
        self.gridLayout_3.addWidget(self.Browse_D_In, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Decryption)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.Output_D_File = QtWidgets.QLineEdit(self.Decryption)
        self.Output_D_File.setObjectName("Output_D_File")
        self.gridLayout_3.addWidget(self.Output_D_File, 1, 1, 1, 1)
        self.Browse_D_Out = QtWidgets.QToolButton(self.Decryption)
        self.Browse_D_Out.setObjectName("Browse_D_Out")
        self.gridLayout_3.addWidget(self.Browse_D_Out, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.Decryption)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.Pass_D = QtWidgets.QLineEdit(self.Decryption)
        self.Pass_D.setInputMask("")
        self.Pass_D.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pass_D.setObjectName("Pass_D")
        self.gridLayout_3.addWidget(self.Pass_D, 2, 1, 1, 1)
        self.Visible_D = QtWidgets.QRadioButton(self.Decryption)
        self.Visible_D.setObjectName("Visible_D")
        self.gridLayout_3.addWidget(self.Visible_D, 2, 2, 1, 1)
        self.Decrypt = QtWidgets.QPushButton(self.Decryption)
        self.Decrypt.setObjectName("Decrypt")
        self.gridLayout_3.addWidget(self.Decrypt, 3, 1, 1, 1)
        self.tabWidget.addTab(self.Decryption, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        Win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Win)
        self.statusbar.setObjectName("statusbar")
        Win.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(Win)
        self.actionHelp.setObjectName("actionHelp")
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Win)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Win)

    def retranslateUi(self, Win):
        _translate = QtCore.QCoreApplication.translate
        Win.setWindowTitle(_translate("Win", "SafeCryptex"))
        self.label_7.setText(_translate("Win", "By Mr. Tatva Agarwal "))
        self.label_3.setText(_translate("Win", "PassPhrase"))
        self.label_2.setText(_translate("Win", "Output Encrypted File"))
        self.Browse_E_In.setText(_translate("Win", "Browse"))
        self.Browse_E_Out.setText(_translate("Win", "Browse"))
        self.Pass.setPlaceholderText(_translate("Win", "PassWord"))
        self.Output_E_File.setPlaceholderText(_translate("Win", "C:/Users/$USERNAME/Desktop/Data.aes"))
        self.Visible_E.setText(_translate("Win", "Visible"))
        self.Input_E_File.setPlaceholderText(_translate("Win", "C:/Users/$USERNAME/Desktop/Data.txt"))
        self.label.setText(_translate("Win", "Input File to be Encrypted"))
        self.Encrypt.setText(_translate("Win", "Encrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Encryption), _translate("Win", "Encryption"))
        self.label_6.setText(_translate("Win", "Input Encrypted File"))
        self.Input_D_File.setPlaceholderText(_translate("Win", "C:/Users/$USERNAME/Desktop/Data.aes"))
        self.Browse_D_In.setText(_translate("Win", "Browse"))
        self.label_4.setText(_translate("Win", "Output Decrypted File"))
        self.Output_D_File.setPlaceholderText(_translate("Win", "C:/Users/$USERNAME/Desktop/Data.txt"))
        self.Browse_D_Out.setText(_translate("Win", "Browse"))
        self.label_5.setText(_translate("Win", "PassPhrase"))
        self.Pass_D.setPlaceholderText(_translate("Win", "PassWord"))
        self.Visible_D.setText(_translate("Win", "Visible"))
        self.Decrypt.setText(_translate("Win", "Decrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Decryption), _translate("Win", "Decryption"))
        self.label_8.setText(_translate("Win", "For Help and Usage : https://github.com/CoderTatva-2006/SafeCryptex"))
        self.menuHelp.setTitle(_translate("Win", "Help"))
        self.actionHelp.setText(_translate("Win", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Win = QtWidgets.QMainWindow()
    ui = Ui_Win()
    ui.setupUi(Win)
    Win.show()
    sys.exit(app.exec_())
