#!/usr/bin/python
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

#funkcija za download slike
def download_photo(img_url, filename):
    image_on_web = urllib.urlopen(img_url)
    downloaded_image = file(filename, "wb")
    while True:
        buf = image_on_web.read(65536)
        if len(buf) == 0:
            break
        downloaded_image.write(buf)
    downloaded_image.close()
    image_on_web.close()


#slika iz kredarice
url = "http://www.hribi.net/spletna_kamera/kredarica/20"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("img")
link=imgs[3].get('src')
print "SLIKA IZ KREDARICE JE V ARRAY[3]: "+link
download_photo(link,"/var/www/html/vreme/onlinePictures/Kredarica.jpg")

#slika iz smarnegore
url = "http://www.hribi.net/spletna_kamera/smarna_gora/315"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)
imgs = soup.findAll("img")
link=imgs[3].get('src')
print "SLIKA IZ SMARNE GORE JE V ARRAY[3]: "+link
download_photo(link,"/var/www/html/vreme/onlinePictures/SmarnaGora.jpg")

#slika iz Kamniskega sedla
url = "http://www.hribi.net/spletna_kamera/kamnisko_sedlo/2326"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("img")
link=imgs[3].get('src')
print "SLIKA IZ KAMNISKEGA SEDLA JE V ARRAY[3]: "+link
download_photo(link,"/var/www/html/vreme/onlinePictures/KamniskoSedlo.jpg")

#slika iz Zavizan
url = "http://hr.hribi.net/kamere.asp?kameraid=2007"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("img")
link=imgs[3].get('src')
print "SLIKA IZ ZAVIZAVA JE V ARRAY[3]: "+link
download_photo(link,"/var/www/html/vreme/onlinePictures/Zavizan.jpg")

#slika Grintovca in Krvavca
url = "http://www.hribi.net/spletna_kamera/grintovec/1570"
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

imgs = soup.findAll("img")
for img in imgs:
    print "link je:"
    print img.get('src')

imgs = soup.findAll("img")
link=imgs[3].get('src')
print "SLIKA IZ GRINTOVCA JE V ARRAY[3]: "+link
download_photo(link,"/var/www/html/vreme/onlinePictures/Grintovec.jpg")










    
    
    

