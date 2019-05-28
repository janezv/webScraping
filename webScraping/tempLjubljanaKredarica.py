#!/usr/bin/python
#https://first-web-scraper.readthedocs.org/en/latest/#act-3-web-scraping
import MySQLdb
import requests
from bs4 import BeautifulSoup

#ARSO najde TEMPERATURNE PODATKE
url = 'http://www.arso.gov.si/vreme/napovedi%20in%20podatki/vreme_si.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#find table with class name online, and list all html childrens
table = soup.find( "table", {"class":"online"} )
rows = table.findChildren(['tr'])


#find row for desired data and read a temperatura data, if there are no tempereature exit the program
temperKredarica = "-273"
temperKoper= "-273"
temperLjubljana = "-273"
for row in rows[2:]:#start for loop with index 2 because before this list are header without td childrens
	cells = row.findChildren('td')
	kraj = cells[0].text
	if ( kraj == "Kredarica" ):
		print (row)
		temperKredarica=cells[2].text
		print (temperKredarica)
	if ( kraj == "Ljubljana" ):
		print (row)
		temperLjubljana=cells[2].text
		print (temperLjubljana)
	if ( kraj == "Bilje Nova Gorica" ):
		print (row)
		temperKoper=cells[2].text
		print (temperKoper)

#Povezi se v bazo
try:
   db = MySQLdb.connect("localhost","webScreping","webScreping","webScraping")   #(Server, User, Password, Data Base)
   cursor = db.cursor()  # prepare a cursor object using cursor() method
   print "connection succesful"
except:
   print "connection do not succed"

#Pisi v bazo
try:
   cursor.execute("INSERT INTO webScraping.temper VALUE (CURRENT_DATE(),%s,%s,%s)", (temperKredarica,temperKoper,temperLjubljana))
   db.commit()
   print "Vpisana je temperatura"
except:
   db.rollback()
   print "Napaka pri vpisu podatkov v tabelo"
   
#posli mail,  da se je vpisalo v bazo
#import smtplib
#
#server = smtplib.SMTP('smtp.gmail.com', 587)
#
#print "narejeno, okej je"
#server.starttls()
#server.login("autoPython.send@gmail.com", "aut16sender")
#
#msg = """To je sporocilo iz
#        tempLjubljanaKredarica.py
#        Ravnokar so se v mysql bazo vpisali
#        temperaturni podarki
#    """
#print type(msg)
#server.sendmail("autoPython.send@gmail.com", "janez.vegan@gmail.com", msg)
#server.quit()





