import sys
import urllib.request, json
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from Form import Ui_Dialog
Movie = ""
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.btnSearch.clicked.connect(self.search)
    def search(self):
        Movie = self.ui.txtSearch.toPlainText()
        Movie = Movie.replace(" ", "+")
        try:
            with urllib.request.urlopen("http://www.omdbapi.com/?apikey=b00d4724&t={}&type=movie".format(Movie)) as url:
                data = json.loads(url.read().decode())
                self.ui.lblPlot.setText(data["Plot"])
                self.ui.lblRated.setText(data["Rated"])
                self.ui.lblTitle.setText(data["Title"])
                self.ui.lblRuntime.setText(data["Runtime"])
                self.ui.lblRelease.setText(data["Released"])
                self.ui.Genres.setText(data["Genre"])
                urllib.request.urlretrieve(data["Poster"], data["Title"] + ".jpg")
                pixmap = QPixmap(data["Title"] + ".jpg")
                self.ui.lblPoster.setPixmap(pixmap)

        except:
            QMessageBox.warning(self,"Movie Not Found","Movie doesn't exist, please check spelling!",QMessageBox.Ok)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

