from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, \
    QFileDialog, QLabel, QWidget, QDial, QGridLayout, \
    QPushButton, QRadioButton, QScrollArea
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import sqlite3
import os
import datetime


# Класс интерфейса
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_name = 'presets_db.db'
        self.setupUi(self)
        self.names = []
        self.connect_to_db()
        self.id = 0

    def setupUi(self, MainWindow):
        # Часть интерфейса с кнопками
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(566, 555)
        # self.image.setPixmap(self.pixmap)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.scroll = QScrollArea(self.centralwidget)
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setGeometry(350, 450, 200, 100)

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(400, 200, 100, 20))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setText('Сохранить пресет')
        self.pushButton_15.clicked.connect(self.save)
        self.push_second_form = QtWidgets.QPushButton(self.centralwidget)
        self.push_second_form.setGeometry(QtCore.QRect(20, 450, 75, 71))
        self.push_second_form.clicked.connect(self.open_second_form)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_13.setGeometry(QtCore.QRect(340, 350, 100, 30))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(400, 150, 100, 20))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setText('Задать пресет')
        self.pushButton_14.clicked.connect(self.presets_update)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 70, 75, 71))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 70, 75, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 70, 75, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 150, 75, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 150, 75, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 150, 75, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 230, 75, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 230, 75, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 230, 75, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(140, 310, 75, 71))
        self.pushButton_0.setObjectName("pushButton_0")

        # Обработка нажатий на кнопки
        self.pushButton_1.clicked.connect(self.button_click_test)
        self.pushButton_2.clicked.connect(self.button_click_test)
        self.pushButton_3.clicked.connect(self.button_click_test)
        self.pushButton_4.clicked.connect(self.button_click_test)
        self.pushButton_5.clicked.connect(self.button_click_test)
        self.pushButton_6.clicked.connect(self.button_click_test)
        self.pushButton_7.clicked.connect(self.button_click_test)
        self.pushButton_8.clicked.connect(self.button_click_test)
        self.pushButton_9.clicked.connect(self.button_click_test)
        self.pushButton_0.clicked.connect(self.button_click_test)

        self.pushButton_13.clicked.connect(self.change_sounds)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 141, 71))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(340, 60, 100, 384))
        self.layoutWidget.setObjectName("layoutWidget")

        # Часть интерфейса с фильрацией кнопок
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.addlayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.addlayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout.addWidget(self.checkBox_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.pushButton_12.clicked.connect(self.cleaning_filter)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_14.setGeometry(QtCore.QRect(340, 380, 100, 30))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.connect_to_db)
        self.verticalLayout.addWidget(self.pushButton_13)
        self.verticalLayout.addWidget(self.pushButton_11)
        self.verticalLayout.addWidget(self.pushButton_14)

        self.table = QtWidgets.QTableWidget(self.centralwidget)  # QTableWidget()
        self.scroll_add()

        self.pushButton_11.clicked.connect(self.buttons_filter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyDRUMS"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_13.setText(_translate("MainWindow", "Новые звуки"))
        self.label.setText(_translate("MainWindow", "Выбери ненужные кнопки"))
        self.checkBox.setText(_translate("MainWindow", "1"))
        self.checkBox_2.setText(_translate("MainWindow", "2"))
        self.checkBox_3.setText(_translate("MainWindow", "3"))
        self.checkBox_4.setText(_translate("MainWindow", "4"))
        self.checkBox_5.setText(_translate("MainWindow", "5"))
        self.checkBox_6.setText(_translate("MainWindow", "6"))
        self.checkBox_7.setText(_translate("MainWindow", "7"))
        self.checkBox_8.setText(_translate("MainWindow", "8"))
        self.checkBox_9.setText(_translate("MainWindow", "9"))
        self.checkBox_10.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setText(_translate("MainWindow", "Очистить фильтр"))
        self.pushButton_11.setText(_translate("MainWindow", "Применить"))
        self.pushButton_14.setText(_translate("MainWindow", "Стандарт"))
        self.push_second_form.setText(_translate("MainWindow", "Ваше мнение"))

    # Функция реализующая функционал таблицы
    def scroll_add(self):
        con = sqlite3.connect('presets_db.db')
        cur = con.cursor()

        res = cur.execute(f"""SELECT * FROM presets ORDER BY id""").fetchall()

        self.scroll_elements = []

        self.table.setRowCount(1)
        self.table.setColumnCount(2)
        self.table.setColumnCount(len(res))
        self.table.setGeometry(QtCore.QRect(340, 430, 150, 100))

        for i in range(len(res)):
            btn = QPushButton(str(res[i][1]))
            btn.clicked.connect(self.use_preset)
            self.table.setCellWidget(0, i, btn)

            print(i)

        con.commit()
        con.close()
        print(self.scroll_elements)

    # Применение пресета
    def use_preset(self):
        self.cleaning_filter()
        self.new_perset = self.sender().text()
        print(self.new_perset)
        for i in self.default_preset:
            if i.text() not in self.sender().text():
                i.setDisabled(True)
                i.setChecked(True)

    # Изменение в бд
    def presets_update(self):
        con = sqlite3.connect('presets_db.db')
        cur = con.cursor()

        sting_of_preset = ''
        for i in self.default_preset:
            if not i.isChecked() and i.text() not in sting_of_preset:
                sting_of_preset += i.text()
        print(sting_of_preset)

        # tablestring = []
        # for i in range(len(self.table_of_pathes)):
        #     tablestring.append(self.table_of_pathes[i].get('sound_path'))
        #     cur.execute(f"""UPDATE presets SET sound{i} = '{tablestring[i]}'""").fetchall()
        # print(tablestring)

        cur.execute(f"""UPDATE presets SET preset = {sting_of_preset}""").fetchall()

        con.commit()
        con.close()

    # Сохранение в БД
    def save(self):
        # default preset
        con = sqlite3.connect('presets_db.db')
        cur = con.cursor()

        lastid = cur.execute(f"""SELECT id from presets ORDER BY id desc limit 1""").fetchall()
        lastid = lastid[0][0]
        sting_of_preset = ''
        for i in self.default_preset:
            if not i.isChecked() and i.text() not in sting_of_preset:
                sting_of_preset += i.text()

        cur.execute(f"""INSERT INTO presets(id, preset) VALUES('{lastid + 1}','{sting_of_preset}')""").fetchall()
        con.commit()
        con.close()
        self.scroll_add()

    # некоторое подключение к базе из которой берутяся пути
    # к дефолтному пресету. Сначала создается список объектов чекбоксов
    # (причем что интересно в неправильном виде он работает) затем
    # такой же только для кнопок, после чего происходит нехитрая запись в словарь
    def connect_to_db(self):
        # self.cleaning_filter()

        con = sqlite3.connect('presets_db.db')
        cur = con.cursor()
        result = cur.execute("""SELECT notes_path FROM pathes
                                                """).fetchall()

        self.default_preset = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_4,
                               self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_9,
                               self.checkBox_10]

        self.default_preset_buttons = [self.pushButton_0, self.pushButton_1, self.pushButton_2, self.pushButton_3
            , self.pushButton_4, self.pushButton_5, self.pushButton_6, self.pushButton_7
            , self.pushButton_8, self.pushButton_9]

        self.table_of_pathes = []
        for i in range(len(result)):
            k = result[i][0]
            k = str(os.getcwd()) + k
            self.table_of_pathes.append({'number': i, 'sound_path': k})
        con.commit()
        con.close()

        self.table_of_sounds = []

        for path in self.table_of_pathes:
            self.media = QtCore.QUrl.fromLocalFile(path.get('sound_path'))
            self.content = QtMultimedia.QMediaContent(self.media)
            self.table_of_sounds.append({'number': path.get('number'), 'sound': self.content})

        # print(len(self.table_of_sounds))

        for elem in self.default_preset:
            elem.setDisabled(False)
            self.buttons_filter()

        for i in range(10):
            self.default_preset[i].setChecked(True)
            self.default_preset_buttons[i].setDisabled(True)
        for i in range(len(self.table_of_sounds)):
            self.default_preset[i].setChecked(False)
            self.default_preset_buttons[i].setDisabled(False)
        self.buttons_filter()

    # Загрузка музыки)
    def load_sounds(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        # table of content
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    # Обнова звуков по факту
    def change_sounds(self):
        self.table_of_sounds = []
        for i in range(10):
            self.new_sound = \
                QFileDialog.getOpenFileName(self, f'Выбрать звук {i + 1}', '', 'Звук (*.mp3);;Звук (*.wav)')[0]
            self.media = QtCore.QUrl.fromLocalFile(self.new_sound)
            self.content = QtMultimedia.QMediaContent(self.media)
            self.table_of_sounds.append({'number': len(self.table_of_sounds), 'sound': self.content})

        # print(len(self.table_of_sounds))

    # Фильтр кнопок
    def buttons_filter(self):
        self.choice_dict = {self.checkBox: self.pushButton_1,
                            self.checkBox_2: self.pushButton_2,
                            self.checkBox_3: self.pushButton_3,
                            self.checkBox_4: self.pushButton_4,
                            self.checkBox_5: self.pushButton_5,
                            self.checkBox_6: self.pushButton_6,
                            self.checkBox_7: self.pushButton_7,
                            self.checkBox_8: self.pushButton_8,
                            self.checkBox_9: self.pushButton_9,
                            self.checkBox_10: self.pushButton_0}
        for i, j in self.choice_dict.items():
            if i.isChecked():
                i.setDisabled(True)
                j.setDisabled(True)
        self.pushButton_14.setDisabled(True)

    # рисование
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.stroke(qp)
        qp.end()

    def stroke(self, qp):
        qp.setBrush(QColor(25, 140, 250))
        qp.drawRect(0, 0, 566, 555)

    # Очистка фильтра
    def cleaning_filter(self):
        for i, j in self.choice_dict.items():
            if i.isChecked():
                i.setChecked(False)
                i.setDisabled(False)
                j.setDisabled(False)
        self.pushButton_14.setDisabled(False)

    # Обработка на кнопках
    # загружает из списка путей по индексу и воспроизводит аудиофайл
    def buttons_clicks(self):
        self.load_sounds(str(self.names[int(self.sender().text()) - 1]))
        self.player.play()

    # Тестовая функция которая трай-ексцептом пытается
    # воспроизвести звук беря текст из кнопки и данные из словаря
    def button_click_test(self):
        try:
            self.initiator = self.sender().text()
            print(self.initiator)
            self.player = QtMultimedia.QMediaPlayer()
            self.player.setMedia(self.table_of_sounds[int(self.initiator)].get('sound'))
            self.player.play()
        except IndexError:
            pass

    # Обработка клавиш осуществляемая с помощью словаря в котором записан объект Qt_Key как ключ,
    # и отрицательное значение результата проверки чекбокса
    def keyPressEvent(self, event):
        self.dict_of_buttons = {Qt.Key_0: not self.checkBox_10.isChecked(),
                                Qt.Key_1: not self.checkBox.isChecked(),
                                Qt.Key_2: not self.checkBox_2.isChecked(),
                                Qt.Key_3: not self.checkBox_3.isChecked(),
                                Qt.Key_4: not self.checkBox_4.isChecked(),
                                Qt.Key_5: not self.checkBox_5.isChecked(),
                                Qt.Key_6: not self.checkBox_6.isChecked(),
                                Qt.Key_7: not self.checkBox_7.isChecked(),
                                Qt.Key_8: not self.checkBox_8.isChecked(),
                                Qt.Key_9: not self.checkBox_9.isChecked()}
        for i, j in self.dict_of_buttons.items():
            if event.key() == i:
                if j:
                    self.player = QtMultimedia.QMediaPlayer()
                    self.player.setMedia(self.table_of_sounds[int(chr(i))].get('sound'))
                    self.player.play()

    # открытие второй формы
    def open_second_form(self):
        self.second_form = SecondForm(self, "Уровень респекта")
        self.second_form.show()

    # загрузка первоначального пресета кнопок
    def assets(self):
        con = sqlite3.connect('presets_db.db')
        cur = con.cursor()
        result = cur.execute("""SELECT preset FROM presets
                                    """).fetchall()
        con.commit()
        con.close()


# Вторая форма
class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 700, 600)
        self.setWindowTitle('Оцените пж)')
        layout = QGridLayout()
        self.lbl = QLabel(args[-1], self)
        self.setLayout(layout)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(0)
        self.dial.valueChanged.connect(self.sliding)
        self.btn = QPushButton(self)
        self.btn.setText('Вердикт')
        self.btn.resize(50, 20)
        self.btn.clicked.connect(self.write_verdict_to_bd)
        layout.addWidget(self.btn)
        layout.addWidget(self.dial)
        layout.addWidget(self.lbl)

    # Функция для объекта self.dial
    # которая меняет текст лейбла в зависимости от поворота диала.
    def sliding(self):
        self.lbl.setText(f'Сколько респекта выдаите за это?: {str(self.dial.value())}')

    # запись в базу данных значений диала
    def write_verdict_to_bd(self):
        self.date = str(datetime.datetime.now())
        con = sqlite3.connect('presets_db.db')
        # print(1)
        cur = con.cursor()
        # print(2)
        res = cur.execute(f"""INSERT INTO verdict VALUES({str(self.dial.value())}, '{self.date}')""")
        # print(3)
        con.commit()
        con.close()
        self.third_form = ThirdForm(self, "Я...")
        self.third_form.show()


# форма вердикта который берется из базы
class ThirdForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setWindowTitle('Я....')
        self.setFixedSize(232, 181)
        self.pixmap = QPixmap(QFileDialog.getOpenFileName(self, 'Выбрать картинку для вдохновения', '',
                                                          'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0])
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
