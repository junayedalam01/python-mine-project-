# import sys
# from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout,QPushButton,QLabel,QGroupBox,QGridLayout

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Editable Text Box')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         group_box = QGroupBox("Text Box")
#         line_edit = QLineEdit()
#         group_box.setLayout(QVBoxLayout())
#         group_box.setLayout(QVBoxLayout())
#         group_box.setLayout(group_box_layout := QGridLayout())
#         group_box_layout.addWidget(line_edit, 0, 0)
#         layout.addWidget(group_box)

#         button = QPushButton('Enter')
#         button.clicked.connect(lambda: print(line_edit.text()))
#         self.hello_message = QLabel("Hello World",self)
#         layout.addWidget(button)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())


# import sys
# from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout,QPushButton,QLabel

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Editable Text Box')

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         line_edit = QLineEdit()
#         line_edit.setContentsMargins(10, 10, 10, 10) # Add padding
#         layout.addWidget(line_edit)

#         button = QPushButton('Enter')
#         button.clicked.connect(lambda: print(f" Hello : {line_edit.text()}"))
#         self.hello_message = QLabel("Hello World",self)
#         layout.addWidget(button)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())
