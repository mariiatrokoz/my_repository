'''IMPORTS'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

'''GET THE DATA'''
customers = pd.read_csv("ecommerce_customers.csv")
print(customers.head())
print(customers.describe())

sns.jointplot(x=customers["Time on Website"],y=customers["Yearly Amount Spent"])
plt.savefig("jointplot.png")

sns.jointplot(x=customers["Time on App"],y=customers["Yearly Amount Spent"])
plt.savefig("jointplot_II.png")

sns.pairplot(customers)
plt.savefig("pairplot.png")

sns.lmplot(x="Yearly Amount Spent", y="Length of Membership", data=customers)
plt.savefig("lmplot.png")

'''TRAINING AND TESTING DATA'''
print(customers.columns)
X=customers[['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']]
y=customers["Yearly Amount Spent"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size =0.3, random_state=101)

'''TRAINING THE MODEL'''
lm = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1) # normalize=False
lm.fit(X_train,y_train)
print("Coefficients: ", lm.coef_) # [25.98154972 38.59015875  0.19040528 61.27909654]

'''PREDICTING TEST DATA'''
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.savefig("lm_scatter.png")

'''EVALUATING THE MODEL'''
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

'''RESIDUALS'''
sns.displot((y_test-predictions),bins=50)
plt.savefig("displot.png")
