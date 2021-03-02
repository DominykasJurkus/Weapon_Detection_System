from PyQt5.QtWidgets import QApplication
import sys
from login_window import LoginWindow

# Starting the application
app = QApplication(sys.argv)
mainwindow = LoginWindow()

# Exiting
try:
	sys.exit(app.exec_())
except: 
	print("Exiting")