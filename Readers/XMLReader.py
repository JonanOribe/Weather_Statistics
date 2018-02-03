'''
Created on 1 feb. 2018

@author: Jonan
'''

import bs4 as bs
import urllib.request

counter=0
cp=48020

print("How many cities do you want to work with?")
cities=input()

while counter<int(cities):

    url = urllib.request.urlopen("http://www.aemet.es/xml/municipios/localidad_"+str(cp)+".xml").read()
    soup=bs.BeautifulSoup(url,"lxml")

    counter+=1

    print("*********************************************")
    print("PLACE: "+str(counter))
    for city in soup.find_all('nombre'):
        print("City: "+city.text)
    
    for province in soup.find_all('provincia'):
        print("Province: "+province.text)
    
    for date in soup.find_all('elaborado'):
        print("Date: "+date.text)
    
    cp+=10
    """
    for date in soup.find_all('dia'):
        if date.text != "":
            print("Date: "+ date.text)
    """
