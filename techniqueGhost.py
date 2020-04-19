from techniqueGhost_ui import *
from PyQt5.QtWidgets import *
import cv2

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	currentFolderName = ""
	currentFileName = ""

	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.serchVideoButton.clicked.connect(self.openFileNameDialog)
		self.searchOutputFolder.clicked.connect(self.openFolderNameDialog)
		self.acceptButton.clicked.connect(self.onAcceptButtonClick)

	def openFileNameDialog(self):
		options = QFileDialog.Options()
		options = QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self,"Buscar Video", "","All mp4 Files (*.mp4)", options=options)
		if fileName:
			self.set_currentFileName(fileName)
			self.entryVideoInput.setPlainText(fileName)

	def openFolderNameDialog(self):
		options = QFileDialog.Options()
		options = QFileDialog.DontUseNativeDialog
		folderName = QFileDialog.getExistingDirectory(self, "Seleccione carpeta de destino")
		if folderName:
			self.set_currentFolderName(folderName)
			self.entryImageOutput.setPlainText(folderName)

	def onAcceptButtonClick(self):
		self.processVideo()
		pass

	def processVideo(self):
		cap = cv2.VideoCapture(self.get_currentFileName())
		i=0
		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == False:
				break
			cv2.imwrite(self.get_currentFolderName() + '/'+str(i)+'.jpg',frame)
			i+=1
		cap.release()
		cv2.destroyAllWindows()




	def get_currentFolderName(self):
		return self._currentFolderName

	def set_currentFolderName(self, currentFolderName):
		self._currentFolderName = currentFolderName

	def get_currentFileName(self):
		return self._currentFileName

	def set_currentFileName(self, currentFileName):
		self._currentFileName = currentFileName
		

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()