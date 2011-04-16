#!/usr/bin/env python 

import socket 
import subprocess

def runProgram(program, command):
    p = subprocess.Popen(program + " " + command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = p.stdout.readlines()
    for line in lines:
        print line,
    retval = p.wait()
    return lines

def execCommand(command):
    from subprocess import call
    ret = runProgram("rhythmbox-client", command)
    return str(runProgram("rhythmbox-client", "--print-playing"))
    

host = '' 
port = 50000 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
    client, address = s.accept() 
    data = client.recv(size) 
    if data == None:
        continue

    if data == "Next":
        #exec next command
        ret = execCommand("--next")
        client.send(ret)
    if data == "Prev":
        print "exec prev"
        ret = execCommand("--previous")
        client.send(ret)

    if data == "Play":
        print "exec play"
        ret = execCommand("--play-pause")
        client.send(ret)

    import re
    r = re.compile('[ \t\n\r:]+')
    packet = r.split(data)
    if packet[0] == "Volume":
        print "exec play"
        ret = execCommand("--set-volume " + packet[1])
        client.send(ret)


    if data == "GetList":
        print "send playlist to client"
        ret = execCommand("--next")
        client.send(ret)

    if data == "Jump": #play a specific song
        #obtain song name
        print "exec jump command"
       
    if data == "enqueue":
        print "exec enqueue command" 
    client.close()
