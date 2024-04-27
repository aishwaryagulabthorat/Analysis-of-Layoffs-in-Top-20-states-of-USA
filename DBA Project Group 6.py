#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


albama=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Alabama.xlsx")

arizona=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Arizona.xlsx")

california=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/California.xlsx")

colorado=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Colorado.xlsx")

connecticut=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Connecticut.xlsx")

florida=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Florida.xlsx")

georgia=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Georgia.xlsx")

indiana=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Indiana.xlsx")

kansas=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Kansas.xlsx")

kentucky=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Kentucky.xlsx")

maryland=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Maryland.xlsx")

michigan=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Michigan.xlsx")

missouri=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Missouri.xlsx")

new_jersey=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/New Jersey.xlsx")

new_york=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/New York.xlsx")

ohio=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Ohio.xlsx")

pennsylvania=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Pennsylvania.xlsx")

texas=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Texas.xlsx")

virginia=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Virginia.xlsx")

washington=pd.read_excel(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/states files/Washington.xlsx")


# In[3]:


print(albama.columns)
print(arizona.columns)
print(california.columns)
print(colorado.columns)
print(connecticut.columns)
print(florida.columns)
print(georgia.columns)
print(indiana.columns)
print(kansas.columns)
print(kentucky.columns)
print(maryland.columns)
print(michigan.columns)
print(missouri.columns)
print(new_jersey.columns)
print(new_york.columns)
print(ohio.columns)
print(pennsylvania.columns)
print(texas.columns)
print(virginia.columns)
print(washington.columns)


# In[4]:


print(albama.columns.shape)
print(arizona.columns.shape)
print(california.columns.shape)
print(colorado.columns.shape)
print(connecticut.columns.shape)
print(florida.columns.shape)
print(georgia.columns.shape)
print(indiana.columns.shape)
print(kansas.columns.shape)
print(kentucky.columns.shape)
print(maryland.columns.shape)
print(michigan.columns.shape)
print(missouri.columns.shape)
print(new_jersey.columns.shape)
print(new_york.columns.shape)
print(ohio.columns.shape)
print(pennsylvania.columns.shape)
print(texas.columns.shape)
print(virginia.columns.shape)
print(washington.columns.shape)


# In[5]:


print(albama.info())
# print(arizona.info())
# print(california.info())
# print(colorado.info())
# print(connecticut.info())
# print(florida.info())
# print(georgia.info())
# print(indiana.info())
# print(kansas.info())
# print(kentucky.info())
# print(maryland.info())
# print(michigan.info())
# print(missouri.info())
# print(new_jersey.info())
# print(new_york.info())
# print(ohio.info())
# print(pennsylvania.info())
# print(texas.info())
# print(virginia.info())
# print(washington.info())


# In[6]:


albama['Number of Workers']=albama['Number of Workers'].fillna(0)
arizona['Number of Workers']=arizona['Number of Workers'].fillna(0)
california['Number of Workers']=california['Number of Workers'].fillna(0)
colorado['Number of Workers']=colorado['Number of Workers'].fillna(0)
connecticut['Number of Workers']=connecticut['Number of Workers'].fillna(0)
indiana['Number of Workers']=indiana['Number of Workers'].fillna(0)
kansas['Number of Workers']=kansas['Number of Workers'].fillna(0)
kentucky['Number of Workers']=kentucky['Number of Workers'].fillna(0)
maryland['Number of Workers']=maryland['Number of Workers'].fillna(0)
michigan['Number of Workers']=michigan['Number of Workers'].fillna(0)
missouri['Number of Workers']=missouri['Number of Workers'].fillna(0)
new_jersey['Number of Workers']=new_jersey['Number of Workers'].fillna(0)
new_york['Number of Workers']=new_york['Number of Workers'].fillna(0)
ohio['Number of Workers']=ohio['Number of Workers'].fillna(0)
pennsylvania['Number of Workers']=pennsylvania['Number of Workers'].fillna(0)
texas['Number of Workers']=texas['Number of Workers'].fillna(0)


# In[7]:


colorado['Number of Workers'].unique()


# In[8]:


colorado['Number of Workers']=colorado['Number of Workers'].replace(' ',0)
colorado['Number of Workers']=colorado['Number of Workers'].replace('  ',0)


# In[9]:


albama['Number of Workers'] = albama['Number of Workers'].astype(int)
arizona['Number of Workers']=arizona['Number of Workers'].astype(int)
california['Number of Workers']=california['Number of Workers'].astype(int)
colorado['Number of Workers']=colorado['Number of Workers'].astype(int)
connecticut['Number of Workers']=connecticut['Number of Workers'].astype(int)
indiana['Number of Workers']=indiana['Number of Workers'].astype(int)
kansas['Number of Workers']=kansas['Number of Workers'].astype(int)
kentucky['Number of Workers']=kentucky['Number of Workers'].astype(int)
maryland['Number of Workers']=maryland['Number of Workers'].astype(int)
michigan['Number of Workers']=michigan['Number of Workers'].astype(int)
missouri['Number of Workers']=missouri['Number of Workers'].astype(int)
new_jersey['Number of Workers']=new_jersey['Number of Workers'].astype(int)
new_york['Number of Workers']=new_york['Number of Workers'].astype(int)
ohio['Number of Workers']=ohio['Number of Workers'].astype(int)
pennsylvania['Number of Workers']=pennsylvania['Number of Workers'].astype(int)
texas['Number of Workers']=texas['Number of Workers'].astype(int)


# In[10]:


print("Albama:        ",albama['Number of Workers'].dtypes)
print("Arizona:       ",arizona['Number of Workers'].dtypes)
print("California:    ",california['Number of Workers'].dtypes)
print("Colorado:      ",colorado['Number of Workers'].dtypes)
print("Connecticut:   ",connecticut['Number of Workers'].dtypes)
print("Florida:       ",florida['Number of Workers'].dtypes)
print("Georgia:       ",georgia['Number of Workers'].dtypes)
print("Indiana:       ",indiana['Number of Workers'].dtypes)
print("Kansas:        ",kansas['Number of Workers'].dtypes)
print("Kentucky:      ",kentucky['Number of Workers'].dtypes)
print("Maryland:      ",maryland['Number of Workers'].dtypes)
print("Michigan:      ",michigan['Number of Workers'].dtypes)
print("Missouri:      ",missouri['Number of Workers'].dtypes)
print("New Jersey:    ",new_jersey['Number of Workers'].dtypes)
print("New York:      ",new_york['Number of Workers'].dtypes)
print("Ohio:          ",ohio['Number of Workers'].dtypes)
print("Pennsylvania:  ",pennsylvania['Number of Workers'].dtypes)
print("Texas:         ",texas['Number of Workers'].dtypes)
print("Virginia:      ",virginia['Number of Workers'].dtypes)
print("Washington:    ",washington['Number of Workers'].dtypes)


# In[11]:


print("Albama:        ",albama['State'].dtypes)
print("Arizona:       ",arizona['State'].dtypes)
print("California:    ",california['State'].dtypes)
print("Colorado:      ",colorado['State'].dtypes)
print("Connecticut:   ",connecticut['State'].dtypes)
print("Florida:       ",florida['State'].dtypes)
print("Georgia:       ",georgia['State'].dtypes)
print("Indiana:       ",indiana['State'].dtypes)
print("Kansas:        ",kansas['State'].dtypes)
print("Kentucky:      ",kentucky['State'].dtypes)
print("Maryland:      ",maryland['State'].dtypes)
print("Michigan:      ",michigan['State'].dtypes)
print("Missouri:      ",missouri['State'].dtypes)
print("New Jersey:    ",new_jersey['State'].dtypes)
print("New York:      ",new_york['State'].dtypes)
print("Ohio:          ",ohio['State'].dtypes)
print("Pennsylvania:  ",pennsylvania['State'].dtypes)
print("Texas:         ",texas['State'].dtypes)
print("Virginia:      ",virginia['State'].dtypes)
print("Washington:    ",washington['State'].dtypes)


# In[12]:


print("Albama:        ",albama['Company'].dtypes)
print("Arizona:       ",arizona['Company'].dtypes)
print("California:    ",california['Company'].dtypes)
print("Colorado:      ",colorado['Company'].dtypes)
print("Connecticut:   ",connecticut['Company'].dtypes)
print("Florida:       ",florida['Company'].dtypes)
print("Georgia:       ",georgia['Company'].dtypes)
print("Indiana:       ",indiana['Company'].dtypes)
print("Kansas:        ",kansas['Company'].dtypes)
print("Kentucky:      ",kentucky['Company'].dtypes)
print("Maryland:      ",maryland['Company'].dtypes)
print("Michigan:      ",michigan['Company'].dtypes)
print("Missouri:      ",missouri['Company'].dtypes)
print("New Jersey:    ",new_jersey['Company'].dtypes)
print("New York:      ",new_york['Company'].dtypes)
print("Ohio:          ",ohio['Company'].dtypes)
print("Pennsylvania:  ",pennsylvania['Company'].dtypes)
print("Texas:         ",texas['Company'].dtypes)
print("Virginia:      ",virginia['Company'].dtypes)
print("Washington:    ",washington['Company'].dtypes)


# In[13]:


california.rename(columns = {'Address':'City'}, inplace = True) 


# In[14]:


colorado['City']=colorado['City'].fillna('none')


# In[15]:


print("Albama:        ",albama['City'].dtypes)
print("Arizona:       ",arizona['City'].dtypes)
print("California:    ",california['City'].dtypes)
print("Colorado:      ",colorado['City'].dtypes)
print("Connecticut:   ",connecticut['City'].dtypes)
print("Florida:       ",florida['City'].dtypes)
print("Georgia:       ",georgia['City'].dtypes)
print("Indiana:       ",indiana['City'].dtypes)
print("Kansas:        ",kansas['City'].dtypes)
print("Kentucky:      ",kentucky['City'].dtypes)
print("Maryland:      ",maryland['City'].dtypes)
print("Michigan:      ",michigan['City'].dtypes)
print("Missouri:      ",missouri['City'].dtypes)
print("New Jersey:    ",new_jersey['City'].dtypes)
print("New York:      ",new_york['City'].dtypes)
print("Ohio:          ",ohio['City'].dtypes)
print("Pennsylvania:  ",pennsylvania['City'].dtypes)
print("Texas:         ",texas['City'].dtypes)
print("Virginia:      ",virginia['City'].dtypes)
print("Washington:    ",washington['City'].dtypes)


# In[16]:


california.rename(columns={'Received Date':'WARN Received Date'},inplace=True)


# In[17]:


print("Albama:        ",albama['WARN Received Date'].dtypes)
print("Arizona:       ",arizona['WARN Received Date'].dtypes)
print("California:    ",california['WARN Received Date'].dtypes)
print("Colorado:      ",colorado['WARN Received Date'].dtypes)
print("Connecticut:   ",connecticut['WARN Received Date'].dtypes)
print("Florida:       ",florida['WARN Received Date'].dtypes)
print("Georgia:       ",georgia['WARN Received Date'].dtypes)
print("Indiana:       ",indiana['WARN Received Date'].dtypes)
print("Kansas:        ",kansas['WARN Received Date'].dtypes)
print("Kentucky:      ",kentucky['WARN Received Date'].dtypes)
print("Maryland:      ",maryland['WARN Received Date'].dtypes)
print("Michigan:      ",michigan['WARN Received Date'].dtypes)
print("Missouri:      ",missouri['WARN Received Date'].dtypes)
print("New Jersey:    ",new_jersey['WARN Received Date'].dtypes)
print("New York:      ",new_york['WARN Received Date'].dtypes)
print("Ohio:          ",ohio['WARN Received Date'].dtypes)
print("Pennsylvania:  ",pennsylvania['WARN Received Date'].dtypes)
print("Texas:         ",texas['WARN Received Date'].dtypes)
print("Virginia:      ",virginia['WARN Received Date'].dtypes)
print("Washington:    ",washington['WARN Received Date'].dtypes)


# In[18]:


arizona['Effective Date']=arizona['Effective Date'].fillna(0)
colorado['Effective Date']=colorado['Effective Date'].fillna(0)
connecticut['Effective Date']=connecticut['Effective Date'].fillna(0)
florida['Effective Date']=florida['Effective Date'].fillna(0)
georgia['Effective Date']=georgia['Effective Date'].fillna(0)
indiana['Effective Date']=indiana['Effective Date'].fillna(0)


kansas['Effective Date']=kansas['Effective Date'].fillna(0)
kentucky['Effective Date']=kentucky['Effective Date'].fillna(0)
maryland['Effective Date']=maryland['Effective Date'].fillna(0)
michigan['Effective Date']=michigan['Effective Date'].fillna(0)
missouri['Effective Date']=missouri['Effective Date'].fillna(0)
new_jersey['Effective Date']=new_jersey['Effective Date'].fillna(0)

new_york['Effective Date']=new_york['Effective Date'].fillna(0)
ohio['Effective Date']=ohio['Effective Date'].fillna(0)
pennsylvania['Effective Date']=pennsylvania['Effective Date'].fillna(0)


# In[19]:


arizona=arizona[~(arizona['Effective Date']=='12/19/2009-01/31/2010')]
arizona=arizona[~(arizona['Effective Date']=='08/13/2009-12/31/2009')]
arizona=arizona[~(arizona['Effective Date']=='05/29/2009 07/31/2009')]
arizona=arizona[~(arizona['Effective Date']=='10/11/2008-08/11/2009')]
arizona=arizona[~(arizona['Effective Date']=='01/03/2010-01/17/2010')]
arizona=arizona[~(arizona['Effective Date']=='05/30/2009-06/13/2009')]
arizona=arizona[~(arizona['Effective Date']=='05/13/2009-08/11/2009')]


# In[20]:


colorado['Effective Date'].unique()


# In[21]:


# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'
# colorado.loc[colorado['Effective Date']=='12/29/2023-1/11/2023','Effective Date']='12/29/2023'
# colorado.loc[colorado['Effective Date']=='11/20/20-11/30/290','Effective Date']='11/20/20'
# colorado.loc[colorado['Effective Date']=='3/20/20-2/28/21','Effective Date']='3/20/20'
# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'
# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'
# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'
# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'
# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'
# colorado.loc[colorado['Effective Date']=='1/1/2024-1/31/2024','Effective Date']='1/1/2024'


# In[22]:


# colorado=colorado[~(colorado['Effective Date']=='1/1/2024-1/31/2024')]
# colorado=colorado[~(colorado['Effective Date']=='12/29/2023-1/11/2023')]
# colorado=colorado[~(colorado['Effective Date']=='11/20/20-11/30/290')]
# colorado=colorado[~(colorado['Effective Date']=='3/20/20-2/28/21')]
# colorado=colorado[~(colorado['Effective Date']=='Unknown')]
# colorado=colorado[~(colorado['Effective Date']=='10/30/20 & 11/30/20')]
# colorado=colorado[~(colorado['Effective Date']=='10/1/20 to 10/4/20')]
# colorado=colorado[~(colorado['Effective Date']=='5/26/20-July/22/20')]
# colorado=colorado[~(colorado['Effective Date']=='7/18/20-8/11/20')]

# colorado=colorado[~(colorado['Effective Date']=='6/17/2020 - 7/1/2020')]
# colorado=colorado[~(colorado['Effective Date']=='7/1/20 & 10/1/30')]
# colorado=colorado[~(colorado['Effective Date']=='7/24/20 & 8/28/20')]
# colorado=colorado[~(colorado['Effective Date']=='5/22/20, 5/26/20, 5/29/20')]

# colorado=colorado[~(colorado['Effective Date']=='5/9/20 & 5/14/20, 5/15/20')]
# colorado=colorado[~(colorado['Effective Date']=='Not available')]
# colorado=colorado[~(colorado['Effective Date']=='4/24/20 & 5/31/20')]
# colorado=colorado[~(colorado['Effective Date']=='4/8/20 - 5/1/20')]
                    

                    
# colorado=colorado[~(colorado['Effective Date']=='4/6/20-5/23/20')]
# colorado=colorado[~(colorado['Effective Date']=='3/24/20, 3/26/20 & 3/30/20')]
# colorado=colorado[~(colorado['Effective Date']=='6/26/20 & 12/29/20')]
# colorado=colorado[~(colorado['Effective Date']=='3/19/20-4/1/20')]
 

                    
# colorado=colorado[~(colorado['Effective Date']=='3/17/20 - 4/2/20')]
# colorado=colorado[~(colorado['Effective Date']=="4/30/20, 5/29/20 and 7/31/20', '3/13/20 through 4/24/20','Downsize 1/26/20', '3/24/20- 4/7/20 in phases','12/31/19 (for 265) Not specified for 191")]
# colorado=colorado[~(colorado['Effective Date']=="Closure 1/10/20- 04/10/20','1/1/20 to 1/14/20'")]
# colorado=colorado[~(colorado['Effective Date']=="10/30/2019, 11/8/2019, 11/22/2019, 11/29/2019")]


# colorado=colorado[~(colorado['Effective Date']=='11/20/20-11/30/20')]
# colorado=colorado[~(colorado['Effective Date']=="9/14/20- 54 employees; 10/31/20, 9 employees, 1-31-2021 - 1 employee','6/5/20 to 6/22/20")]
# colorado=colorado[~(colorado['Effective Date']=="5/1/2020 - 5/17/2020','6/26/2020, 6/30/2020")]
# colorado=colorado[~(colorado['Effective Date']=="6/10/20, 6/17/20, 6/22/20, 6/26/20")]

                    
                                        
# colorado=colorado[~(colorado['Effective Date']=='4/14/20 & 4/20/20')]
# colorado=colorado[~(colorado['Effective Date']=='4/13/20-4/27/20')]
# colorado=colorado[~(colorado['Effective Date']=="3/20/20, 3/24/20, & 3/26/20")]
# colorado=colorado[~(colorado['Effective Date']=="3/23/20, 3/24/20, & 3/26/20")]

                    
# colorado=colorado[~(colorado['Effective Date']=="3/23/20, 3/24/20, & 3/26/20','4/1/20-4/30/20 for hourly workers and May 2020 for salaried associates")]
# colorado=colorado[~(colorado['Effective Date']=="3/16/20-3/20/20 and 3/21/20-3/31/20','3/19/20 to 4/20/20, closing 3/19/20")]
# colorado=colorado[~(colorado['Effective Date']=="4/30/20, 5/29/20 and 7/31/20', '3/13/20 through 4/24/20','Downsize 1/26/20', '3/24/20- 4/7/20 in phases','12/31/19 (for 265) Not specified for 191")]
# colorado=colorado[~(colorado['Effective Date']=="Closure 1/10/20- 04/10/20','1/1/20 to 1/14/20")]


# colorado=colorado[~(colorado['Effective Date']=='12/31/19 to 3/26/20')]
# colorado=colorado[~(colorado['Effective Date']=='11/25/19 - 9/30/20')]
# colorado=colorado[~(colorado['Effective Date']=="10/18/19-12/31/19','10/5/19-12/31/19")]
# colorado=colorado[~(colorado['Effective Date']=="9/7/19 - 12/31/19','7/6/19 - 7/31/19', '8/2/19 - 3/31/20")]


# colorado=colorado[~(colorado['Effective Date']=="3/25/19, 4/24/19, 5/24/19','5/25/19 (thru 18 mo following)', '5/18/19 - 6/1/19")]
# colorado=colorado[~(colorado['Effective Date']=="4/13/19 - 5/19/19','5/24/19 - 3/20/20")]
# colorado=colorado[~(colorado['Effective Date']=='4/13/19-5/30/19')]
# colorado=colorado[~(colorado['Effective Date']=='3/10/19  (184) & 5/31/19  (19)')]

# colorado=colorado[~(colorado['Effective Date']=='3/3/19, 3/31/19')]




# colorado=colorado[~(colorado['Effective Date']=="4/30/20, 5/29/20 and 7/31/20', '3/13/20 through 4/24/20")]
# colorado=colorado[~(colorado['Effective Date']=='3/3/19, 3/31/19')]
# colorado=colorado[~(colorado['Effective Date']=='3/3/19, 3/31/19')]
# colorado=colorado[~(colorado['Effective Date']=='3/3/19, 3/31/19')]
# colorado=colorado[~(colorado['Effective Date']=='3/3/19, 3/31/19')]





# colorado=colorado[~(colorado['Effective Date']=="9/14/20- 54 employees; 10/31/20, 9 employees, 1-31-2021 - 1 employee','6/5/20 to 6/22/20")]
# colorado=colorado[~(colorado['Effective Date']=="5/1/2020 - 5/17/2020','6/26/2020, 6/30/2020")]
# colorado=colorado[~(colorado['Effective Date']=='4/1/20-4/30/20 for hourly workers and May 2020 for salaried associates')]
# colorado=colorado[~(colorado['Effective Date']=="3/16/20-3/20/20 and 3/21/20-3/31/20','3/19/20 to 4/20/20, closing 3/19/20")]


# colorado=colorado[~(colorado['Effective Date']=="4/30/20, 5/29/20 and 7/31/20', '3/13/20 through 4/24/20','Downsize 1/26/20', '3/24/20- 4/7/20 in phases','12/31/19 (for 265) Not specified for 191")]
# colorado=colorado[~(colorado['Effective Date']=="Closure 1/10/20- 04/10/20','1/1/20 to 1/14/20")]
# colorado=colorado[~(colorado['Effective Date']=='11/29/19 - 1/31/2020')]
# colorado=colorado[~(colorado['Effective Date']=="10/18/19-12/31/19','10/5/19-12/31/19")]

# colorado=colorado[~(colorado['Effective Date']=="9/7/19 - 12/31/19','7/6/19 - 7/31/19', '8/2/19 - 3/31/20")]


# In[23]:


# arizona['Effective Date']= pd.to_datetime(arizona['Effective Date'])
# colorado['Effective Date']= pd.to_datetime(colorado['Effective Date'])
# connecticut['Effective Date']= pd.to_datetime(connecticut['Effective Date'])
# florida['Effective Date']= pd.to_datetime(florida['Effective Date'])
# georgia['Effective Date']= pd.to_datetime(georgia['Effective Date'])
# indiana['Effective Date']= pd.to_datetime(indiana['Effective Date'])


# kansas['Effective Date']= pd.to_datetime(kansas['Effective Date'])
# kentucky['Effective Date']= pd.to_datetime(kentucky['Effective Date'])
# maryland['Effective Date']= pd.to_datetime(maryland['Effective Date'])
# michigan['Effective Date']= pd.to_datetime(michigan['Effective Date'])
# missouri['Effective Date']= pd.to_datetime(missouri['Effective Date'])
# new_jersey['Effective Date']= pd.to_datetime(new_jersey['Effective Date'])

# new_york['Effective Date']= pd.to_datetime(new_york['Effective Date'])
# ohio['Effective Date']= pd.to_datetime(ohio['Effective Date'])
# pennsylvania['Effective Date']= pd.to_datetime(pennsylvania['Effective Date'])


# In[24]:


albama['Effective Date'] = albama['Effective Date'].astype(str)
arizona['Effective Date']=arizona['Effective Date'].astype(str)
california['Effective Date']=california['Effective Date'].astype(str)
colorado['Effective Date']=colorado['Effective Date'].astype(str)
connecticut['Effective Date']=connecticut['Effective Date'].astype(str)
indiana['Effective Date']=indiana['Effective Date'].astype(str)
kansas['Effective Date']=kansas['Effective Date'].astype(str)
kentucky['Effective Date']=kentucky['Effective Date'].astype(str)
maryland['Effective Date']=maryland['Effective Date'].astype(str)
michigan['Effective Date']=michigan['Effective Date'].astype(str)
missouri['Effective Date']=missouri['Effective Date'].astype(str)
new_jersey['Effective Date']=new_jersey['Effective Date'].astype(str)
new_york['Effective Date']=new_york['Effective Date'].astype(str)
ohio['Effective Date']=ohio['Effective Date'].astype(str)
pennsylvania['Effective Date']=pennsylvania['Effective Date'].astype(str)
texas['Effective Date']=texas['Effective Date'].astype(str)
virginia['Effective Date']=virginia['Effective Date'].astype(str)
washington['Effective Date']=washington['Effective Date'].astype(str)


# In[25]:


print("Albama:        ",albama['Effective Date'].dtypes)
print("Arizona:       ",arizona['Effective Date'].dtypes)
print("California:    ",california['Effective Date'].dtypes)
print("Colorado:      ",colorado['Effective Date'].dtypes)
print("Connecticut:   ",connecticut['Effective Date'].dtypes)
print("Florida:       ",florida['Effective Date'].dtypes)
print("Georgia:       ",georgia['Effective Date'].dtypes)
print("Indiana:       ",indiana['Effective Date'].dtypes)
print("Kansas:        ",kansas['Effective Date'].dtypes)
print("Kentucky:      ",kentucky['Effective Date'].dtypes)
print("Maryland:      ",maryland['Effective Date'].dtypes)
print("Michigan:      ",michigan['Effective Date'].dtypes)
print("Missouri:      ",missouri['Effective Date'].dtypes)
print("New Jersey:    ",new_jersey['Effective Date'].dtypes)
print("New York:      ",new_york['Effective Date'].dtypes)
print("Ohio:          ",ohio['Effective Date'].dtypes)
print("Pennsylvania:  ",pennsylvania['Effective Date'].dtypes)
print("Texas:         ",texas['Effective Date'].dtypes)
print("Virginia:      ",virginia['Effective Date'].dtypes)
print("Washington:    ",washington['Effective Date'].dtypes)


# In[26]:


albama.rename(columns={'Closure / Layoff':'Closure/Layoff'},inplace=True)
california.rename(columns={'Layoff/Closure':'Closure/Layoff'},inplace=True)


# In[27]:


albama['Closure/Layoff'] = albama['Closure/Layoff'].fillna(0)
arizona['Closure/Layoff']=arizona['Closure/Layoff'].fillna(0)
california['Closure/Layoff']=california['Closure/Layoff'].fillna(0)
colorado['Closure/Layoff']=colorado['Closure/Layoff'].fillna(0)
connecticut['Closure/Layoff']=connecticut['Closure/Layoff'].fillna(0)

florida['Closure/Layoff']=florida['Closure/Layoff'].fillna(0)
georgia['Closure/Layoff']=georgia['Closure/Layoff'].fillna(0)
indiana['Closure/Layoff']=indiana['Closure/Layoff'].fillna(0)
kansas['Closure/Layoff']=kansas['Closure/Layoff'].fillna(0)
kentucky['Closure/Layoff']=kentucky['Closure/Layoff'].fillna(0)
maryland['Closure/Layoff']=maryland['Closure/Layoff'].fillna(0)
michigan['Closure/Layoff']=michigan['Closure/Layoff'].fillna(0)
missouri['Closure/Layoff']=missouri['Closure/Layoff'].fillna(0)
new_jersey['Closure/Layoff']=new_jersey['Closure/Layoff'].fillna(0)
new_york['Closure/Layoff']=new_york['Closure/Layoff'].fillna(0)
ohio['Closure/Layoff']=ohio['Closure/Layoff'].fillna(0)
pennsylvania['Closure/Layoff']=pennsylvania['Closure/Layoff'].fillna(0)
texas['Closure/Layoff']=texas['Closure/Layoff'].fillna(0)
virginia['Closure/Layoff']=virginia['Closure/Layoff'].fillna(0)
washington['Closure/Layoff']=washington['Closure/Layoff'].fillna(0)


# In[28]:


albama['Closure/Layoff'] = albama['Closure/Layoff'].astype(str)
arizona['Closure/Layoff']=arizona['Closure/Layoff'].astype(str)
california['Closure/Layoff']=california['Closure/Layoff'].astype(str)
colorado['Closure/Layoff']=colorado['Closure/Layoff'].astype(str)
connecticut['Closure/Layoff']=connecticut['Closure/Layoff'].astype(str)

florida['Closure/Layoff']=florida['Closure/Layoff'].astype(str)
georgia['Closure/Layoff']=georgia['Closure/Layoff'].astype(str)
indiana['Closure/Layoff']=indiana['Closure/Layoff'].astype(str)
kansas['Closure/Layoff']=kansas['Closure/Layoff'].astype(str)
kentucky['Closure/Layoff']=kentucky['Closure/Layoff'].astype(str)
maryland['Closure/Layoff']=maryland['Closure/Layoff'].astype(str)
michigan['Closure/Layoff']=michigan['Closure/Layoff'].astype(str)
missouri['Closure/Layoff']=missouri['Closure/Layoff'].astype(str)
new_jersey['Closure/Layoff']=new_jersey['Closure/Layoff'].astype(str)
new_york['Closure/Layoff']=new_york['Closure/Layoff'].astype(str)
ohio['Closure/Layoff']=ohio['Closure/Layoff'].astype(str)
pennsylvania['Closure/Layoff']=pennsylvania['Closure/Layoff'].astype(str)
texas['Closure/Layoff']=texas['Closure/Layoff'].astype(str)
virginia['Closure/Layoff']=virginia['Closure/Layoff'].astype(str)
washington['Closure/Layoff']=washington['Closure/Layoff'].astype(str)


# In[29]:


print("Albama:        ",albama['Closure/Layoff'].dtypes)
print("Arizona:       ",arizona['Closure/Layoff'].dtypes)
print("California:    ",california['Closure/Layoff'].dtypes)
print("Colorado:      ",colorado['Closure/Layoff'].dtypes)
print("Connecticut:   ",connecticut['Closure/Layoff'].dtypes)
print("Florida:       ",florida['Closure/Layoff'].dtypes)
print("Georgia:       ",georgia['Closure/Layoff'].dtypes)
print("Indiana:       ",indiana['Closure/Layoff'].dtypes)
print("Kansas:        ",kansas['Closure/Layoff'].dtypes)
print("Kentucky:      ",kentucky['Closure/Layoff'].dtypes)
print("Maryland:      ",maryland['Closure/Layoff'].dtypes)
print("Michigan:      ",michigan['Closure/Layoff'].dtypes)
print("Missouri:      ",missouri['Closure/Layoff'].dtypes)
print("New Jersey:    ",new_jersey['Closure/Layoff'].dtypes)
print("New York:      ",new_york['Closure/Layoff'].dtypes)
print("Ohio:          ",ohio['Closure/Layoff'].dtypes)
print("Pennsylvania:  ",pennsylvania['Closure/Layoff'].dtypes)
print("Texas:         ",texas['Closure/Layoff'].dtypes)
print("Virginia:      ",virginia['Closure/Layoff'].dtypes)
print("Washington:    ",washington['Closure/Layoff'].dtypes)


# In[30]:


albama['Temporary/Permanent'] = albama['Temporary/Permanent'].astype(str)
arizona['Temporary/Permanent']=arizona['Temporary/Permanent'].astype(str)
california['Temporary/Permanent']=california['Temporary/Permanent'].astype(str)
colorado['Temporary/Permanent']=colorado['Temporary/Permanent'].astype(str)
connecticut['Temporary/Permanent']=connecticut['Temporary/Permanent'].astype(str)
florida['Temporary/Permanent']=florida['Temporary/Permanent'].astype(str)
georgia['Temporary/Permanent']=georgia['Temporary/Permanent'].astype(str)
indiana['Temporary/Permanent']=indiana['Temporary/Permanent'].astype(str)
kansas['Temporary/Permanent']=kansas['Temporary/Permanent'].astype(str)
kentucky['Temporary/Permanent']=kentucky['Temporary/Permanent'].astype(str)
maryland['Temporary/Permanent']=maryland['Temporary/Permanent'].astype(str)
michigan['Temporary/Permanent']=michigan['Temporary/Permanent'].astype(str)
missouri['Temporary/Permanent']=missouri['Temporary/Permanent'].astype(str)
new_jersey['Temporary/Permanent']=new_jersey['Temporary/Permanent'].astype(str)
new_york['Temporary/Permanent']=new_york['Temporary/Permanent'].astype(str)
ohio['Temporary/Permanent']=ohio['Temporary/Permanent'].astype(str)
pennsylvania['Temporary/Permanent']=pennsylvania['Temporary/Permanent'].astype(str)
texas['Temporary/Permanent']=texas['Temporary/Permanent'].astype(str)
virginia['Temporary/Permanent']=virginia['Temporary/Permanent'].astype(str)
washington['Temporary/Permanent']=washington['Temporary/Permanent'].astype(str)


# In[31]:


print("Albama:        ",albama['Temporary/Permanent'].dtypes)
print("Arizona:       ",arizona['Temporary/Permanent'].dtypes)
print("California:    ",california['Temporary/Permanent'].dtypes)
print("Colorado:      ",colorado['Temporary/Permanent'].dtypes)
print("Connecticut:   ",connecticut['Temporary/Permanent'].dtypes)
print("Florida:       ",florida['Temporary/Permanent'].dtypes)
print("Georgia:       ",georgia['Temporary/Permanent'].dtypes)
print("Indiana:       ",indiana['Temporary/Permanent'].dtypes)
print("Kansas:        ",kansas['Temporary/Permanent'].dtypes)
print("Kentucky:      ",kentucky['Temporary/Permanent'].dtypes)
print("Maryland:      ",maryland['Temporary/Permanent'].dtypes)
print("Michigan:      ",michigan['Temporary/Permanent'].dtypes)
print("Missouri:      ",missouri['Temporary/Permanent'].dtypes)
print("New Jersey:    ",new_jersey['Temporary/Permanent'].dtypes)
print("New York:      ",new_york['Temporary/Permanent'].dtypes)
print("Ohio:          ",ohio['Temporary/Permanent'].dtypes)
print("Pennsylvania:  ",pennsylvania['Temporary/Permanent'].dtypes)
print("Texas:         ",texas['Temporary/Permanent'].dtypes)
print("Virginia:      ",virginia['Temporary/Permanent'].dtypes)
print("Washington:    ",washington['Temporary/Permanent'].dtypes)


# In[32]:


albama['Union'].unique()


# In[33]:


albama['Union'] = albama['Union'].astype(str)
arizona['Union']=arizona['Union'].astype(str)
california['Union']=california['Union'].astype(str)
colorado['Union']=colorado['Union'].astype(str)
connecticut['Union']=connecticut['Union'].astype(str)
florida['Union']=florida['Union'].astype(str)
georgia['Union']=georgia['Union'].astype(str)
indiana['Union']=indiana['Union'].astype(str)
kansas['Union']=kansas['Union'].astype(str)
kentucky['Union']=kentucky['Union'].astype(str)
maryland['Union']=maryland['Union'].astype(str)
michigan['Union']=michigan['Union'].astype(str)
missouri['Union']=missouri['Union'].astype(str)
new_jersey['Union']=new_jersey['Union'].astype(str)
new_york['Union']=new_york['Union'].astype(str)
ohio['Union']=ohio['Union'].astype(str)
pennsylvania['Union']=pennsylvania['Union'].astype(str)
texas['Union']=texas['Union'].astype(str)
virginia['Union']=virginia['Union'].astype(str)
washington['Union']=washington['Union'].astype(str)


# In[34]:


print("Albama:        ",albama['Union'].dtypes)
print("Arizona:       ",arizona['Union'].dtypes)
print("California:    ",california['Union'].dtypes)
print("Colorado:      ",colorado['Union'].dtypes)
print("Connecticut:   ",connecticut['Union'].dtypes)
print("Florida:       ",florida['Union'].dtypes)
print("Georgia:       ",georgia['Union'].dtypes)
print("Indiana:       ",indiana['Union'].dtypes)
print("Kansas:        ",kansas['Union'].dtypes)
print("Kentucky:      ",kentucky['Union'].dtypes)
print("Maryland:      ",maryland['Union'].dtypes)
print("Michigan:      ",michigan['Union'].dtypes)
print("Missouri:      ",missouri['Union'].dtypes)
print("New Jersey:    ",new_jersey['Union'].dtypes)
print("New York:      ",new_york['Union'].dtypes)
print("Ohio:          ",ohio['Union'].dtypes)
print("Pennsylvania:  ",pennsylvania['Union'].dtypes)
print("Texas:         ",texas['Union'].dtypes)
print("Virginia:      ",virginia['Union'].dtypes)
print("Washington:    ",washington['Union'].dtypes)


# In[35]:


albama['Region'] = albama['Region'].astype(str)
arizona['Region']=arizona['Region'].astype(str)
california['Region']=california['Region'].astype(str)
colorado['Region']=colorado['Region'].astype(str)
connecticut['Region']=connecticut['Region'].astype(str)
florida['Region']=florida['Region'].astype(str)
georgia['Region']=georgia['Region'].astype(str)
indiana['Region']=indiana['Region'].astype(str)
kansas['Region']=kansas['Region'].astype(str)
kentucky['Region']=kentucky['Region'].astype(str)
maryland['Region']=maryland['Region'].astype(str)
michigan['Region']=michigan['Region'].astype(str)
missouri['Region']=missouri['Region'].astype(str)
new_jersey['Region']=new_jersey['Region'].astype(str)
new_york['Region']=new_york['Region'].astype(str)
ohio['Region']=ohio['Region'].astype(str)
pennsylvania['Region']=pennsylvania['Region'].astype(str)
texas['Region']=texas['Region'].astype(str)
virginia['Region']=virginia['Region'].astype(str)
washington['Region']=washington['Region'].astype(str)


# In[36]:


print("Albama:        ",albama['Region'].dtypes)
print("Arizona:       ",arizona['Region'].dtypes)
print("California:    ",california['Region'].dtypes)
print("Colorado:      ",colorado['Region'].dtypes)
print("Connecticut:   ",connecticut['Region'].dtypes)
print("Florida:       ",florida['Region'].dtypes)
print("Georgia:       ",georgia['Region'].dtypes)
print("Indiana:       ",indiana['Region'].dtypes)
print("Kansas:        ",kansas['Region'].dtypes)
print("Kentucky:      ",kentucky['Region'].dtypes)
print("Maryland:      ",maryland['Region'].dtypes)
print("Michigan:      ",michigan['Region'].dtypes)
print("Missouri:      ",missouri['Region'].dtypes)
print("New Jersey:    ",new_jersey['Region'].dtypes)
print("New York:      ",new_york['Region'].dtypes)
print("Ohio:          ",ohio['Region'].dtypes)
print("Pennsylvania:  ",pennsylvania['Region'].dtypes)
print("Texas:         ",texas['Region'].dtypes)
print("Virginia:      ",virginia['Region'].dtypes)
print("Washington:    ",washington['Region'].dtypes)


# In[37]:


albama['County'] = albama['County'].astype(str)
arizona['County']=arizona['County'].astype(str)
california['County']=california['County'].astype(str)
colorado['County']=colorado['County'].astype(str)
connecticut['County']=connecticut['County'].astype(str)
florida['County']=florida['County'].astype(str)
georgia['County']=georgia['County'].astype(str)
indiana['County']=indiana['County'].astype(str)
kansas['County']=kansas['County'].astype(str)
kentucky['County']=kentucky['County'].astype(str)
maryland['County']=maryland['County'].astype(str)
michigan['County']=michigan['County'].astype(str)
missouri['County']=missouri['County'].astype(str)
new_jersey['County']=new_jersey['County'].astype(str)
new_york['County']=new_york['County'].astype(str)
ohio['County']=ohio['County'].astype(str)
pennsylvania['County']=pennsylvania['County'].astype(str)
texas['County']=texas['County'].astype(str)
virginia['County']=virginia['County'].astype(str)
washington['County']=washington['County'].astype(str)


# In[38]:


print("Albama:        ",albama['County'].dtypes)
print("Arizona:       ",arizona['County'].dtypes)
print("California:    ",california['County'].dtypes)
print("Colorado:      ",colorado['County'].dtypes)
print("Connecticut:   ",connecticut['County'].dtypes)
print("Florida:       ",florida['County'].dtypes)
print("Georgia:       ",georgia['County'].dtypes)
print("Indiana:       ",indiana['County'].dtypes)
print("Kansas:        ",kansas['County'].dtypes)
print("Kentucky:      ",kentucky['County'].dtypes)
print("Maryland:      ",maryland['County'].dtypes)
print("Michigan:      ",michigan['County'].dtypes)
print("Missouri:      ",missouri['County'].dtypes)
print("New Jersey:    ",new_jersey['County'].dtypes)
print("New York:      ",new_york['County'].dtypes)
print("Ohio:          ",ohio['County'].dtypes)
print("Pennsylvania:  ",pennsylvania['County'].dtypes)
print("Texas:         ",texas['County'].dtypes)
print("Virginia:      ",virginia['County'].dtypes)
print("Washington:    ",washington['County'].dtypes)


# In[39]:


albama['Industry'] = albama['Industry'].astype(str)
arizona['Industry']=arizona['Industry'].astype(str)
california['Industry']=california['Industry'].astype(str)
colorado['Industry']=colorado['Industry'].astype(str)
connecticut['Industry']=connecticut['Industry'].astype(str)
florida['Industry']=florida['Industry'].astype(str)
georgia['Industry']=georgia['Industry'].astype(str)
indiana['Industry']=indiana['Industry'].astype(str)
kansas['Industry']=kansas['Industry'].astype(str)
kentucky['Industry']=kentucky['Industry'].astype(str)
maryland['Industry']=maryland['Industry'].astype(str)
michigan['Industry']=michigan['Industry'].astype(str)
missouri['Industry']=missouri['Industry'].astype(str)
new_jersey['Industry']=new_jersey['Industry'].astype(str)
new_york['Industry']=new_york['Industry'].astype(str)
ohio['Industry']=ohio['Industry'].astype(str)
pennsylvania['Industry']=pennsylvania['Industry'].astype(str)
texas['Industry']=texas['Industry'].astype(str)
virginia['Industry']=virginia['Industry'].astype(str)
washington['Industry']=washington['Industry'].astype(str)


# In[40]:


print("Albama:        ",albama['Industry'].dtypes)
print("Arizona:       ",arizona['Industry'].dtypes)
print("California:    ",california['Industry'].dtypes)
print("Colorado:      ",colorado['Industry'].dtypes)
print("Connecticut:   ",connecticut['Industry'].dtypes)
print("Florida:       ",florida['Industry'].dtypes)
print("Georgia:       ",georgia['Industry'].dtypes)
print("Indiana:       ",indiana['Industry'].dtypes)
print("Kansas:        ",kansas['Industry'].dtypes)
print("Kentucky:      ",kentucky['Industry'].dtypes)
print("Maryland:      ",maryland['Industry'].dtypes)
print("Michigan:      ",michigan['Industry'].dtypes)
print("Missouri:      ",missouri['Industry'].dtypes)
print("New Jersey:    ",new_jersey['Industry'].dtypes)
print("New York:      ",new_york['Industry'].dtypes)
print("Ohio:          ",ohio['Industry'].dtypes)
print("Pennsylvania:  ",pennsylvania['Industry'].dtypes)
print("Texas:         ",texas['Industry'].dtypes)
print("Virginia:      ",virginia['Industry'].dtypes)
print("Washington:    ",washington['Industry'].dtypes)


# In[41]:


albama['Notes'] = albama['Notes'].astype(str)
arizona['Notes']=arizona['Notes'].astype(str)
california['Notes']=california['Notes'].astype(str)
colorado['Notes']=colorado['Notes'].astype(str)
connecticut['Notes']=connecticut['Notes'].astype(str)
florida['Notes']=florida['Notes'].astype(str)
georgia['Notes']=georgia['Notes'].astype(str)
indiana['Notes']=indiana['Notes'].astype(str)
kansas['Notes']=kansas['Notes'].astype(str)
kentucky['Notes']=kentucky['Notes'].astype(str)
maryland['Notes']=maryland['Notes'].astype(str)
michigan['Notes']=michigan['Notes'].astype(str)
missouri['Notes']=missouri['Notes'].astype(str)
new_jersey['Notes']=new_jersey['Notes'].astype(str)
new_york['Notes']=new_york['Notes'].astype(str)
ohio['Notes']=ohio['Notes'].astype(str)
pennsylvania['Notes']=pennsylvania['Notes'].astype(str)
texas['Notes']=texas['Notes'].astype(str)
virginia['Notes']=virginia['Notes'].astype(str)
washington['Notes']=washington['Notes'].astype(str)


# In[42]:


print("Albama:        ",albama['Notes'].dtypes)
print("Arizona:       ",arizona['Notes'].dtypes)
print("California:    ",california['Notes'].dtypes)
print("Colorado:      ",colorado['Notes'].dtypes)
print("Connecticut:   ",connecticut['Notes'].dtypes)
print("Florida:       ",florida['Notes'].dtypes)
print("Georgia:       ",georgia['Notes'].dtypes)
print("Indiana:       ",indiana['Notes'].dtypes)
print("Kansas:        ",kansas['Notes'].dtypes)
print("Kentucky:      ",kentucky['Notes'].dtypes)
print("Maryland:      ",maryland['Notes'].dtypes)
print("Michigan:      ",michigan['Notes'].dtypes)
print("Missouri:      ",missouri['Notes'].dtypes)
print("New Jersey:    ",new_jersey['Notes'].dtypes)
print("New York:      ",new_york['Notes'].dtypes)
print("Ohio:          ",ohio['Notes'].dtypes)
print("Pennsylvania:  ",pennsylvania['Notes'].dtypes)
print("Texas:         ",texas['Notes'].dtypes)
print("Virginia:      ",virginia['Notes'].dtypes)
print("Washington:    ",washington['Notes'].dtypes)


# In[43]:


albama.head()


# In[44]:


final_merged=pd.concat([albama, arizona,california,colorado,connecticut,florida,georgia,indiana,kansas,kentucky,maryland,michigan,missouri,new_jersey,new_york,ohio,pennsylvania,texas,virginia,washington], axis=0)


# In[45]:


final_merged.to_csv(r"/Users/aishwaryathorat/Movies/MS Courses/Sem 1/Data Visualization/20_states.csv")


# In[46]:


final_merged['WARN Received Date'].min()


# In[47]:


final_merged['Union'].unique()


# In[48]:


final_merged['Industry'].unique()


# In[49]:


final_merged['Region'].unique()


# In[50]:


final_merged['Notes'].unique()


# In[51]:


final_merged[final_merged.duplicated(subset=['Company'], keep=False)].sort_values(by='Company')


# In[52]:


final_merged.info()


# In[53]:


final_merged['State'].unique()


# In[54]:


final_merged[final_merged['City']=='nan']


# In[55]:


final_merged['Company'].unique()


# In[56]:


final_merged['Number of Workers'].unique()


# In[57]:


final_merged[final_merged['Closure/Layoff']=='0']


# In[58]:


final_merged['Temporary/Permanent'].value_counts()


# In[59]:


final_merged['Union'].value_counts()


# In[60]:


final_merged['County'].value_counts()


# In[61]:


final_merged['Industry'].value_counts()


# In[65]:


final_merged_1=final_merged[['State','Company','City','Number of Workers','WARN Received Date','Effective Date','Closure/Layoff','Temporary/Permanent','Region','County','Industry']]
final_merged_1


# In[66]:


state_info=final_merged[['State','Company','City','Region','County']]



# In[69]:


state_info_no_duplicates=state_info.drop_duplicates()


# In[70]:


state_info.info()


# In[72]:


state_info['Company'].value_counts()


# In[71]:


Company_info=final_merged[['Company','Number of Workers','WARN Received Date','Effective Date','Closure/Layoff','Temporary/Permanent','Industry']]


# In[73]:


Company_info.info()


# # Connect to MYSQL Server, Create Tables and Upload Data into Tables

# In[93]:


import mysql.connector
import csv
import getpass

try:
    
    password = getpass.getpass("Enter MySQL password: ")
    connection = mysql.connector.connect(
        host='localhost',
        user=input('Enter Username: '),
        password=password  
    )
    print("Connected to MySQL server successfully!")
    
    cursor = connection.cursor()
    
    # Use newly created database
    cursor.execute("use States")


    cursor.execute("""
    create table if not exists state_info (
        company varchar(255),
        state varchar(255),
        city varchar(255),
        region varchar(255),
        county varchar(255),
        primary key (company,state,city)
    )
    """)
    print("state_info table created successfully!")
    
    

    cursor.execute("""
    create table if not exists company_info (
        company varchar(255),
        Number_of_Workers int,
        WARN_Received_Date date,
        Effective_Date varchar(255),
        Closure_Layoff varchar(255),
        Temporary_Permanent varchar(1000),
        Industry varchar(1000),
        primary key (company,WARN_Received_Date)
    )
    """)
    print("company_info table created successfully!")
    
    
    connection.commit()

except mysql.connector.Error as error:
    print("Failed to connect to MySQL server:", error)
finally:
    
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")


# In[95]:


state_info.shape


# In[96]:


state_info_no_dup=state_info.drop_duplicates(subset=['Company','State','City'])


# In[97]:


state_info_no_dup.shape


# In[106]:


state_info_no_dup=state_info_no_dup[~state_info_no_dup['City'].isnull()]


# In[107]:


state_info_no_dup.shape


# In[108]:


state_info_no_dup=state_info_no_dup.drop_duplicates(subset=['Company','State','City'])


# In[109]:


state_info_no_dup.shape


# In[112]:


state_info_no_dup[state_info_no_dup['Company']=='STANDARD FURNITURE']


# In[113]:


# Create a SQLAlchemy engine using the mysql+mysqlconnector dialect
# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your MySQL connection details
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:72314Nov1997#@localhost:3306/States')

# Replace 'table_name' with the name of your table in MySQL
table_name = 'state_info'

# Upload data from DataFrame to MySQL table
state_info_no_dup.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Close the connection
engine.dispose()


# In[115]:


# Create a SQLAlchemy engine using the mysql+mysqlconnector dialect
# Replace 'username', 'password', 'hostname', 'port', and 'database_name' with your MySQL connection details
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:72314Nov1997#@localhost:3306/States')

# Replace 'table_name' with the name of your table in MySQL
table_name = 'company_info'

# Upload data from DataFrame to MySQL table
Company_info.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Close the connection
engine.dispose()


# # Connect to Snowflake and Upload data into tables present in Snowflake

# In[1]:


get_ipython().system('pip install snowflake-connector-python pandas')


# In[2]:


import snowflake.connector
import pandas as pd


# In[1]:


# conn = snowflake.connector.connect(
#     user='thorataishwarya',
#     password='12345Ab#',
#     account='LNDFLFY.SIB87097',
#     warehouse='layoffs_data',
#     database='layoff_states',
#     schema='PUBLIC'
# )

# cs = conn.cursor()
# try:
# #     cs.execute("SELECT current_version()")
#     one_row = cs.fetchone()
#     print(one_row[0])
# finally:
#     cs.close()
# # conn.close()


# In[2]:


# # Specify Snowflake table name
# table_name = 'your_table_name'

# # Insert data into Snowflake table
# df.to_sql(table_name, conn, schema='<your_snowflake_schema>', if_exists='append', index=False)


# In[ ]:





# # Advanced Data Modeling

# # 

# # Importing Modules

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, cross_validate
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score, recall_score, confusion_matrix, f1_score, roc_curve,auc
import warnings
from sklearn.exceptions import FitFailedWarning
warnings.simplefilter('ignore', FitFailedWarning)
from sklearn.decomposition import PCA


# # Importing Dataset

# In[2]:


df = pd.read_csv('/Users/aishwaryathorat/Movies/MS Courses/Sem 1/DB sys. for Analytics/Project/WA_Fn-UseC_-HR-Employee-Attrition.csv')


# In[3]:


df.head()


# In[4]:


df.columns


# # No Missing Values

# In[5]:


df.isna().any().any()


# # Encoding Categorical Values

# In[6]:


#Columns with string values
categorical_column = ['Attrition', 'BusinessTravel', 'Department','Gender', 'JobRole', 'MaritalStatus', 'OverTime','EducationField']
encoder=LabelEncoder()
df[categorical_column]=df[categorical_column].apply(encoder.fit_transform)


# # Seperating into X and y

# In[7]:


y=df['Attrition']
X=df.drop(['EmployeeCount','Attrition','EmployeeNumber','Over18','StandardHours'],axis=1)


# # Spliting into Train and Test Sets

# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=1)


# ### Sample Row

# In[9]:


X_train.iloc[0].to_dict()


# # Feature Scaling

# PCA

# In[10]:


pca = PCA(n_components=2, random_state=0)
X_train_pca = pca.fit_transform(X_train)
print('20 PCs explain ', np.cumsum(pca.explained_variance_ratio_)*100, '% of variance cumulatively')
# scree plot
PC_values = np.arange(pca.n_components_) + 1
plt.plot(PC_values, pca.explained_variance_ratio_, 'ro-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.show()


# Standardization

# In[11]:


standard_scaler = StandardScaler()

pca_std = PCA(n_components=20, random_state=0)
X_train_standardized = pca_std.fit_transform(standard_scaler.fit_transform(X_train))
print('20 PCs explain ', np.cumsum(pca_std.explained_variance_ratio_)*100, '% of variance cumulatively')
# scree plot
PC_values = np.arange(pca_std.n_components_) + 1
plt.plot(PC_values, pca_std.explained_variance_ratio_, 'ro-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.show()
X_test_standardized = pca_std.transform(standard_scaler.transform(X_test))

X_standardized = pca_std.transform(standard_scaler.fit_transform(X))


# Normalization

# In[12]:


min_max_scaler = MinMaxScaler()

pca_norm = PCA(n_components=17, random_state=0)
X_train_normalized = pca_norm.fit_transform(min_max_scaler.fit_transform(X_train))
print('17 PCs explain ', np.cumsum(pca_norm.explained_variance_ratio_)*100, '% of variance cumulatively')
# scree plot
PC_values = np.arange(pca_norm.n_components_) + 1
plt.plot(PC_values, pca_norm.explained_variance_ratio_, 'ro-', linewidth=2)
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Proportion of Variance Explained')
plt.show()
X_test_normalized = pca_norm.transform(min_max_scaler.transform(X_test))

X_normalized = pca_norm.transform(min_max_scaler.fit_transform(X))


# Full datasets

# In[13]:


X_train = X_train_pca
X_test = pca.transform(X_test)
X = pca.transform(X)


# # Performing Logistic Regression

# In[17]:


def train_predict_evaluate(model,X_train,y_train,X_test):
  model.fit(X_train,y_train)
  y_pred = model.predict(X_test)

  print("Accuracy: ",accuracy_score(y_test,y_pred))
  print("Precision: ",precision_score(y_test,y_pred,zero_division=0))
  print("Recall: ",recall_score(y_test,y_pred,zero_division=0))
  print("F1 Score: ",f1_score(y_test,y_pred,zero_division=0))
  print("Confusion Matrix:\n",confusion_matrix(y_test,y_pred))

  
  fpr,tpr,thresholds = roc_curve(y_test,y_pred)
  plt.plot(fpr, tpr,color='green',label='ROC curve (area = %0.2f)' % auc(fpr,tpr))
  plt.plot([0, 1], [0, 1], color='orange', linestyle='--')
  plt.xlabel("False Positive Rate")
  plt.ylabel("True Positive Rate")
  plt.title("ROC Curve")
  plt.legend(loc="lower right")
  plt.show()


# ### With Standardization

# In[19]:


train_predict_evaluate(LogisticRegression(max_iter=100000,C=0.001,penalty='l2',solver='liblinear'),X_train_standardized,y_train,X_test_standardized)

