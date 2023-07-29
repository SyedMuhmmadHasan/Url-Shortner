import sys
import pyshorteners
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class URLShortenerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('URL Shortener')
        self.setGeometry(200, 200, 400, 100)

        self.url_label = QLabel('Enter URL:')
        self.url_input = QLineEdit()
        self.shortened_label = QLabel('Shortened URL:')
        self.shortened_output = QLineEdit()
        self.shortened_output.setReadOnly(True)

        self.shorten_button = QPushButton('Shorten', clicked=self.shorten_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.shorten_button)
        layout.addWidget(self.shortened_label)
        layout.addWidget(self.shortened_output)

        self.setLayout(layout)

    def shorten_url(self):
        long_url = self.url_input.text()
        if not long_url:
            self.shortened_output.setText('Please enter a valid URL.')
            return

        s = pyshorteners.Shortener()
        try:
            short_url = s.tinyurl.short(long_url)
            self.shortened_output.setText(short_url)
        except pyshorteners.exceptions.ShorteningErrorException:
            self.shortened_output.setText('Error: Unable to shorten the URL.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = URLShortenerApp()
    window.show()
    sys.exit(app.exec_())
