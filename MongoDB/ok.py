import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel('What is your name?')
        self.line_edit = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
