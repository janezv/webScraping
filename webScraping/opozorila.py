#!/usr/bin/python

import MySQLdb
import smtplib
import requests
from BeautifulSoup import BeautifulSoup
import re
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


#ARSO najde TEMPERATURNE PODATKE
url = 'http://www.arso.gov.si/vreme/napovedi%20in%20podatki/zrak/opozorila/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

for div in soup.findAll("div", {"id": "opozorila"}):   #najdi vse tabele
    links=div.findAll("a")   #najdi vse tabele
    for link in links:
        msgt=link.contents[0]
        if len(msgt)>5:
            print "  "
            war=msgt.encode('utf-8')
            print type(war)
            print war
            print len(msgt)
            print "  "
            
            #pripravi mail
            msg = MIMEMultipart()
            #recipients = ['janez_vegan@yahoo.com','janez.vegan@gmail.com']
            recipients = ['janez_vegan@yahoo.com',,'janez.vegan@gmail.com']
            #msg['To'] = ", ".join(recipients)  //polje to
            msg['Subject'] = "Opozorila iz ARSO"
            msg.attach(MIMEText(war, 'plain'))
            #logiraj se in poslji mail
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("autoPython.send@gmail.com", "gesloZaObjavo")
            text = msg.as_string()
            server.sendmail("autoPython.send@gmail.com", recipients, text)
            #server.sendmail("autoPython.send@gmail.com", "hocevar.roman@gmail.com", msg)
            server.quit()
            
        #write to DB
        #connect to db
        try:
            db = MySQLdb.connect("localhost","webScreping","webScreping","webScraping", charset="utf8")   #(Server, User, Password, Data Base)
            cursor = db.cursor()  # prepare a cursor object using cursor() method
            print "connection succesful"
        except:
            print "connection do not succed"
        try:
            cursor.execute("INSERT INTO webScraping.opozorila VALUE (CURRENT_DATE(),%s)", (war,))
            db.commit()
            print "Vpisovano je opozorilo v DB"
        except:
            db.rollback()
            print "napaka pri vpisovanju v DB"
    
    

        


    





    
    
    

