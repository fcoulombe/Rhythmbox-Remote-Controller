#!/usr/bin/python
# -*- coding: utf-8 -*-

# sigslot.py
import sys
import socket
from PyQt4 import QtGui, QtCore

host = '192.168.0.11' 
port = 50000 
playlistSize = 64*1024*1024
def sendCommand(command, size=1024):    
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

    def soundChange(self, value):
        print "update the volume: " + str(float(value/100.0))
        songPlaying = sendCommand("Volume " + str(float(value/100.0)))
        self.updateTrackName(songPlaying)

    def initUI(self):

	#self.serverAddress = QTextInput(self)
        self.songPlaying = QtGui.QLabel(self)
        
        self.b1 = QtGui.QPushButton("Next", self)
        self.b2 = QtGui.QPushButton("Prev", self)
        self.b3 = QtGui.QPushButton("Play/Pause", self)
        #self.b5 = QtGui.QPushButton("ReloadPlayList", self)
        # self.playlist = QtGui.QListWidget(self)
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 100, 30)
       
        self.vbox = QtGui.QVBoxLayout()
    
        self.vbox.addWidget(self.songPlaying)
        self.vbox.addWidget(self.b1)
        self.vbox.addWidget(self.b3)
        self.vbox.addWidget(self.b2)
	    #self.vbox.addWidget(self.b5)
#	self.vbox.addWidget(self.playlist)
        self.vbox.addWidget(slider)

        self.setLayout(self.vbox)
        self.connect(self.b1,  QtCore.SIGNAL('clicked()'), self.next)
        self.connect(self.b2,  QtCore.SIGNAL('clicked()'), self.prev)
        self.connect(self.b3,  QtCore.SIGNAL('clicked()'), self.play)
       # self.connect(self.b5,  QtCore.SIGNAL('clicked()'), self.reload)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),self.soundChange)
        


        self.setWindowTitle('Rythmbox Remote')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = RythmBoxClient()
ex.show()
sys.exit(app.exec_())
