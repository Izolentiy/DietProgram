from PyQt5 import QtWidgets, QtCore, QtGui

from screens.BaseScreen import BaseScreen


class Screen(BaseScreen):

    def init_content(self, layout):
        # Шрифт
        wel_font = QtGui.QFont()
        wel_font.setPointSize(20)

        # Приветственная надпись
        welcome = QtWidgets.QLabel()
        welcome.setObjectName('welcome')
        welcome.setFont(wel_font)
        welcome.setAlignment(QtCore.Qt.AlignCenter)
        welcome.setText('КАЛЬКУЛЯТОР КАЛОРИЙ')

        # Поле ввода для имени
        name_field = QtWidgets.QLineEdit()
        name_field.setObjectName('name_field')
        name_field.setPlaceholderText('Ваше имя')
        name_field.setAlignment(QtCore.Qt.AlignCenter)

        # Кнопка для ввода
        calculate = QtWidgets.QPushButton()
        calculate.setObjectName('calculate')
        calculate.setText('ПОСЧИТАТЬ')

        # Создание атрибутов данных для доступа к ним извне
        self.welcome = welcome
        self.name_field = name_field
        self.calculate = calculate

        # Добавление элементов на экран
        layout.addStretch(1)
        layout.addWidget(self.welcome)
        layout.addSpacing(50)
        layout.addWidget(self.name_field)
        layout.addSpacing(15)
        layout.addStretch(1)

        # Описания
        weight_tip = QtWidgets.QLabel()
        sex_tip = QtWidgets.QLabel()
        age_tip = QtWidgets.QLabel()
        height_tip = QtWidgets.QLabel()
        life_tip = QtWidgets.QLabel()

        weight_tip.setObjectName('weight_tip')
        sex_tip.setObjectName('sex_tip')
        age_tip.setObjectName('age_tip')
        height_tip.setObjectName('height_tip')
        life_tip.setObjectName('life_tip')

        weight_tip.setText('Ваш текущий вес: ')
        sex_tip.setText('Ваш пол: ')
        age_tip.setText('Ваш возраст: ')
        height_tip.setText('Ваш рост: ')
        life_tip.setText('Ваш образ жизни: ')

        # Поля ввода
        weight_field = QtWidgets.QLineEdit()
        sex_field = QtWidgets.QComboBox()
        age_field = QtWidgets.QLineEdit()
        height_field = QtWidgets.QLineEdit()
        life_field = QtWidgets.QComboBox()

        weight_field.setObjectName('weight_field')
        sex_field.setObjectName('sex_field')
        age_field.setObjectName('age_field')
        height_field.setObjectName('height_field')
        life_field.setObjectName('life_field')

        weight_field.setPlaceholderText('60 кг')
        weight_field.setValidator(QtGui.QIntValidator(40, 200))

        # Заполнение комбо-бокса с полом
        sex_field.addItem('М')
        sex_field.addItem('Ж')
        sex_field.addItem('Т')

        age_field.setPlaceholderText('20')
        age_field.setValidator(QtGui.QIntValidator(15, 100))

        height_field.setPlaceholderText('175 см')
        height_field.setValidator(QtGui.QIntValidator(150, 250))

        life_field.addItem('Мебель')
        life_field.addItem('Сидячая работа')
        life_field.addItem('Небольшие нагрузки')
        life_field.addItem('Физически тяжёлая работа')
        life_field.addItem('Грузчик 24/7')

        in_lt = QtWidgets.QGridLayout()  # макет для ввода
        out_lt = QtWidgets.QHBoxLayout()  # макет для вывода

        out_tip = QtWidgets.QLabel()
        result = QtWidgets.QLabel()

        out_tip.setObjectName('out_tip')
        result.setObjectName('result')

        out_tip.setText('Ваша норма в день:')
        result.setText('')

        # Добавление всех элементов на макеты

        self.weight_tip = weight_tip
        self.sex_tip = sex_tip
        self.age_tip = age_tip
        self.height_tip = height_tip
        self.life_tip = life_tip

        self.weight_field = weight_field
        self.sex_field = sex_field
        self.age_field = age_field
        self.height_field = height_field
        self.life_field = life_field

        self.out_tip = out_tip
        self.result = result

        in_lt.addWidget(self.weight_tip, 0, 0)
        in_lt.addWidget(self.weight_field, 0, 1)
        in_lt.addWidget(self.sex_tip, 1, 0)
        in_lt.addWidget(self.sex_field, 1, 1)
        in_lt.addWidget(self.age_tip, 2, 0)
        in_lt.addWidget(self.age_field, 2, 1)
        in_lt.addWidget(self.height_tip, 3, 0)
        in_lt.addWidget(self.height_field, 3, 1)
        in_lt.addWidget(self.life_tip, 4, 0)
        in_lt.addWidget(self.life_field, 4, 1)

        out_lt.addWidget(self.out_tip)
        out_lt.addWidget(self.result)

        layout.addStretch(1)
        layout.addLayout(in_lt)
        layout.addSpacing(50)
        layout.addWidget(self.calculate)
        layout.addSpacing(15)
        layout.addLayout(out_lt)
        layout.addStretch(1)
