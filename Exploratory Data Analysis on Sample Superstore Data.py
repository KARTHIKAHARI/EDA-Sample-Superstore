#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis on Sample Superstore Data
# 
# 
# #1. We need to perform 'Exploratory Data Analysis' on dataset 'Sample Superstore'.
# #2.Find out weak areas where we need to work to make more profits.
# #3.Derive business problems after exploring the data.
# 
# #Importing the libraries and the dataset.
# 
# 

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
superstore = pd.read_csv(r"C:\Users\karth\Downloads\SampleSuperstore.csv")


# In[5]:


superstore.head()


# # Data Summary

# In[8]:


superstore.describe()


# In[2]:


#Dropping unwanted Columns.


# In[6]:


superstore.drop(['Postal Code'], axis = 1, inplace = True)


# In[7]:


superstore.drop(['Country'], axis = 1, inplace = True)


# In[8]:


superstore.head()


# In[9]:


duplicates = superstore.duplicated()


# In[10]:


duplicates.sum()


# In[11]:


superstore.drop_duplicates(inplace = True)


# In[12]:


duplicates = superstore.duplicated()


# In[13]:


duplicates.sum()


# In[ ]:





# In[ ]:





# # Data Visualization

# In[14]:


corr = superstore.corr()


# In[15]:


sns.heatmap(corr, annot = True, cmap = "YlGnBu")


# In[26]:


#We see that there is a positive correlation between sales and profit. As Sales increases the profit also increases.


# ## Discount vs Profit

# In[16]:


plt.figure(figsize = (8,8))
sns.lineplot(x = 'Discount', y = 'Profit', color = 'red', data = superstore)
plt.show()


# In[30]:


#When the business manager sell the product at 10% discount he gets profit, but when he sells the product at 50% discount he is in loss.


# # Quantity vs Profit

# In[17]:


plt.figure(figsize = (8,8))
sns.lineplot(x = 'Quantity', y = 'Profit', color = 'green', data = superstore)
plt.show()


# # Sales by State

# In[18]:


plt.figure(figsize = (16,8))
chart = sns.countplot(x = 'State', data = superstore, order = superstore['State'].value_counts().index)
chart.set_xticklabels(chart.get_xticklabels(), rotation = 90)
chart.set_xlabel("State", fontsize = 16)
plt.show()


# In[19]:


#Top 3 performing states are California, New York and Texas 


# # Category wise Sales

# In[20]:


pie = superstore.groupby('Category')['Sales'].sum().sort_values(ascending = False)

plt.figure(figsize = (8,8))
explode = (0.1, 0.0, 0.0)
color = ['red', 'blue', 'yellow']
pie.plot.pie(autopct = "%1.1f%%", explode = explode, colors = color, shadow = True)
plt.title('Category wise Sales')


# In[21]:


#Category Technology has the highest amount of sales than the other two categories.


# # Plotting a pairplot based on the Category

# In[22]:


sns.pairplot(superstore, hue = 'Category', diag_kind = 'kde')


# In[23]:


#Allotting two different columns df_profit and df_loss


# In[24]:


df_loss = superstore[superstore['Profit']<0]
df_profit = superstore[superstore['Profit']>0]


# # Finding the profitable ship mode

# In[28]:


plt.figure(figsize = (16,8))
axes = plt.subplot(121)
sns.barplot(x = 'Ship Mode', y = 'Profit', data = df_profit, palette = "summer")


# In[29]:


#First Class Ship Mode makes the highest profit among all the Ship Modes.


# # Visualizing Sub-Category

# In[34]:


plt.figure(figsize = (16,8))
sub_ca_count = sns.countplot(x = 'Sub-Category', data = superstore, order = superstore['Sub-Category'].value_counts().index, palette = 'YlOrRd_r')

sub_ca_count.set_xticklabels(sub_ca_count.get_xticklabels(), rotation = 90)
sub_ca_count.set_xlabel("Sub-Ctegory", fontsize = 16)
plt.show()


# In[35]:


#Binders, Paper and Furnishings are the top 3 sub-categories that were sold the most.


# In[36]:


x = df_profit.groupby('Sub-Category')['Profit'].sum().sort_values(ascending = False)

plt.figure(figsize = (10,10))

x.plot.pie(autopct = "%1.1f%%")
plt.title('Sub-Category wise Plot')
plt.show()


# In[37]:


#From the above pie chart it can be seen that binders yield more profit, followed by copiers and phones.


# # Comparing Sales and Profit among segments

# In[38]:


y = superstore.groupby('Segment')[['Sales','Profit']].sum()
y.plot.bar()
plt.show()


# In[39]:


#The segment Consumer has more sales and more profit. It is also to be noted that all the segments make profit.


# # Results

# 1)To gain more profit he should sell his products at 10% discount and not more than that.
# 

# 2)The company's performance is the maximum in California, New York and Texas.

# 3)When it comes to sales based on Category, products that come under Technology were sold the most.
# 

#  4)Based on Ship mode - The first class ship mode gives the company more profit than other ship modes. 

# 5)Binders, papers and furnishings are the most sold products. 

# 

# 6)The sales of binders, copiers and phones were more profitable.

#  7)Interesting fact is that copiers is the least sold product still it yields the second highest profit for the company.

#  8)The segment Consumer has more sales and more profit

# In[ ]:




