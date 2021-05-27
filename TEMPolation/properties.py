import sys
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenuBar, QMenu, \
    QPushButton, QLabel, QWidget, QLineEdit, QVBoxLayout, QMenuBar, \
    QPushButton, QMenu, QLayout, QCheckBox, QRadioButton, QPushButton, QLabel, QGroupBox, \
    QSizePolicy, QMessageBox, QWidget, QGridLayout 
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot as pyQtSlot, Qt, QUrl, QTimer, QSize

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class WidgetCreator(object):

    def __init__(self, parent):
        self.parent = parent

    def add_buttons(self, buttontext, tooltext, shortcuttext, movex, movey, sizex, sizey, sizetext, iconplace):        
        btn = QPushButton(buttontext, self.parent)
        btn.setFont(QtGui.QFont("Times", sizetext))
        btn.setToolTip(tooltext)
        btn.setStyleSheet("""QToolTip {background-color: white; color: black; border: black solid 1px}""")
        btn.setShortcut(shortcuttext)
        btn.setGeometry(movex, movey, sizex, sizey)
        btn.setIcon(QIcon(iconplace))
        btn.setIconSize(QtCore.QSize(sizex/2, sizey/2))
        return btn

    def add_label_title(self, sizex, sizey, movex, movey, sizetext, text):  # creating a label widget Title
        label_title = QLabel(self.parent)
        label_title.setFont(QtGui.QFont("Times", sizetext))
        label_title.setText(text)
        label_title.resize(sizex, sizey)
        label_title.move(movex, movey)
        label_title.setStyleSheet("border: 0px; background: none; color: rgba(0,0,98);")
        label_title.setAlignment(Qt.AlignCenter)
        label_title.setWordWrap(True)

    def add_label_text(self, sizex, sizey, movex, movey, sizetext, text):  # creating a label widget Text
        label_text = QLabel(self.parent)
        label_text.setFont(QtGui.QFont("Times", sizetext))
        label_text.setText(text)
        label_text.resize(sizex, sizey)
        label_text.move(movex, movey)
        label_text.setStyleSheet("border: 0px; background: none")
        label_text.setWordWrap(True)
        return label_text
    
    def add_textbox(self, sizex, sizey, movex, movey, text):  # Text Box
        textbox = QLineEdit(self.parent)
        textbox.move(movex, movey)
        textbox.setReadOnly(True)
        textbox.resize(sizex, sizey)
        textbox.setStyleSheet(" background: none")
        textbox.setPlaceholderText(text)

    def add_label_textcenter(self, sizex, sizey, movex, movey, sizetext, text):  # creating a label widget Text
        label_textcenter = QLabel(self.parent)
        label_textcenter.setFont(QtGui.QFont("Times", sizetext))
        label_textcenter.setText(text)
        label_textcenter.resize(sizex, sizey)
        label_textcenter.move(movex, movey)
        label_textcenter.setStyleSheet("border: 0px; background: none")
        label_textcenter.setAlignment(Qt.AlignCenter)
        label_textcenter.setWordWrap(True)

    def create_image(self, sizex, sizey, movex, movey):                           
        label = QLabel(self.parent)
        pixmap = QPixmap('image/Tempolation 1_image.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)

    def create_image_delete(self, sizex, sizey, movex, movey):
        label = QLabel(self.parent)
        pixmap = QPixmap('image/Table.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)

    def create_image_example1(self, sizex, sizey, movex, movey):
        label = QLabel(self.parent)
        pixmap = QPixmap('image/Text_exe1.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)

    def create_image_example2(self, sizex, sizey, movex, movey):
        label = QLabel(self.parent)
        pixmap = QPixmap('image/Text_exe2.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)

    def information2(self, sizex, sizey, movex, movey):
        label = QLabel(self.parent)
        pixmap = QPixmap('image/help.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setToolTip("Information: \n"
                         "Max. = Maximum Value \n"
                         "Min. = Minimum Value \n"
                         "Avg. = Average \n"
                         "NDP = number of data points \n"
                         "NMP = number of missing points \n"
                         "NMPS = number of missing points in a sequence \n")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)

    def create_imageRWTH(self, sizex, sizey, movex, movey):
        label = QLabel(self.parent)
        pixmap = QPixmap('image/rwth.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)

    def create_imageRWTHLOGO(self, sizex, sizey, movex, movey):
        label = QLabel(self.parent)
        pixmap = QPixmap('image/rwthlogo2.png')
        label.setStyleSheet("border: 0px; background: none")
        label.resize(sizex, sizey)
        label.move(movex, movey)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
