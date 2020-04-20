from techniqueGhost_ui import *
from PyQt5.QtWidgets import *
import cv2

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

	currentFolderName = ""
	currentFileName = ""
	frameList = []
	ghostRatio = 4

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
		self.processFrames()
		self.createGhost()
		self.logEventinView('listo')
		

	def createGhost(self):
		innerFrameList = self.get_frameList()
		imgResult = innerFrameList[0]
		i = 1
		for i in range(i, len(innerFrameList)):
			currentImg = innerFrameList[i]
			imgResult = cv2.addWeighted(imgResult,0.7,currentImg,0.3,0)
			pass
		cv2.imwrite(self.get_currentFolderName() + '/ghost.jpg',imgResult)


	def processFrames(self):
		self.logEventinView('procesando video')
		cap = cv2.VideoCapture(self.get_currentFileName())
		innerFrameList = []
		i=0
		length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		ratio = self.get_ghostRatio() if self.ghostFactorEntry.text() is not None and self.ghostFactorEntry.text() != "" else self.get_ghostRatio()
		print(ratio)
		step = length // self.get_ghostRatio()
		currentStep = step

		while(cap.isOpened()):
			ret, frame = cap.read()
			if ret == False:
				break
			if i == currentStep or i == length:
				currentStep += step
				innerFrameList.append(frame)
			i+=1
		cap.release()
		cv2.destroyAllWindows()
		self.set_frameList(innerFrameList)

	def logEventinView(self, logEvent):
		logText = self.logEventText.toPlainText()
		logText = logText + '\n' + logEvent
		self.logEventText.setPlainText(logText)

	def get_currentFolderName(self):
		return self.currentFolderName

	def set_currentFolderName(self, currentFolderName):
		self.currentFolderName = currentFolderName

	def get_currentFileName(self):
		return self.currentFileName

	def set_currentFileName(self, currentFileName):
		self.currentFileName = currentFileName

	def get_frameList(self):
		return self.frameList

	def set_frameList(self, frameList):
		self.frameList = frameList

	def get_ghostRatio(self):
		return self.ghostRatio

	def set_ghostRatio(self, ghostRatio):
		self.ghostRatio = ghostRatio
		

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()