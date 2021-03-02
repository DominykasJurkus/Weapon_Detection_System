from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import webbrowser
import requests
import json
from settings_window import SettingsWindow

# LoginWindow class that manages login and opening the setting window
class LoginWindow(QMainWindow):
	def __init__(self):
		super(LoginWindow, self).__init__()
		loadUi('UI/login_window.ui', self)

		self.register_button.clicked.connect(self.go_to_register_page)
		self.login_button.clicked.connect(self.login)

		self.popup = QMessageBox()
		self.popup.setWindowTitle("Failed")

		self.show()

	# Open registration page
	def go_to_register_page(self):
		webbrowser.open('http://127.0.0.1:8000/register/')

	# Login function that manages the token authentication
	def login(self):
		try:
			url = 'http://127.0.0.1:8000/api/get_auth_token/'
			response = requests.post(url, data={'username': self.username_input.text(),'password': self.password_input.text()})
			json_response = json.loads(response.text)

			# HTTP 200
			if response.ok:
				# Open settings window
				self.open_settings_window(json_response['token'])
			# Bad response
			else:
				# Show error
				self.popup.setText("Username or Password is not correct")
				self.popup.exec_()
		except:
			# Unable to access server
			self.popup.setText("Unable to access server")
			self.popup.exec_()
	
	# Opens settings window, passes the received token and closes login window
	def open_settings_window(self, token):
		self.settings_window = SettingsWindow(token)
		self.settings_window.displayInfo()
		self.close()
