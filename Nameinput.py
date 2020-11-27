import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic

formWaiting = uic.loadUiType("waiting.ui")[0]

class NameInput(QDialog, formWaiting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.goGameButton.clicked.connect(self.goGame)

    def goGame(self):
        self.accept()

    def showModel(self):
        return super().exec_()