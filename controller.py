from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from model import TemperatureModel


class TemperatureController(QMainWindow):

    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        ui_file = QFile("view.ui")
        ui_file.open(QFile.ReadOnly)

        self.ui = loader.load(ui_file, self)

        ui_file.close()

        self.model = TemperatureModel()

        self.ui.convertButton.clicked.connect(self.convert_temperature)
        self.ui.clearButton.clicked.connect(self.clear_fields)

        self.ui.show()

    def convert_temperature(self):
        fahrenheit_text = self.ui.temperatureInput.text()

        result = self.model.fahrenheit_to_celsius(fahrenheit_text)

        self.ui.resultLabel.setText(result)

    def clear_fields(self):
        self.ui.temperatureInput.clear()

        self.ui.resultLabel.setText("Result will appear here")