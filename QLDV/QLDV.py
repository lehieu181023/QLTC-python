# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QLDV.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 669)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 121, 111))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/Pet Haven.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 410, 191, 181))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/self-service.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(170, 80, 611, 16))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 781, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(390, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tb_t = QtWidgets.QLineEdit(self.groupBox)
        self.tb_t.setGeometry(QtCore.QRect(540, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tb_t.setFont(font)
        self.tb_t.setObjectName("tb_t")
        self.tb_m = QtWidgets.QLineEdit(self.groupBox)
        self.tb_m.setGeometry(QtCore.QRect(170, 40, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tb_m.setFont(font)
        self.tb_m.setObjectName("tb_m")
        self.cb_l = QtWidgets.QComboBox(self.groupBox)
        self.cb_l.setGeometry(QtCore.QRect(170, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_l.setFont(font)
        self.cb_l.setObjectName("cb_l")
        self.cb_l.addItem("")
        self.cb_l.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(380, 270, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.cb_l_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.cb_l_4.setGeometry(QtCore.QRect(120, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_l_4.setFont(font)
        self.cb_l_4.setObjectName("cb_l_4")
        self.cb_l_4.addItem("")
        self.cb_l_4.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 270, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cb_l_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_l_2.setGeometry(QtCore.QRect(120, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_l_2.setFont(font)
        self.cb_l_2.setObjectName("cb_l_2")
        self.cb_l_2.addItem("")
        self.cb_l_2.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 390, 561, 231))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.bt_t = QtWidgets.QPushButton(self.centralwidget)
        self.bt_t.setGeometry(QtCore.QRect(600, 420, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_t.setFont(font)
        self.bt_t.setObjectName("bt_t")
        self.bt_t_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_t_2.setGeometry(QtCore.QRect(600, 470, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_t_2.setFont(font)
        self.bt_t_2.setObjectName("bt_t_2")
        self.bt_x = QtWidgets.QPushButton(self.centralwidget)
        self.bt_x.setGeometry(QtCore.QRect(600, 520, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_x.setFont(font)
        self.bt_x.setObjectName("bt_x")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quản Lý Dịch Vụ "))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin khách hàng"))
        self.label_3.setText(_translate("MainWindow", "Tên khách hàng"))
        self.label_4.setText(_translate("MainWindow", "Loại thú cưng:"))
        self.label_6.setText(_translate("MainWindow", "Số điện thoại"))
        self.cb_l.setItemText(0, _translate("MainWindow", "Chó"))
        self.cb_l.setItemText(1, _translate("MainWindow", "Mèo"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Tiêm phòng"))
        self.label_7.setText(_translate("MainWindow", "Loại dịch vụ :"))
        self.cb_l_4.setItemText(0, _translate("MainWindow", "Phòng dại"))
        self.cb_l_4.setItemText(1, _translate("MainWindow", "Phòng ký sinh"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dịch vụ spa"))
        self.label_2.setText(_translate("MainWindow", "Loại dịch vụ :"))
        self.cb_l_2.setItemText(0, _translate("MainWindow", "Tắm thơm"))
        self.cb_l_2.setItemText(1, _translate("MainWindow", "Cắt tỉa lông"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tên khách hàng"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Loại thú cưng"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Số điện thoại"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dịch vụ spa"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiêm phòng"))
        self.bt_t.setText(_translate("MainWindow", "Thêm"))
        self.bt_t_2.setText(_translate("MainWindow", "Sửa "))
        self.bt_x.setText(_translate("MainWindow", "Xóa"))
import qldv_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())