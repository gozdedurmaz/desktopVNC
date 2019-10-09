# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listandremove.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import xwindowslist
import os
from signal import alarm, signal, SIGALRM, SIGKILL
import subprocess
import re

data = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 30, 311, 221))
        self.listWidget.setObjectName("listWidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 280, 100, 30))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 320, 100, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 360, 100, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(460, 30, 200, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEnabled(False)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 110, 121, 17))
        self.label.setObjectName("label")
        self.label.setEnabled(False)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 180, 100, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 250, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setEnabled(False)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(460, 310, 110, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setEnabled(False)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 360, 110, 30))
        self.pushButton_6.setObjectName("pushButton_5")
        self.pushButton_6.setEnabled(False)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 365, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.setEnabled(False)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 325, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.setEnabled(False)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(650, 290, 90, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setText("View Only")
        self.checkBox.setEnabled(False)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(650, 320, 90, 23))
        self.checkBox_2.setObjectName("checkBox")
        self.checkBox_2.setText("Share Only")
        self.checkBox_2.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.setText("Remove")
        self.pushButton_2.setText("Update List")
        self.pushButton_3.setText("Selection")
        self.pushButton.setEnabled(False)
        self.pushButton_4.setText("OK")
        self.pushButton_5.setText("Paylaşıma Aç")
        self.pushButton_6.setText("Root Olarak Aç")
        MainWindow.setWindowTitle("-Gözde Uygulama-")
        self.label_3.setText("-")
        self.label_4.setText("-")
        self.label.setText(self.comboBox.currentText())  # ilk basta hangi secenek varsa onu yazması için (generic)
        self.label_2.setText("-")  # ok'a basılmadan bi şey yazılı olmaması


#ACTIONS
        command = "ps aux | grep x11vnc"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        basedata = str(out).split("\\n")
        basedata = basedata[:-1]


        for x in basedata:
            if not "grep x11vnc" in x:
                self.listWidget.addItem(str(x))

        self.listWidget.clicked.connect(self.aktiflestir)

        self.pushButton.clicked.connect(self.remove)
        self.pushButton_2.clicked.connect(self.yenile)
        self.pushButton_3.clicked.connect(self.opencombo)
        self.pushButton_6.clicked.connect(self.rootac)

        data = xwindowslist.idofwindows()
        print(data)
        for x in data:
            print(xwindowslist.nameofid(x))
            self.comboBox.addItem(str(xwindowslist.nameofid(x)[0]))  # xwindowslistten çektim combo box'a koydum


    def opencombo(self):
        self.comboBox.setEnabled(True)
        self.label.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.label_2.setEnabled(True)

        self.comboBox.currentTextChanged.connect(self.onActivated)
        self.pushButton_4.clicked.connect(self.cikti)
        self.pushButton_5.clicked.connect(self.paylasim)
        self.pushButton_6.clicked.connect(self.rootac)

    def rootac(self):

        # !çalışmıyor
        print("elma1")

        bilgi = self.label_2.text()

        command = 'DISPLAY=:1 pkexec x11vnc -id ' + bilgi # + ' > /dev/null 2>&1 &'
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        proc.wait()
        (out, err) = proc.communicate()
        print("elma2")

        #yeniliyoruz
        self.listWidget.clear()  # tüm listeyi temizledim cunku guncel liste olusturacagım

        command = "ps aux | grep x11vnc"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        basedata = str(out).split("\\n")
        basedata = basedata[:-1]  # basedata oluşturuldu

        for x in basedata:  # basedatadakileri listeye ekledim
            if not "grep x11vnc" in x:
                self.listWidget.addItem(str(x))

        self.label_3.setEnabled(True)

    def paylasim(self):

        if self.checkBox.isChecked():
            proc = subprocess.Popen(self.viewOnly(), stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            self.yenile()
            self.label_3.setEnabled(True)

        elif self.checkBox_2.isChecked():
            proc = subprocess.Popen(self.shareOnly(), stdout=subprocess.PIPE, shell=True)
            (out, err) = proc.communicate()
            self.yenile()
            self.label_3.setEnabled(True)

        else:
            bilgi = self.label_2.text()
            command = 'x11vnc -id ' + bilgi + '> /dev/null 2>&1 &'
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            proc.wait()
            (out, err) = proc.communicate()
            self.yenile()
            self.label_3.setEnabled(True)


    def cikti(self):

        item_ = self.comboBox.currentText() #string tipinde
        list_id = []
        list_id = xwindowslist.idofwindows() #xwindowslist.idofwindows() id döndürüyor list tipinde
        i1 = 0
        for i in list_id:
            if (item_ == str(xwindowslist.nameofid(i)[0])): #['Xfdesktop', 'Desktop']
                self.label_2.setText(str(list_id[i1]))
            i1=i1+1

        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.checkBox.setEnabled(True)
        self.checkBox.clicked.connect(self.viewOnly)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.clicked.connect(self.shareOnly)

    def viewOnly(self):
        bilgi = self.label_2.text()
        command = "x11vnc -id " + bilgi + " -viewonly" + '> /dev/null 2>&1 &'
        '''proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)request()
        (out, err) = proc.communicate()'''
        return command

    def shareOnly(self):
        bilgi = self.label_2.text()
        command = "x11vnc -id " + bilgi + " -shared" + '> /dev/null 2>&1 &'
        '''proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()'''
        return command

    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def yenile(self):

        self.listWidget.clear()  # tüm listeyi temizledim cunku guncel liste olusturacagım

        command = "ps aux | grep x11vnc"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        basedata = str(out).split("\\n")
        basedata = basedata[:-1] #basedata oluşturuldu

        for x in basedata:  #basedatadakileri listeye ekledim
            if not "grep x11vnc" in x:
                self.listWidget.addItem(str(x))

    def remove(self):
        item = self.listWidget.currentItem() #listedeki secili item #
        item = item.text()
        split1 = item.split(" ")
        split2 = list(filter(None, split1)) #pid değerine ulaştım basedatadaki
        pid = int(split2[1])

        try: #root olmayan kullanıcı için kill yapmaya çalıştı
            os.kill(pid, SIGKILL)
            print("kavun")
            item1 = self.listWidget.selectedItems()
            for counter in item1:
                print("elma")
                self.listWidget.takeItem(self.listWidget.row(counter))
                print("armut")

        except OSError as e:
            err=e
            print("karpuz")

            if "Operation not permitted" in str(err):  # kill ile olmuyorsa pkexec kullansın
                print("kiraz")
                command = "pkexec kill " + str(pid)
                proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()

                item = self.listWidget.selectedItems()
                for counter in item:
                  self.listWidget.takeItem(self.listWidget.row(counter))

        print("papatya")

        if self.listWidget.count() == 0:
            self.pushButton.setEnabled(False)
            self.label_4.setText("-")
            self.label_3.setText("-")
            self.label_3.setEnabled(False)
            self.label_4.setEnabled(False)

    def pidalportver(self):

        item = self.listWidget.currentItem()  # listedeki secili item #
        item = item.text()
        split1 = item.split(" ")
        split2 = list(filter(None, split1))  # pid değerine ulaştım basedatadaki
        pid = int(split2[1])

        command = "lsof -p " + str(pid) + " | grep LISTEN | head -1"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        print(out)
        print("kaplumbaga")
        new_out = str(out).split("*:") # 5901 (LISTEN)\n'
        print(new_out)
        print("summer")
        new_out = str(new_out[1]).split(" ") #['5901', "(LISTEN)\\n'"]
        print(new_out)
        print("winter")

        portnumber = str(new_out[0]) #port number budur = 5901

        self.label_3.setText("PORT=" + portnumber)

    def isimver(self):
        item = self.listWidget.currentItem()
        item = item.text()
        item = item.split("-id ")
        new_item = item[1]
        print(new_item)

        self.label_4.setText(str(xwindowslist.nameofid([new_item][0])[0]))


    def aktiflestir(self):
        self.pushButton.setEnabled(True)
        self.label_3.setEnabled(True)
        self.label_4.setEnabled(True)
        self.pidalportver()
        self.isimver()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
