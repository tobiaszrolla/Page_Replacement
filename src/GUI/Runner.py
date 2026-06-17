from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from src.GUI.UI.MyWiggets import Ui_runner
from src.data.load_data import load_data
from src.engin.Engin import Engine
from src.engin.Logger import Logger
from src.models.PageTable import PageTable
from src.algorithms.Export import FIFO, LFU, LRU, MFU


class Runner(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_runner()
        self.ui.setupUi(self)

        self.trace = None
        self.meta = None
        self.context_size = None
        self.engine = None

        self.ui.PushButton_SelectFile.clicked.connect(self.load_data)
        self.ui.PushButton_Run.clicked.connect(self.run)
        self.ui.PushButton_Save.clicked.connect(self.save)

    def load_data(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select JSON file",
            "",
            "JSON Files (*.json)"
        )

        if not file_path:
            return

        try:
            self.meta, self.trace = load_data(file_path)

            self.context_size = self.meta.get("context_size")

            QMessageBox.information(
                self,
                "OK",
                "Loaded data"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


    def run(self):
        if self.trace is None:
            QMessageBox.warning(self, "Error", "No data loaded")
            return

        if self.context_size is None:
            QMessageBox.warning(self, "Error", "No context size in meta")
            return

        algorithm_choice = self.ui.comboBox.currentText()
        max_time = self.ui.spinBox.value()
        memory_size = self.ui.spinBox_MemorySize.value()
        algorithms = {
            "FIFO": FIFO,
            "LRU": LRU,
            "LFU": LFU,
            "MFU": MFU,
        }

        algorithm_class = algorithms.get(algorithm_choice)

        if not algorithm_class:
            QMessageBox.critical(self, "Error", "Unknown algorithm")
            return

        algorithm = algorithm_class()
        self.engine = Engine(algorithm,
                             self.trace,
                             max_time,
                             memory_size)
        self.engine.run()
        QMessageBox.information(self, "INF", "Finnish running")

    def save(self):
        if self.engine is None:
            QMessageBox.warning(self, "Error", "Run simulation first")
            return

        logger = self.engine.logger

        if logger is None:
            QMessageBox.warning(self, "Error", "No logger available")
            return

        try:

            raw_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save raw logs",
                "result_raw.json",
                "JSON Files (*.json)"
            )

            if not raw_path:
                return

            metrics_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save metrics",
                "result_metrics.json",
                "JSON Files (*.json)"
            )

            if not metrics_path:
                return

            logger.saveRawResults(raw_path)

            metrics = self.engine.get_metrics()

            if metrics is None:
                metrics = {"warning": "No metrics generated"}

            logger.saveMetrics(metrics_path, metrics)

            QMessageBox.information(
                self,
                "OK",
                "Files saved successfully"
            )

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))