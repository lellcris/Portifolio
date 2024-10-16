#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[26]:


# Packages 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[11]:


import random


# In[12]:


# Define categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']

# Set the number of entries you want (e.g., n = 500)
n = 500

# Generate random data
data = {
    'Date': pd.date_range(start='2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())


# In[17]:


# DataFrame’s structure, (number of entries, column names, data types, and memory usage).
print(df.info())


# In[18]:


#Summary of numerical columns (count, mean, standard deviation, minimum, and maximum values).
print(df.describe())


# In[19]:


# Count the Frequency of Each Category(How many times each category appears in the data)

category_counts = df['Category'].value_counts()
print(category_counts)


# In[20]:


# Remove rows with any null values
df_cleaned = df.dropna()


# In[21]:


# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()


# In[22]:


# Convert 'Date' column to datetime format
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])


# In[23]:


# Convert 'Likes' column to integer format
df_cleaned['Likes'] = df_cleaned['Likes'].astype(int)


# In[24]:


# Display the cleaned DataFrame's information to confirm changes
print(df_cleaned.info())


# In[25]:


print(df.head())


# In[27]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[29]:


# Create a histogram of the 'Likes' column
sns.distplot(df_cleaned['Likes'], kde=False)
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.title('Distribution of Likes')
plt.show()


# In[30]:


# Create a Boxplot with a Custom Color Palette
sns.boxplot(x='Category', y='Likes', data=df_cleaned, palette="Pastel1")  
plt.xlabel('Category')
plt.ylabel('Likes')
plt.title('Likes Distribution Across Categories')
plt.xticks(rotation=45)
plt.show()


# In[31]:


# Calculate and print the overall mean of 'Likes'
mean_likes = df_cleaned['Likes'].mean()
print("Mean of Likes:", mean_likes)


# In[32]:


# Calculate and print the mean 'Likes' for each 'Category'
mean_likes_by_category = df_cleaned.groupby('Category')['Likes'].mean()
print(mean_likes_by_category)


# In[ ]:




