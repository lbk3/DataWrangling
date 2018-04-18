Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.sentiment.vader import SentimentIntensityAnalyzer

Warning (from warnings module):
  File "C:\Python27\lib\site-packages\nltk\twitter\__init__.py", line 20
    warnings.warn("The twython library has not been installed. "
UserWarning: The twython library has not been installed. Some functionality from the twitter package will not be available.
>>> import pandas as pd
>>> import string
>>> import matplotlib.pyplot as plt
>>> import os
>>> os.chdir('C:\Users\liamk\Desktop') #Change working directory
>>> sentences = [line.rstrip() for line in open("vadertext.txt")] #Load text file to list
>>> sid = SentimentIntensityAnalyzer() #Initialise Vader
>>> len(sentences) #Code check
7086
>>> summary = {"positive":0,"neutral":0,"negative":0} #Create variable to store VADER results
>>> #Loop through each entry in sentences and update corresponding summary score
>>> for x in sentences:
	sen_pol = sid.polarity_scores(x)
	if sen_pol ["compound"] == 0.0:
		summary["neutral"] +=1
	elif sen_pol ["compound"] > 0.0:
		summary["positive"] +=1
	else:
		summary["negative"] +=1

		
>>> print(summary) #Code check
{'positive': 3855, 'neutral': 804, 'negative': 2427}
>>> #Use matplotlib to turn results into pie chart
>>> labels = 'Positive', 'Neutral', 'Negative'
>>> sizes = [54.409, 11.344, 34.246]
>>> 
>>> fig1, ax1 = plt.subplots()
>>> ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
([<matplotlib.patches.Wedge object at 0x10A10DB0>, <matplotlib.patches.Wedge object at 0x10A21430>, <matplotlib.patches.Wedge object at 0x10A21A50>], [Text(-1.08946,-0.151896,'Positive'), Text(0.651118,-0.886592,'Neutral'), Text(0.96801,0.522453,'Negative')], [Text(-0.594252,-0.0828524,'54.4%'), Text(0.355155,-0.483596,'11.3%'), Text(0.528005,0.284975,'34.2%')])
>>> ax1.axis('equal')
(-1.1110141513782168, 1.107683133780741, -1.1106428511924848, 1.1005068378243725)
>>> plt.tight_layout()
>>> plt.show()
>>> 
