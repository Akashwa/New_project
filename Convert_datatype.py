# importing the required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# converts data types using encoding techniques 
def convert_datatype(dataframe, method):
    for col in dataframe.columns:
        if dataframe[col].dtype == 'object':
            if method == 'label_encoder':            
                lable_encoding = LabelEncoder()
                dataframe[col] = lable_encoding.fit_transform(dataframe[col])                       # it will convert the data type using label encoding method.
            elif method == 'one_hot_encoder':
                onehot_encoding = OneHotEncoder()
                dataframe= pd.concat([dataframe.drop(col, axis=1),
                pd.DataFrame(onehot_encoding.fit_transform(dataframe[[col]]).toarray())], axis=1)   # it will convert the data type using one hot encoding method. 
            
    return dataframe                                                                                # return dataframe with converted datatypes using selected method. 
