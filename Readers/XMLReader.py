'''
Created on 1 feb. 2018

@author: Jonan
'''

import bs4 as bs
import urllib.request
import numpy as np
import pandas as pd


counter=0
cp=48020

#Create the dataFrame

class Places(object):
    def __init__(self,id,city,province,date):
        self.id=id
        self.city=city
        self.province=province
        self.date=date
    def __str__(self):    # All we have done is renamed the method
            return "({0},{1},{2},{3})".format(self.id, self.city,self.province,self.date)

print("How many cities do you want to work with?")
cities=input()

citiesStatus=[]

try:

    while counter<int(cities):

        url = urllib.request.urlopen("http://www.aemet.es/xml/municipios/localidad_"+str(cp)+".xml").read()
        soup=bs.BeautifulSoup(url,"lxml")

        counter+=1

        print("*********************************************")
        print("PLACE: "+str(counter))
        id=counter
        for city in soup.find_all('nombre'):
            cityName=city.text
            print(cityName)
            print("City: "+city.text)

        for province in soup.find_all('provincia'):
            provinceName=province.text
            print("Province: "+province.text)
            cpNumber=cp
            print("CP: "+str(cp))

        for date in soup.find_all('elaborado'):
            dateNumber=date.text
            print("Date: "+date.text)
 
        cp+=10

        place=Places(cityName,provinceName,cpNumber,date)
        citiesStatus.append(place)
        print(str(place))

except:

    print("<------No postal code like "+str(cp)+"------>")

df=pd.DataFrame(citiesStatus,columns=["City","Province","CP","Date"]) #One data for 4 columns,that is the problem
print(df)
#df.to_csv("weatherStatus.csv", sep='\t', encoding='utf-8')
