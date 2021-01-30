# -*- coding: utf-8 -*-
"""IDS 561 Final Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BXZfyQezuSXThCC6iuq4HqrRFChpy1EE

### Black Friday Sales Analysis and Prediction

---

*Submitted by -*
*Ipseeta Deka, Mrinal Ashok Bageshwari, Niharika Yogesh Apte*

---

# **Step 1: Importing libraries and loading the data**
"""

from google.colab import drive 
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#reading the file
from google.colab import files
uploaded = files.upload()

bf_data = pd.read_csv("train.csv") #storing train.csv in a dataframe

"""#**Step 2: Data Cleaning**

Previewing the data
"""

print(bf_data.head())

"""Previewing the datatypes"""

bf_data.info()

"""There are null values in Product_Category_2 and Product_Category_3"""

bf_data.describe()

"""The mean value of Product_Category_2 is 9.842329 and of Product_Category_3 is 12.668243

Hence, we will use these values to fill the missing values


"""

pip install scikit-learn==0.19.1

"""Handling the missing values"""

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(bf_data.iloc[:, 9:11].values)
bf_data.iloc[:,9:11] = imputer.transform(bf_data.iloc[:, 9:11].values)
bf_data.info()

"""Dropping unnecessary columns """

bf_data.drop(['User_ID','Product_ID'], axis=1, inplace=True)
bf_data.info()

"""# **Step 3: Exploratory data analysis**

Observing the purchase behaviour with respect to Age Group
"""

bf_data["Age"] = bf_data["Age"].astype('category')

ax = sns.countplot(y="Age", data=bf_data)
plt.title('Purchasing Behaviour by Age Group')
plt.ylabel('Age group')

total = len(bf_data['Age'])
for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_width()/total)
        x = p.get_x() + p.get_width() + 0.02
        y = p.get_y() + p.get_height()/2
        ax.annotate(percentage, (x, y))

plt.show()

"""Observing the purchase behaviour with respect to Gender



"""

unique_gender = bf_data.Gender.unique()

countF = bf_data[bf_data['Gender'] == 'F'].count() 
countM = bf_data[bf_data['Gender'] == 'M'].count() 

values= [countF.Gender,countM.Gender]
labels = ['Female', 'Male']
explode = (0.2, 0)
plt.pie(values, labels= values,explode=explode,autopct='%1.1f%%', radius=1, counterclock=False, shadow=True)
plt.title('Percent of purchases made by Gender')
plt.legend(labels,loc=3)
plt.show()

"""City wise sales trend"""

ax = sns.countplot(y="City_Category", data=bf_data)
plt.title('Sale percentage by City')
plt.ylabel('City')

total = len(bf_data['City_Category'])
for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_width()/total)
        x = p.get_x() + p.get_width() + 0.02
        y = p.get_y() + p.get_height()/2
        ax.annotate(percentage, (x, y))

plt.show()

"""Best performing product category (in terms of revenue)"""

productwise_revenue = bf_data.groupby(['Product_Category_1'])['Purchase'].sum().reset_index()

plt.figure(figsize=(15,8))
plt.ticklabel_format(style='plain', axis='y',useOffset=False)
plt.title('Product category that generated Maximum revenue')
ax = sns.barplot(x='Product_Category_1', y='Purchase',data=productwise_revenue)

"""Correlation mattrix of relevant features"""

sns.heatmap(
    bf_data.corr(),
    annot=True
)

"""# **Step 4: Data modelling and Prediction of Sales**"""

X = bf_data.iloc[:, 0:9].values 
y = bf_data.iloc[:, 9].values #target variable
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X_train

y_train

X_test

X_test

from sklearn.preprocessing import LabelEncoder
labelencoder_X_train = LabelEncoder()
X_train

X_train[:, 0] = labelencoder_X_train.fit_transform(X_train[:, 0])
X_train

X_train[:, 1] = labelencoder_X_train.fit_transform(X_train[:, 1])
X_train

X_train[:, 3] = labelencoder_X_train.fit_transform(X_train[:, 3])
X_train

X_train[:, 4] = labelencoder_X_train.fit_transform(X_train[:, 4])
X_train

labelencoder_X_test = LabelEncoder()
X_test

X_test[:, 0] = labelencoder_X_test.fit_transform(X_test[:, 0])
X_test

X_test[:, 1] = labelencoder_X_test.fit_transform(X_test[:, 1])
X_test

X_test[:, 3] = labelencoder_X_test.fit_transform(X_test[:, 3])
X_test

X_test[:, 4] = labelencoder_X_test.fit_transform(X_test[:, 4])
X_test

"""Linear Regression Model"""

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()

lin_reg.fit(X_train, y_train)

Y_pred_lin_reg = lin_reg.predict(X_test)

Y_pred_lin_reg

"""KNN Regression Model"""

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor()

knn.fit(X_train, y_train)

Y_pred_knn = knn.predict(X_test)

Y_pred_knn

"""Decision Tree Regression Model"""

from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor()

dt.fit(X_train, y_train)
Y_pred_dt = dt.predict(X_test)
Y_pred_dt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

print("Linear Regression: ")
print("RMSE:",np.sqrt(mean_squared_error(y_test, Y_pred_lin_reg)))
print("R2 score:", r2_score(y_test, Y_pred_lin_reg))

print("KNN regression: ")
print("RMSE:",np.sqrt(mean_squared_error(y_test, Y_pred_knn)))
print("R2 score:", r2_score(y_test, Y_pred_knn))

print("Decision tree regression: ")
print("RMSE:",np.sqrt(mean_squared_error(y_test, Y_pred_dt)))
print("R2 score:", r2_score(y_test, Y_pred_dt))

plt.scatter(y_test, Y_pred_lin_reg, alpha=0.5)
plt.plot(y_test, y_test,color='green')

"""We notice that Linear Regression Model fails entirely when the sales go above 15000."""

plt.scatter(y_test, Y_pred_dt, alpha=0.5)
plt.plot(y_test, y_test,color='green')

"""Decision Tree Regression performs significantly better than Linear Regression also it does not fail as sales rise. """

plt.scatter(y_test, Y_pred_knn, alpha=0.5)
plt.plot(y_test, y_test,color='green')

"""KNN Regression performs similar to Decision Tree Regression Model but RMSE is slightly better and hence this is the most suitable model."""