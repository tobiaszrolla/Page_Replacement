import sys
from PySide6.QtWidgets import QApplication

from src.GUI.MainWindow import MainWindow  # <- upewnij się że ścieżka pasuje


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()