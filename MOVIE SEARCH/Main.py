import urllib.request, json, sys
from MovieForm import Ui_MovieWindow
from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox,QMainWindow
from PyQt5.QtGui import QPixmap,QImage,QPalette,QBrush
from PyQt5.QtCore import QSize
from Search import Ui_SearchForm
from FirstForm import Ui_MainForm
from tvform import Ui_MainWindow
from EpisodeForm import Ui_EpisodeInfoForm
from watchlist import Ui_Dialog


class SearchForm(QDialog):
    def __init__(self):
        super(SearchForm, self).__init__()
        self.ui = Ui_SearchForm()
        self.ui.setupUi(self)
        self.ui.btnSearch.clicked.connect(self.Search)
        self.ui.btnGoback.clicked.connect(self.GoBack)
    def Search(self):
        global Movie
        Movie = self.ui.txtSearch.toPlainText()
        Movie = Movie.replace(" ", "+")
        with urllib.request.urlopen("http://www.omdbapi.com/?apikey=b00d4724&t={}&type=movie".format(Movie)) as url:
            data = json.loads(url.read().decode())
            if data["Response"] == "False":
                QMessageBox.warning(self, "Movie Not Found", "Movie doesn't exist, please check spelling!", QMessageBox.Ok)
            else:
                 MovieWindow.ui.lblPlot.setText(data["Plot"])
                 MovieWindow.ui.lblRated.setText(data["Rated"])
                 MovieWindow.ui.lblTitle.setText(data["Title"])
                 MovieWindow.ui.lblRuntime.setText(data["Runtime"])
                 MovieWindow.ui.lblReleased.setText(data["Released"])
                 MovieWindow.ui.lblGenres.setText(data["Genre"])
                 MovieWindow.ui.lblDirectors.setText(data["Director"])
                 try:
                     urllib.request.urlretrieve(data["Poster"], data["Title"] + ".jpg")
                     pixmap = QPixmap(data["Title"] + ".jpg")
                     MovieWindow.ui.lblPoster.setPixmap(pixmap)
                     MovieWindow.ui.lblPoster.setScaledContents(True)
                 except:
                     QMessageBox.warning(self, "Poster Not Found", "No Poster Available", QMessageBox.Ok)
                 self.hide()
                 MovieWindow.show()
    def GoBack(self):
        self.hide()
        MainForm.show()


class MovieForm(QMainWindow):
    def __init__(self):
        super(MovieForm, self).__init__()
        self.ui = Ui_MovieWindow()
        self.ui.setupUi(self)
        self.ui.actionSearch.triggered.connect(self.Search)
        self.ui.actionExit_Application.triggered.connect(self.exit)
        self.ui.actionView_WatchList.triggered.connect(self.watchlist)
        self.ui.actionAdd_to_Watchlist.triggered.connect(self.Add)
    def Search(self):
        self.hide()
        MovieSearch.show()

    def exit(self):
        quit()
    def watchlist(self):
        with open("Watchlist.txt",'r')as f:
                for line in f:
                    WatchListForm.ui.lstWatchList.addItem(line)
        self.hide()
        WatchListForm.show()
    def Add(self):
        with open("Watchlist.txt",'a')as f:
            f.write(self.ui.lblTitle.text())
class FirstWindow(QDialog):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self.ui.btnMovie.clicked.connect(self.Movie)
        self.ui.btnTv.clicked.connect(self.TV)
        oImage = QImage("download.jpg")
        sImage = oImage.scaled(QSize(588, 436))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)
    def Movie(self):
        self.hide()
        MovieSearch.show()

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
        oImage = QImage("download1.jpg")
        sImage = oImage.scaled(QSize(800, 646))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = WindowRole
        self.setPalette(palette)
    def exit(self):
        quit()

    def GoBack(self):
        self.hide()
        MainForm.show()

    def Search(self):

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
        global season
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
        Episode = self.ui.lstEpi.currentItem().text()
        Episode = " ".join(Episode.split(" ", 2)[:2])
        Episode = Episode.split(" ")[-1]
        with urllib.request.urlopen("http://www.omdbapi.com/?apikey=b00d4724&t={}&season={}&episode={}&type=series".format(TV,season,Episode)) as url:
            data = json.loads(url.read().decode())
            Episodeform.ui.lblTitle.setText(data["Title"])
            Episodeform.ui.lblPlot.setText(data["Plot"])
            Episodeform.ui.lblRating.setText(data["imdbRating"])
            Episodeform.ui.lblRating_2.setText(data["Actors"])
            Episodeform.ui.lblReleased.setText(data["Released"])
class EpisodeWindow(QMainWindow):
    def __init__(self):
        super(EpisodeWindow, self).__init__()
        self.ui = Ui_EpisodeInfoForm()
        self.ui.setupUi(self)

class WatchList(QDialog):
    def __init__(self):
        super(WatchList, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnWatch.clicked.connect(self.Watched)
        self.ui.btnGoBack.clicked.connect(self.GoBack)
    def Watched(self):
        with open("Watchlist.txt",'r')as f:
            filedata = f.read()
        filedata = filedata.replace(self.ui.lstWatchList.currentItem().text(), '')
        with open("Watchlist.txt",'w')as f:
            f.write(filedata)
        self.ui.lstWatchList.takeItem(self.ui.lstWatchList.currentRow())
    def GoBack(self):
        self.ui.lstWatchList.clear()
        self.hide()
        MovieWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MovieWindow = MovieForm()
    MovieSearch = SearchForm()
    MainForm = FirstWindow()
    TvForm = TvWindow()
    Episodeform = EpisodeWindow()
    WatchListForm = WatchList()
    MainForm.show()
    sys.exit(app.exec_())

