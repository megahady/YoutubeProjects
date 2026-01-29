from PyQt5 import QtWidgets, uic
import sys


class Notepad(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("notepad.ui", self)

        self.current_path = None

        # Button connections
        self.btn_Open.clicked.connect(self.load_text_file)
        self.btn_Clear.clicked.connect(self.clear_text)
        self.btn_Save.clicked.connect(self.save)
        self.btn_SaveAs.clicked.connect(self.save_as)

        # Zoom buttons (make sure these exist in your .ui)
        self.btn_Zoomin.clicked.connect(self.zoom_in)
        self.btn_Zoomout.clicked.connect(self.zoom_out)

    # ================= TEXT ACTIONS =================

    def clear_text(self):
        self.textEdit.clear()

    def zoom_in(self):
        self.textEdit.zoomIn(1)

    def zoom_out(self):
        self.textEdit.zoomOut(1)

    # ================= FILE ACTIONS =================

    def load_text_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Text File", "", "Text Files (*.txt)"
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.textEdit.setPlainText(f.read())
                self.current_path = path
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def save(self):
        if not self.current_path:
            self.save_as()
            return

        try:
            with open(self.current_path, "w", encoding="utf-8") as f:
                f.write(self.textEdit.toPlainText())
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def save_as(self):
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save Text File As", "", "Text Files (*.txt)"
        )
        if path:
            self.current_path = path
            self.save()


# ================= STANDALONE TEST =================

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Notepad()
    window.setWindowTitle("Notepad")
    window.resize(600, 400)
    window.show()

    sys.exit(app.exec_())
