Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import csv
>>> import os
>>> import pandas as pd
>>> os.chdir('C:/Users/liamk/Desktop')
>>> f = open('rawgps.txt','r')

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    f = open('rawgps.txt','r')
IOError: [Errno 2] No such file or directory: 'rawgps.txt'
>>> f = open('rawgps.csv','r')
>>> df = pd.read_csv(f, header=None).dropna(how='all',axis=1)
>>> df.columns = ['Latitude', 'Longitude']
>>> df.to_csv('cleancoords.csv', sep='\t', encoding='utf-8')
>>> 
