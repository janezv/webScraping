#!/usr/bin/python
# -*- coding: latin-1 -*-
import time;
import os, sys, stat  #za dolocanja chmod
import shutil   #knjiznica za kopiranje
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#moral sem dati absolutno, ker relativne poti ne delajo
kredaricaToCheckAndDelete="/var/www/html/vreme/onlinePictures/historyKredarica"
grintovecToCheckAndDelete="/var/www/html/vreme/onlinePictures/historyGrintovec"
KamniskoSedloToCheckAndDelete="/var/www/html/vreme/onlinePictures/historyKamniskoSedlo"


#funkcija ki vrne najstarejsi file
def oldestFileDeleteIf(path,intMaxSize):
    size = get_size(path) #poglej koliko je Bytov v mapi kamor bomo kopirali
    if size>intMaxSize:
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        fileToDelete = files[0]
        #newest = files[-1]
        print "Oldest file that will be deleted:", fileToDelete
        os.remove(fileToDelete)
        
#funkcija ki vrne najstarejsi file, posebaj za kredarico, ker mi bo poslalo mail
def forKredaricaOldestFileDeleteIf(path,intMaxSize):
    size = get_size(path) #poglej koliko je Bytov v mapi kamor bomo kopirali
    if size>intMaxSize:
        os.chdir(path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        fileToDelete = files[0]
        #newest = files[-1]
        print "Oldest file that will be deleted:", fileToDelete
        os.remove(fileToDelete)
        #SEND ADVERTISEMENT OF THE DELETED FILE
        msg = MIMEMultipart()
        recipients = ['janez.vegan@gmail.com']
        msg['Subject'] = "Size in folder exceeded"
        msg.attach(MIMEText("Because size of picture in folder are exceeded the oldest picture has been deleted", 'plain'))
        #logiraj se in poslji mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("autoPython.send@gmail.com", "aut16sender")
        text = msg.as_string()
        server.sendmail("autoPython.send@gmail.com", recipients, text)
        #server.sendmail("autoPython.send@gmail.com", "hocevar.roman@gmail.com", msg)
        server.quit()
    
#funkcija za podatke
def dataUSA():
    t = time.localtime(time.time())
    strYear=str(t.tm_year)
    strMonth=str(t.tm_mon)
    strDay=str(t.tm_mday)
    strHour=str(t.tm_hour)
    strMin=str(t.tm_min)
    dUsa = strYear + "-" + strMonth + "-" + strDay +"_"+strHour+":"+strMin+"_"
    return dUsa

#izracunaj stevilo bytov
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def deleteOldest():
    print "prevec zasedeno zbrisal bom najstarejso sliko"
 
    #funkcija za kopiranje datotek
def copyFile(fileForCopy, folderToCopy):
    dirString = os.path.dirname(__file__)

    #this routin is for counting the files in the folder
    folder1="/var/www/html/vreme/onlinePictures/"+folderToCopy+"/"
    print "kopiral bom v sledec folder: ",folder1
    path, dirs, files = os.walk(folder1).next()
    file_count = len(files)
    indexOfPicture=str(file_count).zfill(4)
    print "nastel sem sledece file: "+indexOfPicture

    dUsa = dataUSA()  #klici funkcijo za racunanje casa
    #kopiraj file
    outFile = dirString + "/onlinePictures/"+ folderToCopy +"/"+indexOfPicture +"_"+dUsa + fileForCopy
    inFile = dirString + "/onlinePictures/"+fileForCopy
    print "picture that has been copied to history: ",outFile
    shutil.copy(inFile, outFile)       #kopiraj file


 
#GLAVNI PROGRAM     
fileForCopy="Grintovec.jpg"
folderToCopy="historyGrintovec"
copyFile(fileForCopy, folderToCopy)
fileForCopy="Kredarica.jpg"
folderToCopy="historyKredarica"
copyFile(fileForCopy, folderToCopy)
fileForCopy="KamniskoSedlo.jpg"
folderToCopy="historyKamniskoSedlo"
copyFile(fileForCopy, folderToCopy)
#poglej in brisi ce je prevec filov v grintovec
oldestFileDeleteIf(KamniskoSedloToCheckAndDelete,3000000)
forKredaricaOldestFileDeleteIf(kredaricaToCheckAndDelete,6500000000)
oldestFileDeleteIf(grintovecToCheckAndDelete,3000000)


print "narejeno"


















