# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UISpectrometer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1159, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_10.setSpacing(5)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lb_bnumber = QtWidgets.QLabel(self.groupBox_4)
        self.lb_bnumber.setObjectName("lb_bnumber")
        self.gridLayout_8.addWidget(self.lb_bnumber, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)
        self.sb_bnumber = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.sb_bnumber.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_bnumber.setDecimals(0)
        self.sb_bnumber.setMaximum(1000.0)
        self.sb_bnumber.setProperty("value", 1.0)
        self.sb_bnumber.setObjectName("sb_bnumber")
        self.gridLayout_8.addWidget(self.sb_bnumber, 0, 1, 1, 1)
        self.sb_b = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.sb_b.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_b.setDecimals(0)
        self.sb_b.setMaximum(1000.0)
        self.sb_b.setSingleStep(10.0)
        self.sb_b.setProperty("value", 10.0)
        self.sb_b.setObjectName("sb_b")
        self.gridLayout_8.addWidget(self.sb_b, 1, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sb_E0 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sb_E0.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_E0.setMaximum(24000.0)
        self.sb_E0.setProperty("value", 9000.0)
        self.sb_E0.setObjectName("sb_E0")
        self.gridLayout_3.addWidget(self.sb_E0, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.sb_px1 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sb_px1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_px1.setDecimals(0)
        self.sb_px1.setMaximum(1280.0)
        self.sb_px1.setProperty("value", 600.0)
        self.sb_px1.setObjectName("sb_px1")
        self.gridLayout_3.addWidget(self.sb_px1, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.sb_ev_px = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sb_ev_px.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_ev_px.setSingleStep(0.1)
        self.sb_ev_px.setProperty("value", 0.5)
        self.sb_ev_px.setObjectName("sb_ev_px")
        self.gridLayout_3.addWidget(self.sb_ev_px, 0, 1, 1, 1)
        self.pb_estim_px1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pb_estim_px1.setObjectName("pb_estim_px1")
        self.gridLayout_3.addWidget(self.pb_estim_px1, 1, 3, 1, 1)
        self.chb_show_fit = QtWidgets.QCheckBox(self.groupBox_2)
        self.chb_show_fit.setObjectName("chb_show_fit")
        self.gridLayout_3.addWidget(self.chb_show_fit, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le_b = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_b.sizePolicy().hasHeightForWidth())
        self.le_b.setSizePolicy(sizePolicy)
        self.le_b.setObjectName("le_b")
        self.gridLayout.addWidget(self.le_b, 1, 0, 1, 2)
        self.le_a = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_a.sizePolicy().hasHeightForWidth())
        self.le_a.setSizePolicy(sizePolicy)
        self.le_a.setObjectName("le_a")
        self.gridLayout.addWidget(self.le_a, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(100, 100))
        self.widget.setObjectName("widget")
        self.gridLayout_10.addWidget(self.widget, 0, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pb_background = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_background.setObjectName("pb_background")
        self.gridLayout_5.addWidget(self.pb_background, 1, 2, 1, 1)
        self.sb_nbunch_back = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.sb_nbunch_back.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.sb_nbunch_back.setDecimals(0)
        self.sb_nbunch_back.setProperty("value", 20.0)
        self.sb_nbunch_back.setObjectName("sb_nbunch_back")
        self.gridLayout_5.addWidget(self.sb_nbunch_back, 0, 2, 1, 1)
        self.chb_a = QtWidgets.QCheckBox(self.groupBox_3)
        self.chb_a.setObjectName("chb_a")
        self.gridLayout_5.addWidget(self.chb_a, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_3, 2, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(290, 0))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_10.addWidget(self.widget_2, 0, 2, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_12.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pb_start = QtWidgets.QPushButton(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_start.sizePolicy().hasHeightForWidth())
        self.pb_start.setSizePolicy(sizePolicy)
        self.pb_start.setStyleSheet("color: rgb(255, 0, 0); font-size: 14pt;")
        self.pb_start.setObjectName("pb_start")
        self.gridLayout_11.addWidget(self.pb_start, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_11.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 2, 2, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_14.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pb_a = QtWidgets.QPushButton(self.groupBox_6)
        self.pb_a.setObjectName("pb_a")
        self.gridLayout_13.addWidget(self.pb_a, 1, 0, 1, 1)
        self.pb_logbook = QtWidgets.QPushButton(self.groupBox_6)
        self.pb_logbook.setObjectName("pb_logbook")
        self.gridLayout_13.addWidget(self.pb_logbook, 0, 0, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_13, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_6, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1159, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.lb_bnumber.setText(_translate("MainWindow", "Bunch number"))
        self.label.setText(_translate("MainWindow", "Avarage over N"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Calibration"))
        self.label_4.setText(_translate("MainWindow", "Central pixel [Px1]"))
        self.label_3.setText(_translate("MainWindow", "Central Energy [eV]"))
        self.label_2.setText(_translate("MainWindow", "ev/px"))
        self.pb_estim_px1.setText(_translate("MainWindow", "Estimate Px1"))
        self.chb_show_fit.setText(_translate("MainWindow", "Show Fit Func"))
        self.groupBox.setTitle(_translate("MainWindow", "DOOCS channels"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Background control"))
        self.pb_background.setText(_translate("MainWindow", "Take Background"))
        self.chb_a.setText(_translate("MainWindow", "subtract background"))
        self.label_5.setText(_translate("MainWindow", "N bunches"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Control"))
        self.pb_start.setText(_translate("MainWindow", "Start"))
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox"))
        self.pb_a.setText(_translate("MainWindow", "PB A"))
        self.pb_logbook.setText(_translate("MainWindow", "Print"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

