# -*- coding: utf-8 -*-
"""
TEMPolation is a program to interpolate temperature and humidity of a file which contains
missing values. The program give some statistic about the imported file and also interpolate the missing
data with different methods.

TEMPolation was developed by:
Daniel Coronado

Methods:
Linear Interpolation
Makima Interpolation
Pchip Interpolation

Files:
Main file - The file is the main file where you should run.
Frame - Contains the Ui of the program.
Properties - Contains the most important functions (Button, label, ...)
"""

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QLabel, QWidget, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot as pyQtSlot
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

# from frame import Window1, Window2, Window3, Window4, Window5, Window6, AnotherWindow1, AnotherWindow2
from properties import *
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Properties of the program
        sizeObject = QtWidgets.QDesktopWidget().availableGeometry(-1)
        windowcenterx = sizeObject.width()
        windowcentery = sizeObject.height()

        # Real size of the screen
        windowsizereal = sizeObject.width()

        # Determine size the size of the Window
        if windowsizereal >= 3800:  # Monitor4K
            windowsizecalc = 1300
            f = 0.7
        elif windowsizereal >= 2500:
            windowsizecalc = 1280
            f = 0.7
        elif windowsizereal >= 1850:
            windowsizecalc = 960
            f = 0.8
        elif windowsizereal >= 1500:
            windowsizecalc = 800
            f = 0.9
        elif windowsizereal >= 1200:  # Laptop
            windowsizecalc = 600
            f = 1
        else:
            windowsizecalc = 400
            f = 1

        self.centerx = int((windowcenterx - windowsizecalc) / 2)
        self.centery = int((windowcentery - windowsizecalc) / 2)
        self.width = windowsizecalc
        self.height = windowsizecalc

        # Configuration of the screen
        self.setWindowIcon(QIcon('image/Tempolation 1_logo.png'))
        self.setWindowTitle('TEMPolation')
        self.setFixedHeight(self.height)
        self.setFixedWidth(self.width)
        self.setGeometry(self.centerx, self.centery, self.width, self.height)
        self.setStyleSheet('''background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fdfbf7, stop: 1 #b9c7bd);
                            border-style: solid;border-width: 1px;
                            border-radius: 0px;
                            border-color: #b9c7bd;padding: 3px;''')

        # Determine the proportion of the widgets size
        global p
        p = float(windowsizecalc / 600)

        # Determine the proportion of the text
        global p_f
        p_f = p * f

        # Start the 1st Window
        self.startUIWindow1()

    def startUIWindow1(self):  # WINDOW 1 (Main Window)

        # Call a class to fit in the fields
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Buttons Creation
        self.btn_next = widget_creator.add_buttons(" Next", 'Next Step', 'right', p * 300, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/next.png')
        self.btn_methods = widget_creator.add_buttons(" Methods", 'Methods', 'ctrl + m', p * 200, p * 520, p * 100,
                                                      p * 30, p_f * 9, 'image/methods.png')
        self.btn_help = widget_creator.add_buttons(" Contact", 'Cotact for help', 'ctrl + h', p * 200, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/email.png')
        self.btn_exit = widget_creator.add_buttons(" Exit", 'Exit the program', 'esc', p * 300, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/exit.png')

        # Image Creation (sizex, sizey, movex, movey)
        widget_creator.create_imageRWTH(p * 300, p * 70, p * 165, p * 1)
        widget_creator.create_image(p * 300, p * 300, p * 155, p * 80)

        # Text Creation
        widget_creator.add_label_text(p * 550, p * 50, p * 25, p * 400, p_f * 10,
                                      '<b>TEMPolation </b>is a program to interpolate a data file that contains missing data (temperature and humidity) using 3 different methods (Linear, Makima, or Pchip).')
        widget_creator.add_label_text(p * 550, p * 50, p * 25, p * 450, p_f * 10,
                                      '<b>TEMPolation </b>works as a step-by-step program and it is divided into 4 steps, press next to go for the next steps.')

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Determine the source page
        self.pag_number = 1

        # Buttons Connection
        self.btn_next.clicked.connect(self.startUIWindow2)
        self.btn_methods.clicked.connect(self.popup1)
        self.btn_help.clicked.connect(self.popup2)
        self.btn_exit.clicked.connect(self.close)

        # Show Window
        self.show()

    def startUIWindow2(self):  # WINDOW 2 (Introduction)

        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Buttons Creation
        self.btn_next = widget_creator.add_buttons(" Next", 'Next Step', 'right', p * 300, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/next.png')
        self.btn_back = widget_creator.add_buttons(" Back", 'Previous Step', 'left', p * 200, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/back.png')
        self.btn_restart = widget_creator.add_buttons(" Restart", 'Start again', 'ctrl + n', p * 200, p * 560, p * 100,
                                                      p * 30, p_f * 9, 'image/restart.png')
        self.btn_exit = widget_creator.add_buttons(" Exit", 'Exit the program', 'esc', p * 300, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/exit.png')

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 25, '<b>Introduction</b>')

        # Text Creation
        widget_creator.add_label_text(p * 100, p * 30, p * 40, p * 100, p_f * 15, '<b>Step 1:</b>')
        widget_creator.add_label_text(p * 520, p * 60, p * 45, p * 120, p_f * 10,
                                      'This step consists to import the file. The file must be in the format (.xlsx) or (txt). Examples and more information in the next step.')

        widget_creator.add_label_text(p * 100, p * 30, p * 40, p * 200, p_f * 15, '<b>Step 2:</b>')
        widget_creator.add_label_text(p * 520, p * 60, p * 45, p * 220, p_f * 10,
                                      'In the pre-interpolation part, it is possible to view the plot of the attached file and other information such as (maximum, minimum, average, and others).')

        widget_creator.add_label_text(p * 100, p * 30, p * 40, p * 300, p_f * 15, '<b>Step 3:</b>')
        widget_creator.add_label_text(p * 535, p * 60, p * 45, p * 320, p_f * 10,
                                      'In the post-interpolation part, it is possible to choose the interpolation method (Linear, Makima, or Pchip) and observe how the interpolation methods differ between them.')

        widget_creator.add_label_text(p * 100, p * 30, p * 40, p * 400, p_f * 15, '<b>Step 4:</b>')
        widget_creator.add_label_text(p * 530, p * 60, p * 45, p * 420, p_f * 10,
                                      'The last part has a preview of the table with the new data and allows saving the file with the new interpolated values. The graph can be saved directly from the graphs.')

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Buttons Connection
        self.btn_next.clicked.connect(self.startUIWindow3)
        self.btn_back.clicked.connect(self.startUIWindow1)
        self.btn_restart.clicked.connect(self.startUIWindow1)
        self.btn_exit.clicked.connect(self.close)

        # Show Window
        self.show()

    def startUIWindow3(self):  # WINDOW 3 (Import Data)

        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Buttons Creation
        self.btn_next = widget_creator.add_buttons(" Next", 'Next Step', 'right', p * 300, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/next.png')
        self.btn_next.setEnabled(False)
        self.btn_back = widget_creator.add_buttons(" Back", 'Previous Step', 'left', p * 200, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/back.png')
        self.btn_restart = widget_creator.add_buttons(" Restart", 'Start again', 'ctrl + n', p * 200, p * 560, p * 100,
                                                      p * 30, p_f * 9, 'image/restart.png')
        self.btn_exit = widget_creator.add_buttons(" Exit", 'Exit the program', 'esc', p * 300, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/exit.png')
        self.btn_browse = widget_creator.add_buttons(" Browse", 'Search file place', 'ctrl + o', p * 475, p * 110,
                                                     p * 100, p * 30, p_f * 9, 'image/file.png')

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 25, '<b>Import Data</b>')

        # Text Creation
        widget_creator.add_label_text(p * 150, p * 50, p * 20, p * 100, p_f * 10, '<b>File Name:</b>')
        widget_creator.add_label_text(p * 375, p * 50, p * 200, p * 150, p_f * 10,
                                      'The compatible files for this program are text file (.txt) or Excel File (.xlsx) and must have this configuration:')
        widget_creator.add_label_text(p * 450, p * 50, p * 200, p * 190, p_f * 10, '<b>1st column</b> ➞ Time')
        widget_creator.add_label_text(p * 400, p * 50, p * 200, p * 220, p_f * 10,
                                      '<b>1st column</b> ➞ Time has to be time-sensitive')
        widget_creator.add_label_text(p * 400, p * 50, p * 200, p * 250, p_f * 10,
                                      '<b>2nd column</b> ➞ Temperature or Humidity')
        widget_creator.add_label_text(p * 400, p * 50, p * 200, p * 280, p_f * 10,
                                      '<b>1st line</b> ➞ Title of your choice')
        widget_creator.add_label_text(p * 400, p * 50, p * 200, p * 310, p_f * 10, '<b>No value</b> ➞ Has to be empty')
        widget_creator.add_label_text(p * 400, p * 50, p * 200, p * 340, p_f * 10,
                                      '<b>Excel</b> ➞ Has to start in column "A"; line "1"; Sheet "1"')

        # Image Creation (sizex, sizey, movex, movey)
        widget_creator.add_label_text(p * 450, p * 50, p * 20, p * 150, p_f * 10, '<b>Text file</b>')
        widget_creator.create_image_example1(p * 90, p * 160, p * 100, p * 160)
        widget_creator.add_label_text(p * 450, p * 50, p * 20, p * 310, p_f * 10, '<b>Excel file</b>')
        widget_creator.create_image_example2(p * 90, p * 180, p * 100, p * 320)

        # Define the fild that will receive  the pacht of the file
        self.textbox_path = QLineEdit(self.centralwidget)
        self.textbox_path.setFont(QtGui.QFont("Times", round(p_f * 10)))
        self.textbox_path.move(round(p * 100), round(p * 112))
        self.textbox_path.resize(round(p * 360), round(p * 25))
        self.textbox_path.setReadOnly(True)
        self.textbox_path.setStyleSheet(" background: none")
        self.textbox_path.setPlaceholderText('Please insert path file')

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Buttons Connection
        self.btn_next.clicked.connect(self.startUIWindow4)
        self.btn_back.clicked.connect(self.startUIWindow2)
        self.btn_restart.clicked.connect(self.startUIWindow1)
        self.btn_exit.clicked.connect(self.close)
        self.btn_browse.clicked.connect(self.select_files)

        # Show Window
        self.show()

    def select_files(self):  # Method to import the file

        # Select the file to be imported
        self.file = QFileDialog.getOpenFileName(self, "Select Files", "", "(*.txt);;(*.xlsx)")

        # Get the patch of the imported file
        self.path = self.file[0]

        # Verify if the a file was selected
        if self.path == "":
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Any file was selected")
            self.msgBox.setWindowTitle("Error Message")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec()

        # Read the imported file
        else:

            # Define the global variable to receive the imported data
            global data

            # Verify the extension of the file (.txt or .xlsx)
            if self.path.lower().endswith(".txt"):
                # print("txt")
                data = pd.read_csv(self.path, sep='\s+')

            elif self.path.lower().endswith(".xlsx"):
                # print("xlsx")
                data = pd.read_excel(self.path)

            # amount of columns
            self.qtde = len(data.columns)

            # amount of lines in each column
            self.column_1 = data.iloc[:, 0].count()
            self.column_2 = data.iloc[:, 1].count()

            # amount of zero values
            self.qtde_nan = data.iloc[:, 1].isna().sum()

            # Check if there are any duplicate values in the first column
            self.boolean = data.iloc[:, 0].duplicated().any()

            # Verify if the file is in the correct format
            # if not, inform error
            if (self.qtde != 2) or (self.column_1 < self.column_2) or (self.boolean == True):
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText("The imported file is not in the correct format, please verify!")
                self.msgBox.setWindowTitle("Error Message")
                self.msgBox.setStandardButtons(QMessageBox.Ok)
                self.msgBox.exec()

            elif self.qtde_nan > (self.column_1 * 0.1):
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText("The file contains more than 10% of the values missing, please verify!")
                self.msgBox.setWindowTitle("Error Message")
                self.msgBox.setStandardButtons(QMessageBox.Ok)
                self.msgBox.exec()

            # If it is, pass the address in the window Qline and display a success message
            else:
                self.textbox_path.setText(self.path)
                self.btn_next.setEnabled(True)

                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText("File imported with success!")
                self.msgBox.setWindowTitle("Information")
                self.msgBox.setStandardButtons(QMessageBox.Ok)
                self.msgBox.exec()

    def calcular_nmps(self, data):
        self.qtde_vazia = 0
        self.maior_qtde_vazia = 0
        self.qtde_linhas = data.iloc[:, 0].count()
        i = 5
        for i in range(self.qtde_linhas):
            self.celula = data.iloc[i, 1]
            if pd.isnull(self.celula) == True:
                self.qtde_vazia = self.qtde_vazia + 1

            else:
                if self.qtde_vazia > self.maior_qtde_vazia:
                    self.maior_qtde_vazia = self.qtde_vazia

                self.qtde_vazia = 0

        return self.maior_qtde_vazia

    def grafico(self):
        # Set the chart and its position
        self.canvas = Canvas(self.centralwidget, width=8, height=3)
        self.canvas.setGeometry(round(p * 20), round(p * 140), round(p * 560), round(p * 320))

        # Define the axes
        self.x = data.iloc[:, 0]
        self.y = data.iloc[:, 1]

        global x, y
        x = self.x.values.tolist()
        y = self.y.values.tolist()

        try:
            self.canvas.ax.plot(self.x, self.y, 'o', markersize=4)
        except:
            self.x = self.x.astype(str)
            self.canvas.ax.plot(self.x, self.y, 'o', markersize=4, size=15)

        # Generate the name of the axes
        self.canvas.ax.set_xlabel(data.columns[0], size=20)
        self.canvas.ax.set_ylabel(data.columns[1], size=20)

        # Gather information to assemble the absence lines
        self.qtde_linhas = data.iloc[:, 0].count()
        self.max = data.max()
        self.min = data.min()

        # determine the position of the missing values
        self.list_null = []
        for i in range(self.qtde_linhas):
            self.celula = data.iloc[i, 1]
            if pd.isnull(self.celula) == True:
                self.celula = data.iloc[i, 0]
                self.list_null.append(self.celula)

        # Generate line graph of the missing values
        for i in range(len(self.list_null)):
            self.canvas.ax.plot([self.list_null[i], self.list_null[i]],
                                [self.min[1], self.max[1]],
                                'k-', lw=2, color='r')

        self.canvas.ax.set_position([0.07, 0.1, 0.9, 0.85])  # left,bottom,width,height

        # Generate navigation bar
        self.toolbar = NavigationToolbar(self.canvas, self.centralwidget)
        self.toolbar.setGeometry(round(p * 20), round(p * 105), round(p * 560), round(p * 30))

    def startUIWindow4(self):  # WINDOW 4 (Pre-Interpolation)

        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Buttons Creation
        self.btn_next = widget_creator.add_buttons(" Next", 'Next Step', 'right', p * 300, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/next.png')
        self.btn_back = widget_creator.add_buttons(" Back", 'Previous Step', 'left', p * 200, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/back.png')
        self.btn_restart = widget_creator.add_buttons(" Restart", 'Start again', 'ctrl + n', p * 200, p * 560, p * 100,
                                                      p * 30, p_f * 9, 'image/restart.png')
        self.btn_exit = widget_creator.add_buttons(" Exit", 'Exit the program', 'esc', p * 300, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/exit.png')

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 25, '<b>Pre-Interpolation</b>')

        # Show the plot
        self.grafico()

        # Calculate the required information
        self.max = data.max()
        self.max = str(round(self.max[1], 2))
        self.min = data.min()
        self.min = str(round(self.min[1], 2))
        self.mean = data.mean()
        self.mean = str(round(self.mean[1], 2))
        self.ndp = str(round(data.iloc[:, 0].count(), 2))
        self.nmp = str(round(data.iloc[:, 1].isna().sum(), 2))
        self.nmps = str(round(self.calcular_nmps(data), 2))

        # Text Creation
        widget_creator.information2(p * 20, p * 20, p * 80, p * 480)
        self.label_max = widget_creator.add_label_text(p * 150, p * 50, p * 115, p * 450, p_f * 10,
                                                       '<b>Max.: </b>' + self.max)  # Max Value
        self.label_max.setToolTip("Maximum value")
        self.label_min = widget_creator.add_label_text(p * 150, p * 50, p * 265, p * 450, p_f * 10,
                                                       '<b>Min.: </b>' + self.min)  # Min Value
        self.label_min.setToolTip("Minimum value")
        self.label_avarg = widget_creator.add_label_text(p * 150, p * 50, p * 415, p * 450, p_f * 10,
                                                         '<b>Avg.: </b>' + self.mean)  # Avarge Value
        self.label_avarg.setToolTip("Average")
        self.label_ndp = widget_creator.add_label_text(p * 150, p * 50, p * 115, p * 475, p_f * 10,
                                                       '<b>NDP: </b>' + self.ndp)  # Number of data points
        self.label_ndp.setToolTip("Number of data points")
        self.label_nmp = widget_creator.add_label_text(p * 150, p * 50, p * 265, p * 475, p_f * 10,
                                                       '<b>NMP: </b>' + self.nmp)  # Number of missing points
        self.label_nmp.setToolTip("Number of missing points")
        self.label_nmps = widget_creator.add_label_text(p * 150, p * 50, p * 415, p * 475, p_f * 10,
                                                        '<b>NMPS: </b>' + self.nmps)  # Number of missing points in a sequence
        self.label_nmps.setToolTip("Number of missing points in sequence")

        # Connect the Buttons
        self.btn_next.clicked.connect(self.startUIWindow5)
        self.btn_back.clicked.connect(self.startUIWindow3)
        self.btn_restart.clicked.connect(self.startUIWindow1)
        self.btn_exit.clicked.connect(self.close)

        # Caixas de encaixe nas janelas
        self.setCentralWidget(self.centralwidget)

        # Fit boxs in the windowns
        self.show()

    def interpolation(self, metodo):
        # clear the chart information
        self.canvas.ax.cla()

        # define the x and y axes
        self.x = data.iloc[:, 0]
        self.y = data.iloc[:, 1]

        # Perform the interpolation according to the method passed
        self.y = self.y.interpolate(method=metodo)

        global x, y
        x = self.x.values.tolist()
        y = self.y.values.tolist()

        # Generate the name of the axes
        self.canvas.ax.set_xlabel(data.columns[0], size=20)
        self.canvas.ax.set_ylabel(data.columns[1], size=20)

        # Generate the dot plot
        try:
            self.canvas.ax.plot(self.x, self.y, 'o', markersize=4)
        except:
            self.x = self.x.astype(str)
            self.canvas.ax.plot(self.x, self.y, 'o', markersize=4)

        # Generate the line chart
        self.canvas.ax.plot(self.x, self.y, '-')

        # Gather information to assemble the absence lines
        self.qtde_linhas = data.iloc[:, 0].count()
        self.max = data.max()
        self.min = data.min()

        # determine the lenght of the line 
        self.length = (self.max[1] - self.min[1]) * 0.1
        self.position = self.min[1] + self.length

        # determine the position of the missing values
        self.list_null = []
        for i in range(self.qtde_linhas):
            self.celula = data.iloc[i, 1]
            if pd.isnull(self.celula) == True:
                self.celula = data.iloc[i, 0]
                self.list_null.append(self.celula)

        # Generate line graph of the missing values
        for i in range(len(self.list_null)):
            self.canvas.ax.plot([self.list_null[i], self.list_null[i]],
                                [self.min[1], self.position],
                                'k-', lw=2, color='r')

        # Display the graph
        self.canvas.draw()

        # Set variable to receive data after interpolation
        self.data_pos_interpolation = pd.concat([self.x, self.y], axis=1)

    def startUIWindow5(self):  # WINDOW 5 (Post-Interpolation)
        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Buttons Creation
        self.btn_next = widget_creator.add_buttons(" Next", 'Next Step', 'right', p * 300, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/next.png')
        self.btn_back = widget_creator.add_buttons(" Back", 'Previous Step', 'left', p * 200, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/back.png')
        self.btn_restart = widget_creator.add_buttons(" Restart", 'Start again', 'ctrl + n', p * 200, p * 560, p * 100,
                                                      p * 30, p_f * 9, 'image/restart.png')
        self.btn_exit = widget_creator.add_buttons(" Exit", 'Exit the program', 'esc', p * 300, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/exit.png')

        # Setting the interpolation type buttons
        self.btn_linear = widget_creator.add_buttons(" Linear", 'Linear Interpolation', '', p * 150, p * 470, p * 100,
                                                     p * 30, p_f * 9, 'image/line.png')
        self.btn_akima = widget_creator.add_buttons(" Makima", 'Makima Interpolation', '', p * 250, p * 470, p * 100,
                                                    p * 30, p_f * 9, 'image/curve1.png')
        self.btn_pchip = widget_creator.add_buttons(" Pchip", 'Pchip Interpolation ', '', p * 350, p * 470, p * 100,
                                                    p * 30, p_f * 9, 'image/curve2.png')

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 25, '<b>Post-Interpolation</b>')
        self.grafico()

        # Buttons Connection
        self.btn_next.clicked.connect(self.startUIWindow6)
        self.btn_back.clicked.connect(self.startUIWindow4)
        self.btn_restart.clicked.connect(self.startUIWindow1)
        self.btn_exit.clicked.connect(self.close)

        # Interpolation button connection
        self.btn_linear.clicked.connect(lambda: self.interpolation('linear'))
        self.btn_akima.clicked.connect(lambda: self.interpolation('akima'))
        self.btn_pchip.clicked.connect(lambda: self.interpolation('pchip'))

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Show Window
        self.show()

    def select_directory(self):  # Method for exporting file
        # Select path and file name
        self.file = QFileDialog.getSaveFileName(self, "Save file", "", "(*.txt);;(*.xlsx)")
        self.path = self.file[0]

        # Check if a file has been chosen, if not, display a document not saved message
        if self.path == "":
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Document was not saved")
            self.msgBox.setWindowTitle("Error Message")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec()

        # Check the file extension, proceed with the export and display a success message
        else:
            if self.path.lower().endswith(".txt"):
                self.data_pos_interpolation.to_csv(self.path, sep=' ', index=False, header=True)

            elif self.path.lower().endswith(".xlsx"):
                self.data_pos_interpolation.to_excel(self.path, index=False, header=True)

            self.textbox_path.setText(self.path)
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("Document saved")
            self.msgBox.setWindowTitle("Message")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec()

    def createTable(self):
        # Creat table
        self.tableWidget = QTableWidget(self.centralwidget)

        self.tableWidget.setGeometry(round(p * 150), round(p * 100), round(p * 300), round(p * 280))  # left,bottom,width,height

        # Count how many line and columns
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)

        # Define title name and ajust with the table
        self.tableWidget.setHorizontalHeaderLabels([data.columns[0], data.columns[1]])

        # Define size of the columns
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 100)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setFixedHeight(round(p * 30))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setShowGrid(True)

        # Loop to insert lines in the table
        for i in range(len(data)):
            # Count of lines (actual)
            linha = self.tableWidget.rowCount()

            # Insert 1 line
            self.tableWidget.insertRow(linha)

            self.item_x = QTableWidgetItem(str(x[i]))
            self.item_x.setTextAlignment(round(QtCore.Qt.AlignVCenter) |
                                         round(QtCore.Qt.AlignHCenter))
            self.tableWidget.setItem(linha, 0, self.item_x)

            self.item_y = QTableWidgetItem(str(y[i]))
            self.item_y.setTextAlignment(round(QtCore.Qt.AlignVCenter) |
                                         round(QtCore.Qt.AlignHCenter))
            self.tableWidget.setItem(linha, 1, self.item_y)

    def startUIWindow6(self):  # WINDOW 6 (Export File)
        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Buttons Creation
        self.btn_back = widget_creator.add_buttons(" Back", 'Previous Step', 'left', p * 200, p * 520, p * 100, p * 30,
                                                   p_f * 9, 'image/back.png')
        self.btn_restart = widget_creator.add_buttons(" Restart", 'Start again', 'ctrl + n', p * 200, p * 560, p * 100,
                                                      p * 30, p_f * 9, 'image/restart.png')
        self.btn_exit = widget_creator.add_buttons(" Exit", 'Exit the program', 'esc', p * 300, p * 560, p * 100,
                                                   p * 30, p_f * 9, 'image/exit.png')
        self.btn_help = widget_creator.add_buttons(" Contact", 'Cotact for help', 'ctrl + h', p * 300, p * 520, p * 100,
                                                   p * 30, p_f * 9, 'image/email.png')
        self.btn_browse = widget_creator.add_buttons(" Browse", 'Search file place', 'ctrl + o', p * 475, p * 408,
                                                     p * 100, p * 30, p_f * 9, 'image/file.png')

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 25, '<b>Export File and Plot</b>')
        self.createTable()

        # Text Creation
        widget_creator.add_label_text(p * 150, p * 50, p * 20, p * 397, p_f * 10, '<b>Save File:</b>')
        widget_creator.add_label_text(p * 375, p * 50, p * 100, p * 430, p_f * 10,
                                      'The data file can be saved in .txt or .xlsx format. The new values with the interpolated data will be added in the file.')

        # Definition of the field that will receive the file path
        self.textbox_path = QLineEdit(self.centralwidget)
        self.textbox_path.setFont(QtGui.QFont("Times", round(p_f * 10)))
        self.textbox_path.move(round(p * 100), round(p * 410))
        self.textbox_path.resize(round(p * 360), round(p * 25))
        self.textbox_path.setReadOnly(True)
        self.textbox_path.setStyleSheet(" background: none")
        self.textbox_path.setPlaceholderText('')

        # Determine the source page
        self.pag_number = 6

        # Buttons Connection
        self.btn_back.clicked.connect(self.startUIWindow5)
        self.btn_restart.clicked.connect(self.startUIWindow1)
        self.btn_exit.clicked.connect(self.close)
        self.btn_browse.clicked.connect(self.select_directory)
        self.btn_help.clicked.connect(self.popup2)

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Show Window
        self.show()

    def popup1(self):  # Methods
        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 20, '<b>Methods</b>')

        # Text Creation
        widget_creator.add_label_text(p * 300, p * 30, p * 20, p * 100, p_f * 12, '<b>Linear Interpolation:</b>')
        widget_creator.add_label_text(p * 550, p * 80, p * 20, p * 125, p_f * 10,
                                      'In numerical analysis, linear interpolation consists of approximating a function in an interval by a linear function, using first-degree polynomials. If the two known points are given by the coordinates(x0,y0)and(x1,y1), the linear interpolation is the straight line between these points.')

        widget_creator.add_label_text(p * 300, p * 30, p * 20, p * 200, p_f * 12, '<b>Makima:</b>')
        widget_creator.add_label_text(p * 550, p * 80, p * 20, p * 222, p_f * 10,
                                      'Modified Akima piecewise cubic Hermite interpolation (Makima) as the name says is a modification of the Akima Interpolation. The original Akima algorithm gives equal weight to the points on both sides, the Makima give difference weights regarding the distance between the points.')

        widget_creator.add_label_text(p * 300, p * 30, p * 20, p * 300, p_f * 12, '<b>Pchip:</b>')
        widget_creator.add_label_text(p * 550, p * 80, p * 20, p * 320, p_f * 10,
                                      'In the mathematical field of numerical analysis, a spline interpolation is a form of interpolation where the interpolated is a special type of piecewise polynomial called a spline. That is, instead of fitting a single, high-degree polynomial to all of thevalues at once, spline interpolation fits low-degree polynomials to small subsets of the values.')

        widget_creator.add_label_text(p * 550, p * 60, p * 20, p * 400, p_f * 8,
                                      '<i>For more information check the master thesis "Evaluation of different interpolations techniques for missing data - internal and external humidity and temperature." RWTH-Aachen 2021 by Joao Daniel Coronado Pinho.</i>')

        # Buttons Creation
        self.btn_ok = widget_creator.add_buttons(" ok", 'OK', 'enter', p * 250, p * 520, p * 100, p * 30, p_f * 9,
                                                 'image/check.png')

        # Buttons Connection
        self.btn_ok.clicked.connect(self.startUIWindow1)

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Show Window
        self.show()

    def popup2(self):  # Help
        # Fit boxs in the windowns
        self.centralwidget = QWidget(self)
        widget_creator = WidgetCreator(self.centralwidget)

        # Title Creation
        widget_creator.add_label_title(p * 400, p * 50, p * 100, p * 25, p_f * 20, '<b>Contact Us</b>')

        # Text Creation
        widget_creator.add_label_textcenter(p * 400, p * 150, p * 100, p * 30, p_f * 10,
                                            'If you have any questions, please feel free to contact us:')
        widget_creator.add_label_textcenter(p * 400, p * 150, p * 100, p * 60, p_f * 11, '<b>Daniel Coronado</b>')
        widget_creator.add_label_textcenter(p * 400, p * 150, p * 100, p * 80, p_f * 11, 'danielcoronado92@gmail.com ')

        widget_creator.add_label_textcenter(p * 400, p * 150, p * 100, p * 110, p_f * 11, '<b>Avichal Malhotra</b>')
        widget_creator.add_label_textcenter(p * 400, p * 150, p * 100, p * 130, p_f * 11, 'malhotra@e3d.rwth-aachen.de')

        widget_creator.create_imageRWTH(p * 230, p * 85, p * 200, p * 230)
        widget_creator.create_image(p * 170, p * 170, p * 230, p * 330)

        # Buttons Creation
        self.btn_ok = widget_creator.add_buttons(" ok", 'OK', 'enter', p * 250, p * 520, p * 100, p * 30, p_f * 9, 'image/check.png')

        # Determine which button to connect to via the source page
        # Origem startUIWindow1
        if self.pag_number == 1:

            self.btn_ok.clicked.connect(self.startUIWindow1)

        # Origem startUIWindow6
        elif self.pag_number == 6:
            self.btn_ok.clicked.connect(self.startUIWindow6)

        # Fit boxs in the windowns
        self.setCentralWidget(self.centralwidget)

        # Show Window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
