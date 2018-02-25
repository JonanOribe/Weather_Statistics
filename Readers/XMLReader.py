'''
Created on 1 feb. 2018

@author: Jonan
'''

import bs4 as bs
import urllib.request
#import numpy as np
import pandas as pd
import re

counter=0
cp=48020
data=[]

"""
class Places(object):
    def __init__(self,id,city,province,date):
        self.id=id
        self.city=city
        self.province=province
        self.date=date
    def __str__(self):    # All we have done is renamed the method
            return "({0},{1},{2},{3})".format(self.id, self.city,self.province,self.date)
"""

#print("How many cities do you want to work with?")
#cities=input()
cities=8

try:

    while counter<int(cities):
        url="http://www.aemet.es/xml/municipios/localidad_"
        urlRequest = urllib.request.urlopen(url+str(cp)+".xml").read()
        soup=bs.BeautifulSoup(urlRequest,"lxml")

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
            print("Date: "+dateNumber)
 
        cp+=10

        for temperature in soup.find_all('prediccion'):
            temperatureValue=temperature
            print("Temperature: "+temperatureValue)

        #temperature=takeTemperature()

        #print(temperature)

        actualPlace=[cityName,provinceName,cpNumber,dateNumber]

        data.append(actualPlace)

        print(data)

except:

    print("<------No postal code like "+str(cp)+"------>")

columns=["City","Province","CP","Date"]

df=pd.DataFrame(data,columns=columns) 

df.to_csv("weatherStatus.csv", sep='\t', encoding='utf-8')

print(df)

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility


def takeTemperature():

    regex = r"(<temperatura>)\n(<maxima>)\d*(<\/maxima>)\n(<minima>)2(<\/minima>)"

    test_str = str(soup)

    matches = re.finditer(regex, test_str)

    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1

        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    return match