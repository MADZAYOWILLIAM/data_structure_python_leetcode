from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Loading the data

data=pd.read_csv("/home/william/Dev/data/Morning_Routine_Productivity_Dataset.csv")
data

# Making A DataFrame from the data
dg=pd.DataFrame(data)
dg

# Checking the shape of the data
dg.shape

# Checking info of the data
dg.info()


dg.describe()


dg.columns

# Visualizing the data
sns.pairplot(dg,diag_kind='kde')
plt.show()

# Visualizing Column_wise
sns.histplot(x=dg['Wake-up Time'],y=dg['Sleep Duration (hrs)'])
plt.show()

sns.scatterplot(dg,x=dg['Sleep Duration (hrs)'],y=dg['Productivity Score (1-10)'])