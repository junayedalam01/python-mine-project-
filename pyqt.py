import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QEn
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.setGeometry(100, 100, 320, 200) # x, y, width, height

        # Create a label and center the text
        self.hello_message = QLabel("<h1>Hello, World!</h1>", self)

        self.hello_message =QLabel("HELLO WORLD",self)
        self.hello_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hello_message.setGeometry(0, 0, 320, 200) # Position and size within the window

def main():
    app = QApplication(sys.argv) # Create the application instance
    window = MainWindow()        # Create the main window object
    window.show()                # Display the window
    sys.exit(app.exec())         # Start the event loop and ensure clean exit

if __name__ == "__main__":
    main()
