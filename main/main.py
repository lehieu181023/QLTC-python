# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'QLTC')))

from QLTC import Ui_MainWindowtc


class Ui_MainWindow(object):
    
    def window(self,ui_main_window):
        window = QtWidgets.QMainWindow()
        ui = ui_main_window()
        ui.setupUi(window)
        return window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 921, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.stackedWidget.addWidget(self.window(Ui_MainWindowtc))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 21))
        self.menubar.setObjectName("menubar")
        self.menuCh_c_n_ng = QtWidgets.QMenu(self.menubar)
        self.menuCh_c_n_ng.setObjectName("menuCh_c_n_ng")
        self.menuTh_ng_k = QtWidgets.QMenu(self.menubar)
        self.menuTh_ng_k.setObjectName("menuTh_ng_k")
        self.menuTho_t = QtWidgets.QMenu(self.menubar)
        self.menuTho_t.setObjectName("menuTho_t")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQL_thu_cung = QtWidgets.QAction(MainWindow)
        self.actionQL_thu_cung.setObjectName("actionQL_thu_cung")
        self.actionQL_nhan_vien = QtWidgets.QAction(MainWindow)
        self.actionQL_nhan_vien.setObjectName("actionQL_nhan_vien")
        self.menuCh_c_n_ng.addAction(self.actionQL_thu_cung)
        self.menuCh_c_n_ng.addAction(self.actionQL_nhan_vien)
        self.menubar.addAction(self.menuCh_c_n_ng.menuAction())
        self.menubar.addAction(self.menuTh_ng_k.menuAction())
        self.menubar.addAction(self.menuTho_t.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuCh_c_n_ng.setTitle(_translate("MainWindow", "Chức năng"))
        self.menuTh_ng_k.setTitle(_translate("MainWindow", "Thống kê"))
        self.menuTho_t.setTitle(_translate("MainWindow", "Thoát"))
        self.actionQL_thu_cung.setText(_translate("MainWindow", "QL thu cung"))
        self.actionQL_nhan_vien.setText(_translate("MainWindow", "QL nhan vien"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())