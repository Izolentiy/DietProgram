from PyQt5 import QtWidgets

from screens.InOutScreen import InOutScreen
from screens.WelcomeScreen import WelcomeScreen


class ScreenController(QtWidgets.QMainWindow):

    """Главное окно, оно управляет всеми экранами и вспомогательными объектами"""

    # Конструктор
    def __init__(self):
        super().__init__()

        # Установка параметрова главного окна
        self.setWindowTitle('Программа для диет')
        self.resize(500, 250)

        # Создание экранов
        welcomeScreen = WelcomeScreen()
        inoutScreen = InOutScreen()

        self.set_screen(welcomeScreen)  # установка приветственного экрана
        self.show()  # метод для отображения главного окна

    # Манипуляция с экранами
    def set_screen(self, screen):
        screen.show_ui(self)

    # Обработка нажатий
    def button_processor(self):
        pass
