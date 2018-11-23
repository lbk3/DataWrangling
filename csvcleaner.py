Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import csv
>>> import os
>>> import pandas as pd
>>> os.chdir('yourpath')
>>> f = open('yourfile.txt','r')
>>> f = open('yourfile.csv','r')
>>> df = pd.read_csv(f, header=None).dropna(how='all',axis=1)
>>> df.columns = ['a', 'b']
>>> df.to_csv('filename.extension', sep='\t', encoding='utf-8')
>>> 
