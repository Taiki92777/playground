#%%
import pandas as pd

df=pd.DataFrame([['green','M',10.1,'class1'],['red','L',13.5,'class2'],['blue','XL',15.3,'class1']])
df.columns=['color','size','price','classlabel']
df
#%%
size_mapping={'XL':3,'L':2,'M':1}
df['size']=df['size'].map(size_mapping)
df
#%%
inv_size_mapping={v:k for k,v in size_mapping.items()}
df['size'].map(inv_size_mapping)
#%%
import numpy as np

class_mapping={label:idx for idx,label in enumerate(np.unique(df['classlabel']))}
class_mapping
#%%
df['classlabel']=df['classlabel'].map(class_mapping)
df
#%%
inv_class_mapping={v:k for k,v in class_mapping.items()}
df['classlabel']=df['classlabel'].map(inv_class_mapping)
df
#%%
from sklearn.preprocessing import LabelEncoder

class_le=LabelEncoder()
y=class_le.fit_transform(df['classlabel'].values)
y
#%%
class_le.inverse_transform(y)
#%%
X=df[['color','size','price']].values
color_le=LabelEncoder()
X[:,0]=color_le.fit_transform(X[:,0])
X
#%%
from sklearn.preprocessing import OneHotEncoder

ohe=OneHotEncoder(categorical_features=[0])
ohe.fit_transform(X).toarray()
#%%
pd.get_dummies(df[['price','color','size']])
#%%
pd.get_dummies(df[['price','color','size']],drop_first=True)
#%%
ohe=OneHotEncoder(categorical_features=[0])
ohe.fit_transform(X).toarray()[:,1:]