# Simple Web browser made in python using PyQt5
# pip install PyQt5
# pip install PyQtWebEngine
# @author pettis1996 on github

# importing the important PyQt5 modules that i will use in this program
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


# Creating a Window for the browser
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # back button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # refresh current page - button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # go to the home page - button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    # function used from home button to get to home url
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    # function used to navigate to a specific url in the url bar
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # function used to update the url with the new page's url after loading it
    def update_url(self, q):
        self.url_bar.setText(q.toString())


# app creation and display
app = QApplication(sys.argv)
QApplication.setApplicationName('@author Pettis1996')
window = MainWindow()
app.exec_()
