from PyQt5 import QtWidgets

from screens.Screen import Screen


class ScreenController(QtWidgets.QMainWindow):

    """Главное окно, оно управляет всеми экранами и вспомогательными объектами"""

    # Конструктор
    def __init__(self):
        super().__init__()

        # Установка параметрова главного окна
        self.setWindowTitle('Программа для диет')
        self.resize(500, 250)

        # Создание экранов
        self.screen = Screen()

        self.set_screen(self.screen)  # установка экрана
        self.show()  # метод для отображения главного окна

    # Манипуляция с экранами
    def set_screen(self, screen):
        screen.show_ui(self)
        screen.calculate.clicked.connect(self.button_processor)

    # Обработка нажатий
    def button_processor(self):
        if self.screen.weight_field.text() is '' or self.screen.height_field.text() is '' or self.screen.age_field.text() is '':
            print('Enter data')
        else:
            sex = self.screen.sex_field.currentText()
            height = float(self.screen.height_field.text())
            age = float(self.screen.age_field.text())
            weight = float(self.screen.weight_field.text())

            self.calculate(height, weight, age, sex)

    def calculate(self, height, weight, age, sex):
        if sex == 'М':
            result = 66 + (13.7 * weight) + (5 * height) - (6.76 * age)
        elif sex == 'Ж':
            result = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            result = '???'
        self.screen.result.setText(str(result) + ' ккал')
