from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(553, 371)
        MainWindow.setFixedSize(555, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupCreation = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupCreation.setFont(font)
        self.groupCreation.setObjectName("groupCreation")
        self.verticalLayout_2.addWidget(self.groupCreation)
        self.groupMemberAdd = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupMemberAdd.setFont(font)
        self.groupMemberAdd.setObjectName("groupMemberAdd")
        self.verticalLayout_2.addWidget(self.groupMemberAdd)
        self.groupCreateAddMember = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupCreateAddMember.setFont(font)
        self.groupCreateAddMember.setObjectName("groupCreateAddMember")
        self.verticalLayout_2.addWidget(self.groupCreateAddMember)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sendText = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendText.setFont(font)
        self.sendText.setObjectName("sendText")
        self.verticalLayout_3.addWidget(self.sendText)
        self.sendDoc = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendDoc.setFont(font)
        self.sendDoc.setObjectName("sendDoc")
        self.verticalLayout_3.addWidget(self.sendDoc)
        self.sendMedia = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendMedia.setFont(font)
        self.sendMedia.setObjectName("sendMedia")
        self.verticalLayout_3.addWidget(self.sendMedia)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whatsapp Auto"))
        self.label.setText(_translate("MainWindow", "Whatsapp Auto"))
        self.label_2.setText(_translate("MainWindow", "Application"))
        self.label_3.setText(_translate("MainWindow", "Whatsapp"))
        self.groupCreation.setText(_translate("MainWindow", "Group Creation"))
        self.groupMemberAdd.setText(_translate("MainWindow", "Group Member Addition"))
        self.groupCreateAddMember.setText(_translate("MainWindow", "Group Create & Add Member"))
        self.sendText.setText(_translate("MainWindow", "Send Text"))
        self.sendDoc.setText(_translate("MainWindow", "Send Document"))
        self.sendMedia.setText(_translate("MainWindow", "Send Mediafiles"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    #Style
    with open("style.css","r") as style:
        app.setStyleSheet(style.read())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
