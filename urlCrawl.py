Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import unicodecsv
>>> import urllib2
>>> from bs4 import BeautifulSoup
>>> from datetime import datetime
>>> target_page = 'http://www.newlook.com/uk/womens/clothing/dresses/black-floral-print-soft-touch-dress/p/563723709?comp=Browse'
>>> page = urllib2.urlopen(target_page)
>>> soup = BeautifulSoup(page,'html.parser')
>>> name_box = soup.find('h1',attrs={'class': 'product-description__name'})
>>> name = name_box.text.strip()
>>> price_box = soup.find('span',attrs={'class':'price'})
>>> price = price_box.text.strip()
>>> with open ('price.csv','a') as csv_file:
	writer = unicodecsv.writer(csv_file)
	writer.writerow([name,price,datetime.now()])

	
>>> 
