import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'main.ui'))

class MainDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        lista = ['2', '3', '5']
        self.BaseStation.addItems(lista)
        self.Program.addItems(lista)
        self.Parametr.addItems(lista)
        self.Year.addItems(lista)

