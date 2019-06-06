import sys
import urllib.request, json

from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from Form import Ui_Dialog
from FirstForm import Ui_MainForm
from tvform import Ui_MainWindow
from EpisodeForm import Ui_EpisodeInfoForm

class MovieForm(QDialog):
    def __init__(self):
        super(MovieForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
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
        except:
                QMessageBox.warning(self, "Movie Not Found", "Movie doesn't exist, please check spelling!", QMessageBox.Ok)
        try:
                print(data["Poster"])
                urllib.request.urlretrieve(data["Poster"], data["Title"] + ".jpg")

                pixmap = QPixmap(data["Title"] + ".jpg")
                self.ui.lblPoster.setPixmap(pixmap)
        except:
            QMessageBox.warning(self, "Poster not found!", "Poster not available ",
                                QMessageBox.Ok)






class FirstWindow(QDialog):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self.ui.btnMovie.clicked.connect(self.Movie)
        self.ui.btnTv.clicked.connect(self.TV)
    def Movie(self):
        self.hide()
        ui.show()
    def TV(self):
        self.hide()
        TvForm.show()


class TvWindow(QMainWindow):
    def __init__(self):
        super(TvWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.Search)
        self.ui.btnGo.clicked.connect(self.Go)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.actionExit.setShortcut('Ctrl+Q')
        self.ui.actionGo_Back.triggered.connect(self.GoBack)
        self.ui.btnExtra.clicked.connect(self.ExtraInfo)

    def exit(self):
        quit()
    def GoBack(self):
        self.hide()
        MainForm.show()

    def Search(self):
        global season
        global TV
        TV = self.ui.txtSearch.toPlainText()
        TV = TV.replace(" ", "+")
        self.ui.lstEpi.clear()
        try:
            with urllib.request.urlopen("http://www.omdbapi.com/?apikey=b00d4724&t={}&type=series".format(TV)) as url:
                data = json.loads(url.read().decode())
                self.ui.lblTitle.setText(data["Title"])
                urllib.request.urlretrieve(data["Poster"], data["Title"] + ".jpg")
                pixmap = QPixmap(data["Title"] + ".jpg")
                self.ui.lblPoster.setPixmap(pixmap)
                self.ui.lblPoster.setScaledContents(True)
                for i in range(1, int(data["totalSeasons"]) + 1):
                    self.ui.lstEpi.addItem("Season " + str(i))
        except:
            QMessageBox.warning(self, "TV Series Not Found", "TV show doesn't exist, please check spelling!", QMessageBox.Ok)
    def Go(self):
        try:
            season = self.ui.lstEpi.currentItem().text()
            season = season.split(" ")[-1]
        except:
            QMessageBox.warning(self, "TV Series Not Found", "No Season/Episode selected!", QMessageBox.Ok)
        self.ui.lstEpi.clear()
        try:

            with urllib.request.urlopen("http://www.omdbapi.com/?apikey=b00d4724&t={}&season={}&type=series".format(TV,season)) as url:
                data = json.loads(url.read().decode())
                Episodes = data["Episodes"]
                for idx,i in enumerate(Episodes):
                    self.ui.lstEpi.addItem("Episode {} ".format(idx + 1) + i.get("Title"))
        except:
            QMessageBox.warning(self, "TV Series Not Found", "No Season/Episode selected!", QMessageBox.Ok)

    def ExtraInfo(self):
        Episodeform.show()

class EpisodeWindow(QMainWindow):
    def __init__(self):
        super(EpisodeWindow, self).__init__()
        self.ui = Ui_EpisodeInfoForm()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MovieForm()
    MainForm = FirstWindow()
    TvForm = TvWindow()
    Episodeform = EpisodeWindow()
    MainForm.show()
    sys.exit(app.exec_())

