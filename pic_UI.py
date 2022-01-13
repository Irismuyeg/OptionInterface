# -*-coding:utf-8-*-
from PyQt5.QtWidgets import QLabel, QLineEdit, QApplication
from PyQt5.QtGui import *
# import os


# from PyQt5.QtCore import *



def result(page):
    # 标题
    # label_main = QLabel()
    # label_main.setFont(page.font_main)
    # label_main.setText("  Back-test Results")
    # page.grid.addWidget(label_main, 1, 0, 1, 4)
    # # 文字
    # label_hint = QLabel()
    # label_hint.setFont(page.font_content)
    # label_hint.setText("      These are the results")
    # page.grid.addWidget


    #pics
    # F.fig.add_subplot(2, 1, 0)
    label_monthly_returns = QLabel()
    label_monthly_returns.setPixmap(QPixmap('../frontend/monthly_returns.png').scaled(500, 400))
    # label_monthly_returns.setEnabled(False)
    page.grid.addWidget(label_monthly_returns, 0, 0)

    label_pnl = QLabel()
    label_pnl.setPixmap(QPixmap('../frontend/daily_PnL.png').scaled(500, 400))
    # # label_pnl.setEnabled(False)
    page.grid.addWidget(label_pnl, 1, 0)