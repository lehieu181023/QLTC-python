# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QLGTC.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SaveClass')))
from classgtc import giongtc

class Ui_QL_GTC(object):
    def setupUi(self, QL_GTC):
        QL_GTC.setObjectName("QL_GTC")
        QL_GTC.resize(1074, 653)
        self.centralwidget = QtWidgets.QWidget(QL_GTC)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 20, 921, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 100, 1041, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(70, 20, 321, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.cb_l = QtWidgets.QComboBox(self.widget)
        self.cb_l.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.cb_l.setObjectName("cb_l")
        self.cb_l.addItem("")
        self.cb_l.addItem("")
        self.gridLayout.addWidget(self.cb_l, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lb_g = QtWidgets.QLineEdit(self.widget)
        self.lb_g.setObjectName("lb_g")
        self.gridLayout.addWidget(self.lb_g, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lb_gia = QtWidgets.QLineEdit(self.widget)
        self.lb_gia.setObjectName("lb_gia")
        self.gridLayout.addWidget(self.lb_gia, 2, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(560, 20, 315, 111))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lb_gt = QtWidgets.QPlainTextEdit(self.widget1)
        self.lb_gt.setObjectName("lb_gt")
        self.gridLayout_2.addWidget(self.lb_gt, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 270, 1041, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setGeometry(QtCore.QRect(700, 0, 341, 71))
        self.groupBox.setObjectName("groupBox")
        self.lb_tk = QtWidgets.QLineEdit(self.groupBox)
        self.lb_tk.setGeometry(QtCore.QRect(80, 30, 151, 20))
        self.lb_tk.setObjectName("lb_tk")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget2 = QtWidgets.QWidget(self.frame_3)
        self.widget2.setGeometry(QtCore.QRect(40, 10, 651, 51))
        self.widget2.setObjectName("widget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btn_t = QtWidgets.QPushButton(self.widget2)
        self.btn_t.setObjectName("btn_t")
        self.gridLayout_3.addWidget(self.btn_t, 0, 0, 1, 1)
        self.by_s = QtWidgets.QPushButton(self.widget2)
        self.by_s.setObjectName("by_s")
        self.gridLayout_3.addWidget(self.by_s, 0, 1, 1, 1)
        self.bt_x = QtWidgets.QPushButton(self.widget2)
        self.bt_x.setObjectName("bt_x")
        self.gridLayout_3.addWidget(self.bt_x, 0, 2, 1, 1)
        self.btn_h = QtWidgets.QPushButton(self.widget2)
        self.btn_h.setObjectName("btn_h")
        self.gridLayout_3.addWidget(self.btn_h, 0, 3, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(20, 360, 1041, 281))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(110, 20, 741, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
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
        header = self.tableWidget.horizontalHeader()
        for i in range(self.tableWidget.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(19, 9, 121, 91))
        self.groupBox_2.setStyleSheet("border-image: url(:/bgr/Pet Haven.png);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        QL_GTC.setCentralWidget(self.centralwidget)

        self.retranslateUi(QL_GTC)
        QtCore.QMetaObject.connectSlotsByName(QL_GTC)
        
        self.pushButton_4.clicked.connect(self.tk)
        self.btn_t.clicked.connect(self.them)
        self.by_s.clicked.connect(self.sua)
        self.bt_x.clicked.connect(self.xoa)
        self.btn_h.clicked.connect(self.huy)
        self.tableWidget.cellClicked.connect(self.cellclick)
        self.hienthi()

    def retranslateUi(self, QL_GTC):
        _translate = QtCore.QCoreApplication.translate
        QL_GTC.setWindowTitle(_translate("QL_GTC", "MainWindow"))
        self.label.setText(_translate("QL_GTC", "Quản lý giống thú cưng"))
        self.label_2.setText(_translate("QL_GTC", "Loại :"))
        self.cb_l.setItemText(0, _translate("QL_GTC", "Chó"))
        self.cb_l.setItemText(1, _translate("QL_GTC", "Mèo"))
        self.label_3.setText(_translate("QL_GTC", "Giống :"))
        self.label_5.setText(_translate("QL_GTC", "Giá :"))
        self.label_4.setText(_translate("QL_GTC", "Giới thiệu :"))
        self.groupBox.setTitle(_translate("QL_GTC", "Tìm kiếm"))
        self.label_6.setText(_translate("QL_GTC", "Tìm kiếm :"))
        self.pushButton_4.setText(_translate("QL_GTC", "Tìm kiếm"))
        self.btn_t.setText(_translate("QL_GTC", "Thêm"))
        self.by_s.setText(_translate("QL_GTC", "Sửa"))
        self.bt_x.setText(_translate("QL_GTC", "Xóa"))
        self.btn_h.setText(_translate("QL_GTC", "Hủy"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("QL_GTC", "Mã giống"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("QL_GTC", "Loại"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("QL_GTC", "Giống"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("QL_GTC", "Giá"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("QL_GTC", "Giới thiệu"))
    def tk(self):
        tk = self.lb_tk.text()
        gtc = giongtc
        try:
            tk = int(tk)
        except:
            pass
        if isinstance(tk, int):         
            self.nhaptable(gtc.timkiemma(tk))
        elif tk == "":
            self.nhaptable(gtc.hienthi())    
        else:
            self.nhaptable(gtc.timkiemgiong(tk))
    
    def them(self):
        loai = self.cb_l.currentText()
        giong = self.lb_g.text()
        gia = self.lb_gia.text()
        gt = self.lb_gt.toPlainText()
        gtc = giongtc("",loai,giong,gia,gt)
        gtc.them()
        self.hienthi()
    
    
    def sua(self):
        mag = self.mag
        loai = self.cb_l.currentText()
        giong = self.lb_g.text()
        gia = self.lb_gia.text()
        gt = self.lb_gt.toPlainText()
        gtc = giongtc(mag,loai,giong,gia,gt)
        gtc.sua()
        self.hienthi()
        
    def xoa(self):
        mag = self.mag
        gtc = giongtc
        gtc.xoa(mag)
        self.hienthi()
        
    def huy(self):
        self.lb_gt.setPlainText("")
        self.lb_g.setText("")
        self.lb_gia.setText("")
        self.cb_l.setCurrentIndex(0)
        self.lb_tk.setText("")
        self.hienthi()
        
    def hienthi(self):      
        gtc = giongtc
        data = gtc.hienthi()
        self.nhaptable(data)
    
    def nhaptable(self,data):
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_position, column_index, QTableWidgetItem(str(cell_data)))
        
    def cellclick(self):
        row = self.tableWidget.currentRow()
        self.mag = self.tableWidget.item(row,0).text()
        self.cb_l.setCurrentText(self.tableWidget.item(row,1).text())
        self.lb_gt.setPlainText(self.tableWidget.item(row,4).text())
        self.lb_g.setText(self.tableWidget.item(row,2).text())
        self.lb_gia.setText(self.tableWidget.item(row,3).text())
import bg


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QL_GTC = QtWidgets.QMainWindow()
    ui = Ui_QL_GTC()
    ui.setupUi(QL_GTC)
    QL_GTC.show()
    sys.exit(app.exec_())