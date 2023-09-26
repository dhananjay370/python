import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Smart Calculator')

        layout = QGridLayout(self)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setObjectName('display')
        layout.addWidget(self.display, 0, 0, 1, 4)

        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C' # Clear button
        ]

        for i, label in enumerate(button_labels):
            button = QPushButton(label)
            button.setObjectName('button')
            layout.addWidget(button, i//4 + 1, i%4)
            if label == 'C':
                button.clicked.connect(self.clearDisplay)
            else:
                button.clicked.connect(self.buttonClicked)

        self.setStyleSheet('''
            #display {
                font-size: 30px;
                padding: 10px;
                background-color: white;
                border: 1px solid black;
                border-radius: 5px;
                margin-bottom: 10px;
            }

            #button {
                font-size: 20px;
                padding: 10px;
                background-color: #f2f2f2;
                border: 1px solid black;
                border-radius: 5px;
            }

            #button:hover {
                background-color: #e6e6e6;
            }

            #button:pressed {
                background-color: #d9d9d9;
            }
        ''')

        self.show()

    def buttonClicked(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error'
            self.display.setText(result)
        else:
            self.display.setText(self.display.text() + text)

    def clearDisplay(self):
        self.display.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
