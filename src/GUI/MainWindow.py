from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtGui import QAction

from src.GUI.Runner import Runner
from src.GUI.Create import Create


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Page Replacement Simulator")
        self.resize(1000, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.run_widget = Runner()
        self.data_widget = Create()

        self.stack.addWidget(self.run_widget)
        self.stack.addWidget(self.data_widget)

        self.stack.setCurrentWidget(self.run_widget)

        menubar = self.menuBar()

        view_menu = menubar.addMenu("View")

        self.action_runner = QAction("Runner", self)
        self.action_creator = QAction("Creator", self)

        view_menu.addAction(self.action_runner)
        view_menu.addAction(self.action_creator)


        self.action_runner.triggered.connect(self.show_runner)
        self.action_creator.triggered.connect(self.show_creator)


    def show_creator(self):
        self.stack.setCurrentWidget(self.data_widget)

    def show_runner(self):
        self.stack.setCurrentWidget(self.run_widget)