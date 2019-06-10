import urllib.request, json, sys
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from Search import Ui_SearchForm
class SearchForm(QDialog):
    def __init__(self):
        super(SearchForm, self).__init__()
        self.ui = Ui_SearchForm()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.Search)
        self.show()
    def Search(self):
        while True:
                QMessageBox.warning(self, "Movie Not Found", "Movie doesn't exist, please check spelling!", QMessageBox.Ok)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MovieSearch = SearchForm()
    sys.exit(app.exec_())
