from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from src.GUI.UI.MyWiggets import Ui_Create
from src.data.generateData import generate_data
from src.data.save_data import save_data


class Create(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Create()
        self.ui.setupUi(self)
        self.data = None

        self.ui.PushButton_CreateAndSave.clicked.connect(
            self.createAndSave
        )

    def create(self):
        context_change_prob = self.ui.SpinBox_ContextChangeProb.value()
        length = self.ui.SpinBox.value()
        context_size = self.ui.SpinBox_ContextSize.value()
        processes = self.ui.SpinBox_ContextSize_2.value()
        pages = self.ui.SpinBox_PageNumber.value()
        working_set_size = self.ui.SpinBox_WorkingSetSize.value()
        pages_reuse = self.ui.SpinBox_PageReuseProbability.value()

        self.data = generate_data(context_switch_probability=context_change_prob,
                                write_probability= 0.2,
                                n_processes= processes,
                                n_pages=pages,
                                length=length,
                                context_size=context_size,
                                page_reuse=pages_reuse,
                                working_set_size=working_set_size)
    
    def save(self):
        context_size = self.ui.SpinBox_ContextSize.value()
        processes = self.ui.SpinBox_ContextSize_2.value()
        pages = self.ui.SpinBox_PageNumber.value()
        if self.data is None:
            QMessageBox.warning(self, "Err", "No data to save")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(self,
                                                "Saving taksks",
                                                "trace.json",
                                                "JSON Files (*.json)")
        
        if not file_path:
            QMessageBox.warning(self, "Err", "No file path")
            return
        
        QMessageBox.information(self, "Inf", "Saving")
        save_data(self.data, file_path, processes, pages, context_size)

    def createAndSave(self):
        self.create()
        self.save()
        