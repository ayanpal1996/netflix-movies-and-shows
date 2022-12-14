

import pandas as pd
data=pd.read_csv(r"C:\Users\aychowdh\Downloads\netflix data.csv")



# In[4]:


data.head()


# In[5]:


data.tail()


# In[9]:


data.shape


# In[10]:


data.size


# In[11]:


data.columns


# In[13]:


data.dtypes


# #finding duplicate rows

# In[15]:


data[data.duplicated()]


# In[17]:


data.drop_duplicates(inplace=True)#if there is any duplictes result we can get rid of it using this code


# In[18]:


data[data.duplicated()]


# In[19]:


data.isnull()


# In[22]:


data.isnull().sum()


# In[21]:


import seaborn as sna


# In[23]:


sna.heatmap(data.isnull())


# In[24]:


data.head()


# In[28]:


data[data['title'].isin(["Kota Factory"])]#isin used to find a particular value 


# In[33]:


data[data['title'].str.contains("Zubaan")]


# In[35]:


data.dtypes


# In[39]:


data['Data_added_New']=pd.to_datetime(data['date_added'])


# In[41]:


data.dtypes


# In[45]:


data['Data_added_New'].dt.year.value_counts()#number of movies and tv shows release in a year 


# In[46]:


data['Data_added_New'].dt.year.value_counts().plot(kind='bar')#Ploting bar graph 


# In[51]:


data.groupby('type').type.count()#groupby is used to creat groups [data.groupby()]


# In[53]:


sna.countplot(data['type'])


# In[54]:


data.head(2)


# In[58]:


data[(data['type']=='Movie')&(data["release_year"]==2020)]


# In[59]:


data.head(2)


# In[73]:


data[(data['type']=='TV Show')&(data['country']=='India')]["title"]


# In[88]:


data['director'].value_counts().head(10)#Top 10 directors who gave maximum number of shows and movies 


# In[92]:


data1=data[data['country']=='India'


# In[93]:


data1.head(2)


# In[99]:


data1['director'].value_counts().head(10)#showing top directors from India who directed higest number of movies and Tv Shows


# In[102]:


data[(data['type']=='Movie')&(data['listed_in']=='Romantic Movies')&(data["country"]=="United States")]


# In[103]:


data[(data['type']=='Movie')&(data['listed_in']=='Romantic Movies')|(data['country']=="India")]


# In[108]:


data[data['cast']=='Tom Cruise']


# In[110]:


data[data['cast'].str.contains('Tom Cruise')]


# In[111]:


data_new=data.dropna()#Drop rows which have null values 


# In[112]:


data_new.head(2)


# In[113]:


data_new[data_new['cast'].str.contains('Tom Cruise')]#Movies and Tv series where Tom cruise was cast


# In[114]:


data['rating'].unique()


# In[117]:


data['rating'].nunique()


# In[14]:


data[(data['rating']=="TV-14")&(data['type']=='Movie')&(data['country']=='Canada')]


# In[17]:


data[(data['type']=='TV Show')&(data['rating']=='TV-14')&(data['release_year']>2018)]#Tv-shows got TV-14 rating after 2018


# In[19]:


data.duration.unique()


# In[21]:


data.duration.dtype


# In[25]:


data[['Minutes','Units']]=data['duration'].str.split(' ',expand=True)#Spliting a string to make two cloumns 


# In[26]:


data.head(2)


# In[36]:


data['Minutes'].dtype


# In[84]:


data2=data.Minutes.astype(float) #converting objct type into float


# In[2]:


data[data2['Minutes']==312.0


# In[3]:


data[data2['Minutes']==312.0'


# In[62]:


data2.min()


# In[88]:


data2.max()


# In[64]:


data_tvshow=data[data['type']=='TV Show']#crteating new data set contains only tv shows 


# In[65]:


data.head(2)


# In[66]:


data_tvshow.country.value_counts()


# In[67]:


data_tvshow.country.value_counts().head(1)#filtaring the country with maximum tv shows


# In[80]:


data.sort_values(by='release_year',ascending=False)# sorting data acordding to release yaer


# In[81]:


data[(data['type']== 'Movie')&(data['listed_in']=='Dramas')|(data['type']== 'TV Show')&(data['listed_in']=='kids')


# In[ ]:




