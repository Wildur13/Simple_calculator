# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_calculator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_calculator(object):
    def setupUi(self, calculator):
        if not calculator.objectName():
            calculator.setObjectName(u"calculator")
        calculator.resize(355, 509)
        calculator.setMinimumSize(QSize(0, 471))
        calculator.setMaximumSize(QSize(400, 554))
        self.gridLayout = QGridLayout(calculator)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_tan = QPushButton(calculator)
        self.btn_tan.setObjectName(u"btn_tan")
        self.btn_tan.setMinimumSize(QSize(40, 40))
        self.btn_tan.setMaximumSize(QSize(100, 110))
        self.btn_tan.setFlat(True)

        self.gridLayout.addWidget(self.btn_tan, 5, 0, 1, 1)

        self.btn_log = QPushButton(calculator)
        self.btn_log.setObjectName(u"btn_log")
        self.btn_log.setMinimumSize(QSize(40, 40))
        self.btn_log.setMaximumSize(QSize(100, 110))
        self.btn_log.setFlat(True)

        self.gridLayout.addWidget(self.btn_log, 5, 1, 1, 1)

        self.btn_exp = QPushButton(calculator)
        self.btn_exp.setObjectName(u"btn_exp")
        self.btn_exp.setMinimumSize(QSize(40, 40))
        self.btn_exp.setMaximumSize(QSize(100, 110))
        self.btn_exp.setFlat(True)

        self.gridLayout.addWidget(self.btn_exp, 5, 2, 1, 1)

        self.btn_div = QPushButton(calculator)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setMinimumSize(QSize(40, 40))
        self.btn_div.setMaximumSize(QSize(100, 110))
        self.btn_div.setFlat(True)

        self.gridLayout.addWidget(self.btn_div, 5, 3, 1, 1)

        self.btn_cos = QPushButton(calculator)
        self.btn_cos.setObjectName(u"btn_cos")
        self.btn_cos.setMinimumSize(QSize(40, 40))
        self.btn_cos.setMaximumSize(QSize(100, 110))
        self.btn_cos.setFlat(True)

        self.gridLayout.addWidget(self.btn_cos, 6, 0, 1, 1)

        self.btn_puissance = QPushButton(calculator)
        self.btn_puissance.setObjectName(u"btn_puissance")
        self.btn_puissance.setMinimumSize(QSize(40, 40))
        self.btn_puissance.setMaximumSize(QSize(100, 110))
        self.btn_puissance.setFlat(True)

        self.gridLayout.addWidget(self.btn_puissance, 4, 0, 1, 1)

        self.btn_sin = QPushButton(calculator)
        self.btn_sin.setObjectName(u"btn_sin")
        self.btn_sin.setMinimumSize(QSize(40, 40))
        self.btn_sin.setMaximumSize(QSize(100, 110))
        self.btn_sin.setFlat(True)

        self.gridLayout.addWidget(self.btn_sin, 6, 1, 1, 1)

        self.btn_off = QPushButton(calculator)
        self.btn_off.setObjectName(u"btn_off")
        self.btn_off.setMinimumSize(QSize(40, 40))
        self.btn_off.setMaximumSize(QSize(100, 110))
        self.btn_off.setFlat(True)

        self.gridLayout.addWidget(self.btn_off, 2, 0, 1, 1)

        self.btn_reset = QPushButton(calculator)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(40, 40))
        self.btn_reset.setMaximumSize(QSize(100, 110))
        self.btn_reset.setFlat(True)

        self.gridLayout.addWidget(self.btn_reset, 2, 3, 1, 1)

        self.operation = QLineEdit(calculator)
        self.operation.setObjectName(u"operation")
        self.operation.setMinimumSize(QSize(0, 35))
        font = QFont()
        font.setPointSize(14)
        self.operation.setFont(font)
        self.operation.setFrame(False)
        self.operation.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.operation, 0, 0, 1, 4)

        self.btn_inv = QPushButton(calculator)
        self.btn_inv.setObjectName(u"btn_inv")
        self.btn_inv.setMinimumSize(QSize(40, 40))
        self.btn_inv.setMaximumSize(QSize(100, 110))
        self.btn_inv.setFlat(True)

        self.gridLayout.addWidget(self.btn_inv, 4, 1, 1, 1)

        self.resultat = QLineEdit(calculator)
        self.resultat.setObjectName(u"resultat")
        self.resultat.setMinimumSize(QSize(0, 42))
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        font1.setWeight(75)
        self.resultat.setFont(font1)
        self.resultat.setFrame(False)
        self.resultat.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout.addWidget(self.resultat, 1, 0, 1, 4)

        self.btn_plus = QPushButton(calculator)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setMinimumSize(QSize(40, 40))
        self.btn_plus.setMaximumSize(QSize(100, 110))
        self.btn_plus.setFlat(True)

        self.gridLayout.addWidget(self.btn_plus, 8, 3, 1, 1)

        self.btn_1 = QPushButton(calculator)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(40, 40))
        self.btn_1.setMaximumSize(QSize(100, 110))
        self.btn_1.setFlat(True)

        self.gridLayout.addWidget(self.btn_1, 9, 0, 1, 1)

        self.btn_4 = QPushButton(calculator)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(40, 40))
        self.btn_4.setMaximumSize(QSize(100, 110))
        self.btn_4.setFlat(True)

        self.gridLayout.addWidget(self.btn_4, 8, 0, 1, 1)

        self.btn_8 = QPushButton(calculator)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setMinimumSize(QSize(40, 40))
        self.btn_8.setMaximumSize(QSize(100, 110))
        self.btn_8.setFlat(True)

        self.gridLayout.addWidget(self.btn_8, 7, 1, 1, 1)

        self.btn_7 = QPushButton(calculator)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setMinimumSize(QSize(40, 40))
        self.btn_7.setMaximumSize(QSize(100, 110))
        self.btn_7.setFlat(True)

        self.gridLayout.addWidget(self.btn_7, 7, 0, 1, 1)

        self.btn_mult = QPushButton(calculator)
        self.btn_mult.setObjectName(u"btn_mult")
        self.btn_mult.setMinimumSize(QSize(40, 40))
        self.btn_mult.setMaximumSize(QSize(100, 110))
        self.btn_mult.setFlat(True)

        self.gridLayout.addWidget(self.btn_mult, 6, 3, 1, 1)

        self.btn_3 = QPushButton(calculator)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(40, 40))
        self.btn_3.setMaximumSize(QSize(100, 110))
        self.btn_3.setFlat(True)

        self.gridLayout.addWidget(self.btn_3, 9, 2, 1, 1)

        self.btn_6 = QPushButton(calculator)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setMinimumSize(QSize(40, 40))
        self.btn_6.setMaximumSize(QSize(100, 110))
        self.btn_6.setFlat(True)

        self.gridLayout.addWidget(self.btn_6, 8, 2, 1, 1)

        self.btn_9 = QPushButton(calculator)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setMinimumSize(QSize(40, 40))
        self.btn_9.setMaximumSize(QSize(100, 110))
        self.btn_9.setFlat(True)

        self.gridLayout.addWidget(self.btn_9, 7, 2, 1, 1)

        self.btn_racine = QPushButton(calculator)
        self.btn_racine.setObjectName(u"btn_racine")
        self.btn_racine.setMinimumSize(QSize(40, 40))
        self.btn_racine.setMaximumSize(QSize(100, 110))
        self.btn_racine.setFlat(True)

        self.gridLayout.addWidget(self.btn_racine, 6, 2, 1, 1)

        self.btn_2 = QPushButton(calculator)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(40, 40))
        self.btn_2.setMaximumSize(QSize(100, 110))
        self.btn_2.setFlat(True)

        self.gridLayout.addWidget(self.btn_2, 9, 1, 1, 1)

        self.btn_0 = QPushButton(calculator)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setMinimumSize(QSize(40, 40))
        self.btn_0.setMaximumSize(QSize(100, 110))
        self.btn_0.setFlat(True)

        self.gridLayout.addWidget(self.btn_0, 10, 1, 1, 1)

        self.btn_point = QPushButton(calculator)
        self.btn_point.setObjectName(u"btn_point")
        self.btn_point.setMinimumSize(QSize(40, 40))
        self.btn_point.setMaximumSize(QSize(100, 110))
        self.btn_point.setFlat(True)

        self.gridLayout.addWidget(self.btn_point, 10, 2, 1, 1)

        self.btn_moins = QPushButton(calculator)
        self.btn_moins.setObjectName(u"btn_moins")
        self.btn_moins.setMinimumSize(QSize(40, 40))
        self.btn_moins.setMaximumSize(QSize(100, 110))
        self.btn_moins.setFlat(True)

        self.gridLayout.addWidget(self.btn_moins, 7, 3, 1, 1)

        self.btn_5 = QPushButton(calculator)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(40, 40))
        self.btn_5.setMaximumSize(QSize(100, 110))
        self.btn_5.setFlat(True)

        self.gridLayout.addWidget(self.btn_5, 8, 1, 1, 1)

        self.btn_mr = QPushButton(calculator)
        self.btn_mr.setObjectName(u"btn_mr")
        self.btn_mr.setMinimumSize(QSize(40, 40))
        self.btn_mr.setMaximumSize(QSize(100, 110))
        self.btn_mr.setFlat(True)

        self.gridLayout.addWidget(self.btn_mr, 4, 2, 1, 1)

        self.btn_mc = QPushButton(calculator)
        self.btn_mc.setObjectName(u"btn_mc")
        self.btn_mc.setMinimumSize(QSize(40, 40))
        self.btn_mc.setMaximumSize(QSize(100, 110))
        self.btn_mc.setFlat(True)

        self.gridLayout.addWidget(self.btn_mc, 3, 0, 1, 1)

        self.btn_mPlus = QPushButton(calculator)
        self.btn_mPlus.setObjectName(u"btn_mPlus")
        self.btn_mPlus.setMinimumSize(QSize(40, 40))
        self.btn_mPlus.setMaximumSize(QSize(100, 110))
        self.btn_mPlus.setFlat(True)

        self.gridLayout.addWidget(self.btn_mPlus, 3, 1, 1, 1)

        self.btn_mMoins = QPushButton(calculator)
        self.btn_mMoins.setObjectName(u"btn_mMoins")
        self.btn_mMoins.setMinimumSize(QSize(40, 40))
        self.btn_mMoins.setMaximumSize(QSize(100, 110))
        self.btn_mMoins.setFlat(True)

        self.gridLayout.addWidget(self.btn_mMoins, 3, 2, 1, 1)

        self.btn_backspace = QPushButton(calculator)
        self.btn_backspace.setObjectName(u"btn_backspace")
        self.btn_backspace.setMinimumSize(QSize(40, 40))
        self.btn_backspace.setMaximumSize(QSize(100, 110))
        self.btn_backspace.setFlat(True)

        self.gridLayout.addWidget(self.btn_backspace, 3, 3, 2, 1)

        self.btn_equal = QPushButton(calculator)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setMinimumSize(QSize(40, 40))
        self.btn_equal.setMaximumSize(QSize(100, 110))
        self.btn_equal.setFlat(True)

        self.gridLayout.addWidget(self.btn_equal, 9, 3, 2, 1)

        self.btn_percent = QPushButton(calculator)
        self.btn_percent.setObjectName(u"btn_percent")
        self.btn_percent.setMinimumSize(QSize(40, 40))
        self.btn_percent.setMaximumSize(QSize(100, 110))
        self.btn_percent.setFlat(True)

        self.gridLayout.addWidget(self.btn_percent, 2, 1, 1, 1)

        self.btn_degree = QPushButton(calculator)
        self.btn_degree.setObjectName(u"btn_degree")
        self.btn_degree.setMinimumSize(QSize(40, 40))
        self.btn_degree.setMaximumSize(QSize(100, 110))
        self.btn_degree.setFlat(True)

        self.gridLayout.addWidget(self.btn_degree, 10, 0, 1, 1)

        self.retranslateUi(calculator)

        QMetaObject.connectSlotsByName(calculator)

    # setupUi

    def retranslateUi(self, calculator):
        calculator.setWindowTitle(QCoreApplication.translate("calculator", u"simple_calculator", None))
        self.btn_tan.setText(QCoreApplication.translate("calculator", u"tan", None))
        self.btn_log.setText(QCoreApplication.translate("calculator", u"log", None))
        self.btn_exp.setText(QCoreApplication.translate("calculator", u"e", None))
        self.btn_div.setText(QCoreApplication.translate("calculator", u"/", None))
        self.btn_cos.setText(QCoreApplication.translate("calculator", u"cos", None))
        self.btn_puissance.setText(QCoreApplication.translate("calculator", u"10^", None))
        self.btn_sin.setText(QCoreApplication.translate("calculator", u"sin", None))
        self.btn_off.setText(QCoreApplication.translate("calculator", u"Off", None))
        self.btn_reset.setText(QCoreApplication.translate("calculator", u"AC", None))
        self.btn_inv.setText(QCoreApplication.translate("calculator", u"Inv", None))
        self.resultat.setText("")
        self.btn_plus.setText(QCoreApplication.translate("calculator", u"+", None))
        self.btn_1.setText(QCoreApplication.translate("calculator", u"1", None))
        self.btn_4.setText(QCoreApplication.translate("calculator", u"4", None))
        self.btn_8.setText(QCoreApplication.translate("calculator", u"8", None))
        self.btn_7.setText(QCoreApplication.translate("calculator", u"7", None))
        self.btn_mult.setText(QCoreApplication.translate("calculator", u"*", None))
        self.btn_3.setText(QCoreApplication.translate("calculator", u"3", None))
        self.btn_6.setText(QCoreApplication.translate("calculator", u"6", None))
        self.btn_9.setText(QCoreApplication.translate("calculator", u"9", None))
        self.btn_racine.setText(QCoreApplication.translate("calculator", u"\u221a", None))
        self.btn_2.setText(QCoreApplication.translate("calculator", u"2", None))
        self.btn_0.setText(QCoreApplication.translate("calculator", u"0", None))
        self.btn_point.setText(QCoreApplication.translate("calculator", u".", None))
        self.btn_moins.setText(QCoreApplication.translate("calculator", u"-", None))
        self.btn_5.setText(QCoreApplication.translate("calculator", u"5", None))
        self.btn_mr.setText(QCoreApplication.translate("calculator", u"MR", None))
        self.btn_mc.setText(QCoreApplication.translate("calculator", u"MC", None))
        self.btn_mPlus.setText(QCoreApplication.translate("calculator", u"M+", None))
        self.btn_mMoins.setText(QCoreApplication.translate("calculator", u"M-", None))
        self.btn_backspace.setText(QCoreApplication.translate("calculator", u"\u2190", None))
        self.btn_equal.setText(QCoreApplication.translate("calculator", u"=", None))
        self.btn_percent.setText(QCoreApplication.translate("calculator", u"%", None))
        self.btn_degree.setText(QCoreApplication.translate("calculator", u"Deg", None))
    # retranslateUi
