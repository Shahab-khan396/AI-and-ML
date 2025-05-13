#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[3]:


df = pd.read_csv("H:/faheeemjan/AI_and_ML/data.csv")
# To display the top 5 rows 
df.head(5)  


# In[4]:


df.tail(5)                        # To display the botton 5 rows


# In[5]:


#. Checking the types of data
df.dtypes


# In[6]:


#Dropping irrelevant columns
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
df.head(5)


# In[7]:


#Renaming the columns
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
df.head(5)


# In[8]:


# Dropping the duplicate rows
df.shape


# In[9]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)


# In[10]:


df.count()      # Used to count the number of rows


# In[11]:


df = df.drop_duplicates()
df.head(5)


# In[12]:


df.count()


# In[13]:


#Dropping the missing or null values.
print(df.isnull().sum())


# In[14]:


df = df.dropna()    # Dropping the missing values.
df.count()


# In[15]:


print(df.isnull().sum())   # After dropping the values


# In[16]:


#Detecting Outliers


# In[17]:


sns.boxplot(x=df['Price'])


# In[18]:


sns.boxplot(x=df['HP'])


# In[19]:


sns.boxplot(x=df['Cylinders'])


# In[20]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[21]:


df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape


# In[22]:


#Plot different features against one another (scatter), against frequency (histogram)


# In[23]:


df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');


# In[24]:


plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[25]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


#Import all relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[28]:


#Loading the data


# In[29]:


#Read in the csv file and convert to a Pandas dataframe
df = pd.read_csv("https://raw.githubusercontent.com/siglimumuni/Datasets/master/customer-data.csv")


# In[30]:


#Viewing the dataframe


# In[31]:


#Return number of rows and columns
df.shape


# In[32]:


#Return first 5 rows of the dataset
df.head()


# In[33]:


#Return info on dataset
df.info()


# In[34]:


#Preparing the data
#Missing values


# In[35]:


#Display number missing values per column
df.isna().sum()


# In[36]:


#Check the mean credit score for each income group
df.groupby(by="income")["credit_score"].mean()


# In[37]:


#Create a function to impute missing values based on mean credit score for each income group
def impute_creditscore(income_classes):
    """This function takes a list of income groups and imputes the missing values of each based on the mean credit score for          each group"""
    #iterate through each income group
    for income_class in income_classes:      
        
        #create a subset of dataframe to use as filter
        mask = df["income"] == income_class
        
        #calculate the mean for the income group
        mean = df[df["income"] == income_class]["credit_score"].mean()
        
        #fill the missing values with mean of credit score for group
        df.loc[mask,"credit_score"] = df.loc[mask,'credit_score'].fillna(mean)


# In[38]:


#Apply the function to the dataframe
income_groups = ["poverty","upper class","middle class","working class"]
impute_creditscore(income_groups)

#check for missing values
df.isnull().sum()


# In[39]:


#Check the mean annual mileage for the different driving experience groups
df.groupby(by="driving_experience")["annual_mileage"].mean()


# In[40]:


#Calculate mean for annual_mileage column
mean_mileage = df["annual_mileage"].mean()

#Fill in null values using the column mean
df["annual_mileage"].fillna(mean_mileage,inplace=True)

#Check for null values
df.isna().sum()


# In[41]:


#Dropping columns


# In[42]:


#Delete the id and postal_code columns
df.drop(["id","postal_code"],axis=1,inplace=True)


# In[43]:


#Analyzing the data
#Univariate analysis


# In[44]:


#Check the count for each category in the "gender" column
df["gender"].value_counts()


# In[45]:


#Create a countplot to visualize the count of each category in the gender column.
sns.countplot(data=df,x="gender")
plt.title("Number of Clients per Gender")
plt.ylabel("Number of Clients")
plt.show()


# In[46]:


#Define plot size
plt.figure(figsize=[6,6])

#Define column to use
data = df["income"].value_counts(normalize=True)

#Define labels
labels = ["upper class","middle class","poverty","working class"]

#Define color palette
colors = sns.color_palette('pastel')

#Create pie chart
plt.pie(data,labels=labels,colors=colors, autopct='%.0f%%')
plt.title("Proportion of Clients by Income Group")
plt.show()


# In[47]:


#Create a countplot to visualize the count of each category in the education column 
plt.figure(figsize=[8,5])
sns.countplot(data=df,x="education",order=["university","high school","none"],color="orange")
plt.title("Number of Clients per Education Level")
plt.show()


# In[48]:


#Return summary statistics for the "credit_score" column
df["credit_score"].describe()


# In[49]:


#Plot a histogram using the "credit_score" column
plt.figure(figsize=[8,5])
sns.histplot(data=df,x="credit_score",bins=40).set(title="Distribution of credit scores",ylabel="Number of clients")
plt.show()


# In[50]:


#Plot a histogram using the "annual_mileage" column
plt.figure(figsize=[8,5])
sns.histplot(data=df,x="annual_mileage",bins=20,kde=True).set(title="Distribution of Annual Mileage",ylabel="Number of clients")
plt.show()


# In[51]:


#Bivariate analysis


# In[52]:


#Create a scatter plot to. show relationship between "annual_mileage" and "speeding_violations"
plt.figure(figsize=[8,5])
plt.scatter(data=df,x="annual_mileage",y="speeding_violations")
plt.title("Annual Mileage vrs Speeding Violations")
plt.ylabel("Speeding Violations")
plt.xlabel("Annual Mileage")
plt.show()


# In[53]:


#Create a correlation matrix to show relationship between select variables
corr_matrix = df[["speeding_violations","DUIs","past_accidents"]].corr()
corr_matrix


# In[54]:


#Create a heatmap to visualize correlation
plt.figure(figsize=[8,5])
sns.heatmap(corr_matrix,annot=True,cmap='Reds')
plt.title("Correlation between Selected Variables")
plt.show()


# In[55]:


#Check the mean annual mileage per category in the outcome column
df.groupby('outcome')['annual_mileage'].mean()


# In[56]:


#Plot two boxplots to compare dispersion
sns.boxplot(data=df,x='outcome', y='annual_mileage')
plt.title("Distribution of Annual Mileage per Outcome")
plt.show()


# In[ ]:




