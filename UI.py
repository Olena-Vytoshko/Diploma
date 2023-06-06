from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from Markov_chain_1_order import *
from app import *
import psycopg2
import sys


def define_query(choose_parameter):
    if choose_parameter == 'Виконавець':
        parameter = 'artist'
    elif choose_parameter == 'Жанр':
        parameter = 'genre'
    else:
        parameter = 'melodytype'
    new_query = "SELECT %sname FROM %s"
    return new_query % (parameter, parameter)


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.updateComboBox.currentIndexChanged.connect(self.updateComboBox_2)

    # print(execute_query(connection_to_DB(), define_query('Виконавець')))
    Form, Window = uic.loadUiType("app.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    form.comboBox.addItem('Виконавець')
    form.comboBox.addItem('Жанр')
    form.comboBox.addItem('Тип')

    def updateComboBox_2(self):
        self.comboBox_2.clear()
        selected_item = self.comboBox.currentText()
        conn = connection_to_DB()
        cursor = conn.cursor()
        query_for_comboBox_2(selected_item)
        cursor.execute(query_for_comboBox_2(selected_item))
        rows = cursor.fetchall()
        for row in rows:
            self.comboBox_2.addItem(row[0])
        conn.close()

    app.exec()







