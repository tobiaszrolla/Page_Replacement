from .create_ui import Ui_Create
from PySide6.QtWidgets import QWidget
from .runner_ui import Ui_runner
class Wig_Create(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Create()
        self.ui.setupUi(self)

class Wig_Runner(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_runner()
        self.ui.setupUi(self)

