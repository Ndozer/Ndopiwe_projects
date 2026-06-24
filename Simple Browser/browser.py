from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import *
import sys

class Browser(QMainWindow):
    def __init__(self, *args,**kwargs):
        super(Browser,self).__init__(*args,**kwargs)
        self.window = QWidget()
        self.window.setWindowTitle("The Ndops Browser")

        self.layout1 = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.search_btn = QPushButton("Search")
        self.search_btn.setMinimumHeight(30)
        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(30)
        self.forward_btn = QPushButton("Forward")
        self.forward_btn.setMinimumHeight(30)
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.search_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.clear_btn)

        self.browser = QWebEngineView()

        self.search_btn.clicked.connect(lambda:self.searching(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(lambda:self.browser.back())
        self.forward_btn.clicked.connect(lambda:self.browser.forward())
        self.clear_btn.clicked.connect(lambda:self.clear())

        self.layout1.addLayout(self.horizontal)
        self.layout1.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))
        self.window.setLayout(self.layout1)
        self.window.show()
    def searching(self,url):
        url = url.strip()
        if not url:
            return
        if "." in url or url.startswith("http://") or url.startswith("https://"):
            if not (url.startswith("http://") or url.startswith("https://")):
                url1 = "https://" + url
            else:
                url1 = url
        else:
            search_query = url.replace(" ", "+")
            url1 = f"https://www.google.com/search?q={search_query}"
        self.url_bar.setText(url1)
        self.browser.setUrl(QUrl(url1))
    def clear(self):
        self.url_bar.setText("")
app = QApplication(sys.argv)
window = Browser()
app.exec_()