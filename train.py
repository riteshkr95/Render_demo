import numpy as np
import pandas as pd
import warnings
import joblib

from scipy.stats import scoreatpercentile

warnings.filterwarnings("ignore")

df=pd.read_csv('/Users/riteshkumar/Desktop/Data_Science/Datasets/anemia_dataset.csv')
print(df.columns)
df=df[["%Red Pixel","%Green pixel" ,"%Blue pixel","Hb" ,"Anaemic"]]

# One hot encoding
df["Anaemic"]=pd.get_dummies(df["Anaemic"] ,dtype=int ,drop_first=True)

print(df)
#Variable Separation
X=df.drop(columns="Anaemic")
y=df["Anaemic"]

from sklearn.model_selection import  train_test_split
X_train,X_test ,y_train,y_test=train_test_split(X,y ,test_size=0.3 ,random_state=43)

from sklearn.linear_model import LogisticRegression

log_reg=LogisticRegression()

log_reg.fit(X_train,y_train)
y_pred=log_reg.predict(X_test)


joblib.dump(log_reg, "model.pkl")