#!/usr/bin/python
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/
#http://stackoverflow.com/questions/4416013/beautiful-soup-python-and-the-extracting-of-text-in-a-table

#******************************************OPOZORILA***********************************************
#ker nisem nasel razreda td, torej <td>, sem ?el desni klik in nato source code
#tam sem v iframe najdel pravi link do tabele
#******************************************OPOZORILA***********************************************
import MySQLdb
import requests
from BeautifulSoup import BeautifulSoup
import re

arsoTabelaData=[]
sneg=[]

#ARSO najde TEMPERATURNE PODATKE
url = 'http://www.meteo.si/uploads/probase/www/observ/surface/text/sl/observation_si-snow_latest.html'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

for i in soup.findAll('td'):
    arsoTabelaData.append(i.text.replace('&nbsp;', ''))

try:
    index=arsoTabelaData.index("Kredarica")
    print arsoTabelaData[index]
    print "Sneg  visina: ", arsoTabelaData[index+3]
    kredaricaSneg=arsoTabelaData[index+3]
    print "Zapadlo v pol dneva:",arsoTabelaData[index+2]
    kredaricaPadlo=arsoTabelaData[index+2]
except:
    print "Za sneg na kredarici ni vec podatkov"
    kredaricaSneg="Ni podatka"
    kredaricaPadlo="Ni podatka"
    
try:
    index=arsoTabelaData.index("Ljubljana")
    print arsoTabelaData[index]
    print "Sneg  visina: ", arsoTabelaData[index+3]
    ljubljanaPadlo=arsoTabelaData[index+3]
except:
    ljubljanaPadlo="Ni podatka"
#***********************************************************
#********************PODATKI Zavizan************************
url = 'http://vrijeme.hr/aktpod.php?id=sneg'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

for table in soup.findAll('table'):   #najdi vse tabele
    for div in table.findAll('div',{'class':'sadrzajContents'}):   #znotraj tabele najdi vse div razreda sadrzajContents
        for cell in div.findAll('td'):    #znotraj te tabele najdi vse celice in izpisi vsebino
            sneg.append(cell.text.replace('&nbsp;', ''))
            
url = 'http://vrijeme.hr/aktpod.php?id=snijeg'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

for table in soup.findAll('table'):   #najdi vse tabele
    for div in table.findAll('div',{'class':'sadrzajContents'}):   #znotraj tabele najdi vse div razreda sadrzajContents
        for cell in div.findAll('td'):    #znotraj te tabele najdi vse celice in izpisi vsebino
            sneg.append(cell.text.replace('&nbsp;', ''))
        
try: 
    index=sneg.index("Zavi&#382;an")
    print sneg[index]
    print "Visina snega:",sneg[index+1],"cm"
    zavizanSneg=sneg[index+1]
    print "Zapadlo snega:",sneg[index+2],"cm"
    zavizanPadlo=sneg[index+2]
except:
    print "za Zavizan ni vec podatkov"
    zavizanSneg = "Ni podatka"
    zavizanPadlo = "Ni podatka"
    

#******************Povezi in zapisi podatke v bazo
#Povezi se v bazo
try:
   db = MySQLdb.connect("localhost","webScreping","webScreping","webScraping")   #(Server, User, Password, Data Base)
   cursor = db.cursor()  # prepare a cursor object using cursor() method
   print "connection succesful"
except:
   print "connection do not succed"
   
#Pisi v bazo
sql="""INSERT INTO webScraping.sneg (Dan, Kredarica, KredaricaPadlo, Zavizan, ZavizanPadlo, Ljubljana)
    VALUE (CURRENT_DATE(),%s,%s,%s,%s,%s)"""
sqlData=(kredaricaSneg,kredaricaPadlo,zavizanSneg,zavizanPadlo, ljubljanaPadlo)
try:
   cursor.execute(sql, sqlData)
   db.commit()
   print "Vpisana je visina snega"
except:
   db.rollback()
   print "Napaka pri vpisu podatkov v tabelo"




    
    
    

