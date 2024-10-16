#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# The project began by generating random social media data to simulate various post categories and like counts. I utilized Python’s Pandas, Seaborn, and Matplotlib libraries to clean, explore, and visualize the data effectively. Throughout the process, I encountered and resolved challenges related to data cleaning, ensuring the final dataset was robust for analysis. Additionally, I experimented with Seaborn palettes to enhance visual appeal and legibility of the plots.

# In[21]:


# Packages 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[22]:


import random


# In[23]:


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


# In[24]:


# DataFrame’s structure, (number of entries, column names, data types, and memory usage).
print(df.info())


# In[25]:


#Summary of numerical columns (count, mean, standard deviation, minimum, and maximum values).
print(df.describe())


# In[26]:


# Count the Frequency of Each Category(How many times each category appears in the data)

category_counts = df['Category'].value_counts()
print(category_counts)


# In[27]:


# Remove rows with any null values
df_cleaned = df.dropna()


# In[28]:


# Remove duplicate rows
df_cleaned = df_cleaned.drop_duplicates()


# In[29]:


# Convert 'Date' column to datetime format
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])


# In[30]:


# Convert 'Likes' column to integer format
df_cleaned['Likes'] = df_cleaned['Likes'].astype(int)


# In[31]:


# Display the cleaned DataFrame's information to confirm changes
print(df_cleaned.info())


# In[32]:


print(df.head())


# In[33]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[34]:


# Create a histogram of the 'Likes' column
sns.histplot(df_cleaned['Likes']),
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.title('Distribution of Likes')
plt.show()


# In[35]:


# Create a Boxplot with a Custom Color Palette
sns.boxplot(x='Category', y='Likes', data=df_cleaned, palette="Pastel1")  
plt.xlabel('Category')
plt.ylabel('Likes')
plt.title('Likes Distribution Across Categories')
plt.xticks(rotation=45)
plt.show()


# In[36]:


# Calculate and print the overall mean of 'Likes'
mean_likes = df_cleaned['Likes'].mean()
print("Mean of Likes:", mean_likes)


# In[37]:


# Calculate and print the mean 'Likes' for each 'Category'
mean_likes_by_category = df_cleaned.groupby('Category')['Likes'].mean()
print(mean_likes_by_category)


# ### Key Findings ###

# The analysis revealed a nearly uniform distribution of likes across all posts, likely due to the random nature of the data generation. Among categories, 'Culture' and 'Food' posts tended to receive higher average likes, while 'Fashion' and 'Health' were slightly lower. Such insights might indicate potential areas for content focus, especially if these categories were real-world data.

# ### This Project ###

# What sets this project apart is the thorough approach to data quality and the commitment to making data-driven insights accessible through clear and visually appealing plots. My focus on data cleaning and aesthetic customization showcases a readiness to adapt and optimize for real-world analytics tasks.

# ### Improvements ###

# To elevate this analysis further, I would consider generating data that reflects real-world social media patterns, potentially including additional metrics like comments or shares. An interactive dashboard could also offer users an engaging way to explore the data dynamically, providing more flexibility in how insights are derived and applied.

# In[ ]:




