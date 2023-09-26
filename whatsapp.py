import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QTextEdit, QWidget)

# Create the main window
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("WhatsApp")
window.setWindowIcon(QIcon("icon.png"))

# Create a widget for the main window
widget = QWidget()
layout = QGridLayout()
widget.setLayout(layout)

# Create the labels and text boxes
phone_number_label = QLabel("Phone number:")
phone_number_text_box = QLineEdit()
layout.addWidget(phone_number_label, 0, 0)
layout.addWidget(phone_number_text_box, 0, 1)

message_label = QLabel("Message:")
message_text_box = QTextEdit()
layout.addWidget(message_label, 1, 0)
layout.addWidget(message_text_box, 1, 1)

# Create the send button
send_button = QPushButton("Send")
layout.addWidget(send_button, 2, 1)

# Function to handle the send button being clicked

def send_clicked():
    phone_number = phone_number_text_box.text()
    message = message_text_box.toPlainText()
    # Send the message using your preferred method (e.g. Selenium, Puppeteer, etc.)


# Connect the send button to the send_clicked function
send_button.clicked.connect(send_clicked)

# Display the main window
window.setCentralWidget(widget)
window.show()
sys.exit(app.exec_())
