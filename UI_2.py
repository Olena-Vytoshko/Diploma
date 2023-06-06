from PyQt5 import QtCore, QtGui, QtWidgets
from Markov_chain_1_order import *
from Markov_chain_2_order import *


def query_for_comboBox_2(choose_parameter):
    if choose_parameter == 'Виконавець':
        parameter = 'artist'
    elif choose_parameter == 'Жанр':
        parameter = 'genre'
    else:
        parameter = 'melodytype'
    new_query = "SELECT %sname FROM %s"
    return new_query % (parameter, parameter)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 739)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\olena\\PycharmProjects\\Diploma\\../../OneDrive/Pulpit/istockphoto-1394280873-612x612.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-6)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(450, 30, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 17, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 221, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 131, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 70, 321, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 30, 341, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 60, 341, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(590, 110, 331, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 80, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(130, 260, 281, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 219, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 220, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(500, 260, 281, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tableView_2.setFont(font)
        self.tableView_2.setObjectName("tableView_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 510, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 600, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(790, 150, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(880, 80, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.comboBox.setPlaceholderText("Виберіть елемент")
        self.comboBox.addItem('Жанр')
        self.comboBox.addItem('Виконавець')
        self.comboBox.addItem('Тип')


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Generator"))
        self.label.setText(_translate("MainWindow", "Параметр"))
        self.label_2.setText(_translate("MainWindow", "Значення параметра"))
        self.pushButton.setText(_translate("MainWindow", "Фільтрувати базу за цим параметром"))
        self.groupBox.setTitle(_translate("MainWindow", "Ритм"))
        self.radioButton.setText(_translate("MainWindow", "Шаблон 1"))
        self.radioButton_2.setText(_translate("MainWindow", "Шаблон 2"))
        self.radioButton_3.setText(_translate("MainWindow", "Шаблон 3"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Генерувати за допомогою"))
        self.radioButton_4.setText(_translate("MainWindow", "Ланцюгів Маркова I порядку"))
        self.radioButton_5.setText(_translate("MainWindow", "Ланцюгів Маркова II порядку"))
        self.label_3.setText(_translate("MainWindow", "Довжина мелодії (кількість нот): "))
        self.label_4.setText(_translate("MainWindow", "База мелодій"))
        self.label_5.setText(_translate("MainWindow", "Відфільтрована база мелодій"))
        self.pushButton_2.setText(_translate("MainWindow", "Генерувати"))
        self.pushButton_3.setText(_translate("MainWindow", "Завантажити"))
        self.label_6.setText(_translate("MainWindow", "Початкова нота"))
        self.label_7.setText(_translate("MainWindow", "0"))

        self.comboBox.currentIndexChanged.connect(self.updateComboBox_2)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(500)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(100)
        self.horizontalSlider.valueChanged.connect(self.slide_func)
        self.pushButton.clicked.connect(self.filter_query)

    def updateComboBox_2(self, index):
        self.comboBox_2.clear()
        conn = connection_to_DB()
        cursor = conn.cursor()
        if index == 0:
            selected_item = 'Жанр'
        elif index == 1:
            selected_item = 'Виконавець'
        else:
            selected_item = 'Тип'
        cursor.execute(query_for_comboBox_2(selected_item))
        rows = cursor.fetchall()
        for row in rows:
            self.comboBox_2.addItem(row[0])
        conn.close()

    def slide_func(self, value):
        self.label_7.setText(str(value))

    def filter_query(self):
        table_ua = self.comboBox.currentText()
        value = self.comboBox_2.currentText()
        table_en = 'Artist'
        if table_ua == 'Виконавець':
            table_en = 'Artist'
        elif table_ua == 'Жанр':
            table_en = 'Genre'
        elif table_ua == 'Тип':
            table_en = 'Melodytype'
        query = '''SELECT Melody.*
        FROM Melody
        JOIN %s ON Melody.%sID = %s.%sID
        WHERE %s.%sName = '%s'
        '''
        ready_query = query % (table_en, table_en, table_en, table_en, table_en, table_en, value)
        print(ready_query)
        return ready_query


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
