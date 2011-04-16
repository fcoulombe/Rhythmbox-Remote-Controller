#!/usr/bin/python
# -*- coding: utf-8 -*-

# sigslot.py
#test
#test2
import sys
import socket
from PyQt4 import QtGui, QtCore

host = '192.168.0.11' 
port = 50000 
size = 1024 

def sendCommand(command):    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host,port)) 
    s.send(command) 
    data = s.recv(size) 
    s.close() 
    return data
    #print 'Received:', data



class RythmBoxClient(QtGui.QWidget):
  
    def __init__(self):
        super(RythmBoxClient, self).__init__()
        
        self.initUI()

    def updateTrackName(self, songPlaying):
        self.songPlaying.setText("currently playing: \n" + songPlaying)

    def next(self):
        print "next"
        songPlaying = sendCommand("Next")
        self.updateTrackName(songPlaying)

    def prev(self):
        print "prev"
        songPlaying = sendCommand("Prev")
        self.updateTrackName(songPlaying)

    def play(self):
        print "play/pause"
        songPlaying = sendCommand("Play")
        self.updateTrackName(songPlaying)

    def reload(self):
        print "reload"
        songPlaying = sendCommand("Reload")
        self.updateTrackName(songPlaying)


    def initUI(self):

	#self.serverAddress = QTextInput(self)
        self.songPlaying = QtGui.QLabel(self)
        
        self.b1 = QtGui.QPushButton("Next", self)
        self.b2 = QtGui.QPushButton("Prev", self)
        self.b3 = QtGui.QPushButton("Play/Pause", self)
        #self.b5 = QtGui.QPushButton("ReloadPlayList", self)
        #self.playlist = QtGui.QListWidget(self)

        self.vbox = QtGui.QVBoxLayout()
    
        self.vbox.addWidget(self.songPlaying)
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b2)

        self.setLayout(self.vbox)
        self.connect(self.b1,  QtCore.SIGNAL('clicked()'), self.next)
        self.connect(self.b2,  QtCore.SIGNAL('clicked()'), self.prev)
        self.connect(self.b3,  QtCore.SIGNAL('clicked()'), self.play)


        self.setWindowTitle('Rythmbox Remote')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = RythmBoxClient()
ex.show()
sys.exit(app.exec_())
