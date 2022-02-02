# Created by: Yash Dhingra

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Musifre(object):
    global a 
    a=0
    def download_music(self):
        print("clicked")
        self.status.setText("Download Status: Searching...")
        trackname=self.track_name.text()
        import urllib.request
        import re 
        import time
        from pytube import YouTube
        import os

        keyword=trackname
        keyword=keyword.replace(" ","+")

        url="https://www.youtube.com/results?search_query="+keyword

        html = urllib.request.urlopen(url)
        self.status.setText("Download Status: Search Complete.")
        time.sleep(1)

        video_ids=re.findall(r"watch\?v=(\S{11})", html.read().decode())

        #Downloading Inititaion

        yt=YouTube("https://www.youtube.com/watch?v="+video_ids[0])
        self.status.setText("Download Status: Downloading...")
        time.sleep(1)


        
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        destination = "."
        
        # download the file
        out_file = video.download(output_path=destination)
        self.status.setText("Download Status: Decoding...")
        time.sleep(1)
        
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.wav'
        os.rename(out_file, new_file)
        self.song_selection.addItem(new_file)

        self.status.setText("Download Status: Saving...")
        time.sleep(1)

        # result of success
        print(yt.title + " has been successfully downloaded.")
        print(trackname)
        self.status.setText("Download Status: Complete...")
        import pickle
        with open("data.dat","rb") as file:
                song_dict=pickle.load(file)
                song_dict[new_file]=trackname.title()
        with open("data.dat","wb") as file:
                pickle.dump(song_dict,file)
        #self.song_selection.addItem(yt.title)
        time.sleep(1)
    def play_pause(self):
        import pickle
        with open("data.dat","rb") as file:
                song_dict=pickle.load(file)
        str1=str(self.song_selection.currentText())
        self.track_playing.setText(song_dict[str1])
        global a
        if a==0:
                import subprocess
                import time
                from subprocess import Popen
                a=1
                print("Playing Pressed",str1)
                global p
                p = Popen(["afplay", str1])
                a=1
        else:
                
                print("Paused Pressed")
                p.terminate()
                a=0
                
                
        

    def setupUi(self, Musifre):
        global a 
        
        Musifre.setObjectName("Musifre")
        Musifre.resize(941, 460)
        Musifre.setMaximumSize(QtCore.QSize(941, 460))
        self.centralwidget = QtWidgets.QWidget(Musifre)
        self.centralwidget.setMaximumSize(QtCore.QSize(941, 481))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -10, 941, 481))
        self.widget.setMaximumSize(QtCore.QSize(941, 481))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(65, 151, 251, 255), stop:1 rgba(32, 241, 254, 255));\n"
"}")
        self.widget.setObjectName("widget")
        self.download = QtWidgets.QPushButton(self.widget)
        self.download.setGeometry(QtCore.QRect(190, 290, 191, 41))
        self.download.setStyleSheet("border-radius:20px;\n"
"font: 500 24pt \"Helvetica Neue\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.download.setObjectName("download")
        self.download.clicked.connect(self.download_music)
        self.status = QtWidgets.QLabel(self.widget)
        self.status.setGeometry(QtCore.QRect(200, 350, 181, 16))
        self.status.setTextFormat(QtCore.Qt.PlainText)
        self.status.setObjectName("status")
        self.logo = QtWidgets.QLabel(self.widget)
        self.logo.setGeometry(QtCore.QRect(30, 50, 271, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Design Support Files/Logo Design2.png"))
        self.logo.setObjectName("logo")
        self.track_name = QtWidgets.QLineEdit(self.widget)
        self.track_name.setGeometry(QtCore.QRect(80, 180, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(17)
        self.track_name.setFont(font)
        self.track_name.setStyleSheet("border-radius:20px;")
        self.track_name.setText("")
        self.track_name.setObjectName("track_name")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(590, 40, 16, 371))
        self.line.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.track_name_label_DE = QtWidgets.QLabel(self.widget)
        self.track_name_label_DE.setGeometry(QtCore.QRect(100, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(14)
        self.track_name_label_DE.setFont(font)
        self.track_name_label_DE.setObjectName("track_name_label_DE")
        self.track_playing = QtWidgets.QLabel(self.widget)
        self.track_playing.setGeometry(QtCore.QRect(670, 310, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.track_playing.setFont(font)
        self.track_playing.setStyleSheet("font: 500 30pt \"Helvetica Neue\";")
        self.track_playing.setObjectName("track_playing")
        
        self.song_selection = QtWidgets.QComboBox(self.widget)
        self.song_selection.setGeometry(QtCore.QRect(650, 280, 221, 26))
        self.song_selection.setObjectName("song_selection")
        self.song_selection.addItem("--No Song Selected--")
        ##
        import pickle
        with open("data.dat","rb") as file:
                data_bin_songname=pickle.load(file)
                songpath=data_bin_songname.keys()
                for i in songpath:
                        self.song_selection.addItem(i)
        self.visualization = QtWidgets.QLabel(self.widget)
        self.visualization.setGeometry(QtCore.QRect(660, 30, 201, 241))
        self.visualization.setStyleSheet("border-radius:20px")
        self.visualization.setText("")
        self.visualization.setPixmap(QtGui.QPixmap("Design Support Files/Visualisationfinal.png"))
        self.visualization.setObjectName("visualization")
        self.play = QtWidgets.QPushButton(self.widget)
        self.play.setGeometry(QtCore.QRect(730, 360, 51, 51))
        self.play.setStyleSheet("border-radius:24px;\n"
"font: 500 24pt \"Helvetica Neue\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.play.setObjectName("play")
        a=0
        self.play.clicked.connect(self.play_pause)
        #Paste Here
        Musifre.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Musifre)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 24))
        self.menubar.setObjectName("menubar")
        self.menuPort = QtWidgets.QMenu(self.menubar)
        self.menuPort.setObjectName("menuPort")
        Musifre.setMenuBar(self.menubar)
        self.actionExport_to_CSV = QtWidgets.QAction(Musifre)
        self.actionExport_to_CSV.setObjectName("actionExport_to_CSV")
        self.actionGenerate_Zip = QtWidgets.QAction(Musifre)
        self.actionGenerate_Zip.setObjectName("actionGenerate_Zip")
        self.menuPort.addAction(self.actionExport_to_CSV)
        self.menuPort.addSeparator()
        self.menuPort.addAction(self.actionGenerate_Zip)
        self.menubar.addAction(self.menuPort.menuAction())

        self.retranslateUi(Musifre)
        QtCore.QMetaObject.connectSlotsByName(Musifre)

    def retranslateUi(self, Musifre):
        _translate = QtCore.QCoreApplication.translate
        Musifre.setWindowTitle(_translate("Musifre", "Musifre"))
        self.download.setText(_translate("Musifre", "Download"))
        self.status.setText(_translate("Musifre", "Download Status: N/A"))
        self.track_name_label_DE.setText(_translate("Musifre", "Track Name"))
        self.track_playing.setText(_translate("Musifre", "Track Playing"))
        self.play.setText(_translate("Musifre", "| |"))
        self.menuPort.setTitle(_translate("Musifre", "Port"))
        self.actionExport_to_CSV.setText(_translate("Musifre", "Export to CSV"))
        self.actionExport_to_CSV.setShortcut(_translate("Musifre", "Ctrl+E"))
        self.actionGenerate_Zip.setText(_translate("Musifre", "Generate Zip"))
        self.actionGenerate_Zip.setShortcut(_translate("Musifre", "Ctrl+Shift+E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Musifre = QtWidgets.QMainWindow()
    ui = Ui_Musifre()
    ui.setupUi(Musifre)
    Musifre.show()
    sys.exit(app.exec_())