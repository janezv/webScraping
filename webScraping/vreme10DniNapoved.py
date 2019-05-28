#!/usr/bin/python
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/
#http://stackoverflow.com/questions/4416013/beautiful-soup-python-and-the-extracting-of-text-in-a-table

#******************************************OPOZORILA***********************************************
#ker nisem nasel razreda td, torej <td>, sem ?el desni klik in nato source code
#tam sem v iframe najdel pravi link do tabele
#******************************************OPOZORILA***********************************************

import requests
from BeautifulSoup import BeautifulSoup
import re
napoved=[]
rezultat=[]

#ARSO najde TEMPERATURNE PODATKE
url = 'http://www.vreme.us/vremenska-napoved-10-dni.html'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

for data in soup.findAll('tr'):  #soup.findAll('tr',attrs={'style':'padding-top: 20px'})
    for table in data.findAll('table'):
        for i,row in enumerate(table.findAll('tr')):
            if i>50:
                break
            for cell in row.findAll('td'):
                if cell.find('td',attrs={'colspan':'2'}):
                    if cell.find('b'):
                        napoved.append(cell.text)
                if cell.find('font', attrs={'color':'red'}):
                    napoved.append(cell.find('font').text)

                
#for n, i in enumerate(napoved):
#   print n,"---->",i

inf=napoved[2]
print inf
print type(inf)

print "zacenjamo z splitom"
infL=inf.split(" - ")
for n,i in enumerate(infL):
    c=i.replace(";","<-->")
    d=c.replace("&#","<-->")
    e=d.replace("mm","<-->")
    #print n,"<------->",e
    j=e.split("<-->")
    for st, k in enumerate(j):
        #print k,"------------->",st
        if st==0:
            rezultat.append("datum")
        if st==1:
            d=str(k)
            rezultat.append(d)
        if st==3:
            rezultat.append(k)
    
for ind, izpis in enumerate(rezultat):
    print ind,"----------->",izpis

    
    

print "KONCANO"




                
            
        

    

                    

                    
                
            
        
    

            

            

        

            






    
    
    

