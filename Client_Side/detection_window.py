from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np
import time
import requests
from detection import Detection

# Manages detection window, starts and stops detection thread
class DetectionWindow(QMainWindow):
	def __init__(self):
		super(DetectionWindow, self).__init__()	
		loadUi('UI/detection_window.ui', self)

		self.stop_detection_button.clicked.connect(self.close)

	# Created detection instance
	def create_detection_instance(self, token, location, receiver):
		self.detection = Detection(token, location, receiver)

	# Assigns detection output to the label in order to display detection output
	@pyqtSlot(QImage)
	def setImage(self, image):
		self.label_detection.setPixmap(QPixmap.fromImage(image))

	# Starts detection
	def start_detection(self):
		self.detection.changePixmap.connect(self.setImage)
		self.detection.start()
		self.show()

	# When closed
	def closeEvent(self, event):
		self.detection.running = False
		event.accept()

