from PyQt5 import QtWidgets


class BaseScreen(QtWidgets.QWidget):

    """Базовый экран, описывает общие черты всех экранов для избежнаия дубликации кода"""

    # Метод для установки виджета(экрана) в качестве центрального внутрь главного окна
    def show_ui(self, main_window):
        self.widget = QtWidgets.QWidget(self)
        self.widget.screen = self  # Костыль из-за, я полагаю, бага
        if self.widget.layout() is None:
            self.init_base()
        main_window.setCentralWidget(self.widget)

    # В этом методе описаны общие черты
    def init_base(self):
        # main_vlt - main layout вертикальный макет
        main_vlt = QtWidgets.QVBoxLayout()
        main_vlt.setContentsMargins(0, 0, 0, 0)
        main_vlt.setSpacing(0)
        # main_hlt - main layout горизонтальный макет
        main_hlt = QtWidgets.QHBoxLayout()
        main_hlt.setContentsMargins(0, 0, 0, 0)
        main_hlt.setSpacing(0)

        content_lt = QtWidgets.QVBoxLayout()  # создание основного макета
        self.init_content(content_lt)  # заполнение основного макета

        # Добавление отступов
        main_vlt.addSpacing(50)  # верхний отступ
        main_hlt.addSpacing(50)  # левый отступ
        main_vlt.addLayout(main_hlt)  # добавление горизонтального макета в вертикальный
        main_hlt.addLayout(content_lt)  # добавление основного макета в горизонтальный
        main_hlt.addSpacing(50)  # правый отступ
        main_vlt.addSpacing(50)  # нижний отступ

        self.widget.setLayout(main_vlt)  # установка вертикального макета в экран

    # Этот метод будет по своему реализовываться у каждого дочернего класса
    def init_content(self, layout):
        pass
