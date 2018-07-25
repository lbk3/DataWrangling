Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> from sklearn import model_selection
>>> from sklearn.feature_extraction.text import TfidfVectorizer
>>> from sklearn.naive_bayes import MultinomialNB
>>> from sklearn.utils import shuffle
>>> import os
>>> os.chdir('YOUR_PATH') #Change working directory
>>> names =['Sentiment','Sentence'] #Create labels for dataset
>>> f = 'FILE_NAME' #Access file
>>> dataset = pd.read_csv(f, sep='\t', names=names) #Load file and labels to pandas dataframe, separate on tab
>>> df = shuffle(dataset) #Randomly shuffle dataset
>>> df.head() #Test to see if code is working
      Sentiment                                           Sentence
5927          0    This quiz sucks and Harry Potter sucks ok bye..
5803          0  Not because I hate Harry Potter, but because I...
2469          1                               I love Harry Potter.
3669          1              dudeee i LOVED brokeback mountain!!!!
5447          0    This quiz sucks and Harry Potter sucks ok bye..
>>> df_x = dataset["Sentence"] #Assign value to Sentence column
>>> df_y = dataset["Sentiment"] #Assign value to Sentiment column
>>> cv = TfidfVectorizer(min_df=1,stop_words='english') #Load feature extractor
>>> xcolumn_train, xcolumn_test, ycolumn_train, ycolumn_test = model_selection.train_test_split(df_x,df_y,test_size=0.2,random_state=4) #Split test and training data with 80/20 ratio
>>> x_traincv=cv.fit_transform(xcolumn_train) #Train with original training data
>>> a=x_traincv.toarray() #Convert to array
>>> cv.inverse_transform(a[20]) #Check any entry to see if it has been converted
[array([u'code', u'da', u'happy', u'sucks', u'vinci'], dtype='<U62')]
>>> mnb=MultinomialNB() #Initialise the machine learning classifier
>>> ycolumn_train=ycolumn_train.astype('int') #Convert the test data to int
>>> mnb.fit(x_traincv,ycolumn_train) #Populate classifier with training data
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
>>> x_testcv = cv.transform(xcolumn_test) #Extract tfidf features and apply to test set
>>> pred = mnb.predict(x_testcv) #Gather predictions of test data
>>> actual =np.array(ycolumn_test) #Gather actual results
>>> count = 0 #Set count to 0 before passing to loop
>>> #Loop through each entry of predictions, add 1 to count if it is a match
>>> for i in range (len(pred)):
	if pred[i] == actual[i]:
		count = count + 1

		
>>> count
1359
>>> len(pred)
1384
>>> accuracy = 1359/1384.0
>>> print("Multinomial Naive Bayes Accuracy: " + str(accuracy))
Multinomial Naive Bayes Accuracy: 0.981936416185
>>> 
