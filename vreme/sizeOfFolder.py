#!/usr/bin/python
import os
import subprocess
import smtplib
import re
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#funkcija, ki racuna velikost mape (vkljucujoc podmape)
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size
    
#poklici funkcijo, ki racuna velikost mape 
sizeOfFolder = get_size('/var/www/html/vreme/onlinePictures/historyKredarica')                            
#preracunaj v kb, Mb in GB, ter pretvori v tekst
sizeOfFolderfloat=float(sizeOfFolder)
sizeOfFolderStr=str(sizeOfFolder)
sizeOfFolderKilo=sizeOfFolderfloat/1000
sizeOfFolderKiloStr=str(sizeOfFolderKilo)
sizeOfFolderMega=sizeOfFolderfloat/1000000
sizeOfFolderMegaStr=str(sizeOfFolderMega)
sizeOfFolderGiga=sizeOfFolderfloat/1000000000
sizeOfFolderGigaStr=str(sizeOfFolderGiga)
print sizeOfFolderStr, "b   [bytes]"
print sizeOfFolderKiloStr, "kb [kilo Bytes]"
print sizeOfFolderMegaStr, "Mb [Mega Bytes]"
print sizeOfFolderGigaStr, "Gb [Giga Bytes]"

#ce je vecja od 100Mb poslji mail
if sizeOfFolder>100000000:
    #logiraj se
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("autoPython.send@gmail.com", "aut16sender")
    #sestavi sporocilo in ga poslji
    msg = MIMEMultipart()
    msg['Subject'] = "Mapa nad 100Mb"
    msgBody = """Mapa s slikami Kredarice je 100MBytes
    prekoracila 1 Mb
    """
    msg.attach(MIMEText(msgBody, 'plain'))
    text = msg.as_string()
    server.sendmail("autoPython.send@gmail.com", "janez.vegan@gmail.com", text)
    print "poslan mail"


