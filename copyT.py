#!/usr/bin/env python
# coding: utf-8

# ## Data Tools Engineer Task:

# In[38]:


import pandas as pd
from itertools import permutations, product
import openpyxl
from datetime import date
import requests
import json


# ## Load CarsData

# In[39]:


data_sheet = 'CarsData.xlsx'
df = pd.read_excel(data_sheet, sheet_name='Sheet1', index_col=0).T # transpose the data


# ## Display data columns (testing if it loaded right)

# In[40]:


df.columns.values


# ## API call

# In[41]:


url = 'https://api.coinbase.com/v2/exchange-rates'
x = requests.get(url, auth=('myAPIkey', 'CLP'))
api_data = json.loads(x.text)


# In[42]:


usd_rate = api_data['data']['rates']['USD']
clp_rate = api_data['data']['rates']['CLP']
exhange_rate = abs(float(usd_rate) / float(clp_rate))


# ## clean data and parase the columns

# In[43]:


cars_df = df.drop("Condition") # we dont need the condition


# In[44]:


# parasing the columns data
def parse_att(data):
    return data.iloc[0].split(';')


# In[45]:


Q1 = parse_att(cars_df['Q1-IsElectric'])
Q2 = parse_att(cars_df['Q2-KM'])
Q3 = parse_att(cars_df['Q3-EngineSize'])
Q4 = parse_att(cars_df['Q4-Color'])
Q5 = parse_att(cars_df['Q5-ModelData'])


# ## create permutations cars data from the columns data

# In[46]:


wb_out = openpyxl.Workbook()
ws_out = wb_out.active
for i in product(Q1, Q2, Q3, Q4, Q5):
    ws_out.append(i)
wb_out.save(filename='carsCleaned.xlsx')


# ## Load new data to Pandas DB

# In[47]:


cars = pd.read_excel('carsCleaned.xlsx',header=None,
                     names=['Q1-IsElectric', 'Q2-KM', 'Q3-EngineSize', 'Q4-Color', 'Q5-ModelData'])


# ## check conditons

# In[48]:


cond = df.loc['Condition']


# In[49]:


print(cond)


# ## clean data by condition

# In[50]:


cars.loc[cars['Q1-IsElectric'] == False, 'Q3-EngineSize'] = None


# In[ ]:





# ## Test new data ( we should get 600rows  and engine size nan if q1 is false )

# In[51]:


cars.tail(10)


# In[52]:


cars.head(10)


# In[53]:


cars.shape[0] ## return number of rows (all good)


# ## Create new full Date column with car manufacture date as type dd/mm/yyyy

# In[54]:


cars['Dates'] = cars['Q5-ModelData'].apply(
    lambda x: x.split(',')[2].split(':')[1].rstrip('}').rstrip('\n')).astype(int)


# In[55]:


cars['Dates'] = pd.to_datetime(cars['Dates'],format='%Y')


# In[ ]:





# ## Create new full Date column current date as type dd/mm/yyyy

# In[56]:


today = date.today()
cars["Current_Date"] = today


# ## Create column with the value of days passed since manufacture till today and diplay the data

# In[57]:


cars['Days_Passed'] = (pd.to_datetime(cars['Current_Date']) - cars['Dates']).dt.days


# In[58]:


cars.head(10)


# # Create column with the exhange rate between currencies

# In[59]:


cars['exhange_rate'] = exhange_rate


# In[60]:


cars.head(10)


# ## Calculate the price of the car and return the data as excel

# In[61]:


cars['Price'] = cars['Q2-KM'] * cars['Days_Passed'] * cars['exhange_rate'] 


# In[62]:


cars.to_excel("carsPriced.xlsx", index=False, columns=['Q1-IsElectric', 'Q2-KM', 'Q3-EngineSize', 'Q4-Color',
       'Q5-ModelData','Price'])  


# ## display cars price data 

# In[63]:


cars_priced = pd.read_excel('carsPriced.xlsx')


# In[65]:


cars_priced.tail(10)


# In[ ]:





# In[ ]:




