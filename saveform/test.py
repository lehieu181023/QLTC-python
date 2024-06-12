import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt5 import QtWidgets

from t import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")

        layout = QVBoxLayout()

        # Tạo các màn hình con và thêm vào stacked widget
        screen1 = Screen1()
        screen2 = Screen2()

        self.stacked_widget.addWidget(screen1)
        self.stacked_widget.addWidget(screen2)
        
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        self.stacked_widget.addWidget(Form)

        # Thêm nút để chuyển đổi giữa các màn hình
        button1 = QPushButton("Screen 1")
        button1.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(screen1))

        button2 = QPushButton("Screen 2")
        button2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(screen2))
        
        button3 = QPushButton("form")
        button3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(Form))

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)


class Screen1(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        label = QLabel("Screen 1")
        layout.addWidget(label)

        self.setLayout(layout)


class Screen2(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        label = QLabel("Screen 2")
        layout.addWidget(label)

        button = QPushButton("Test Button")
        button.clicked.connect(self.on_test_button_clicked)
        layout.addWidget(button)

        self.setLayout(layout)

    def on_test_button_clicked(self):
        print("test")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
