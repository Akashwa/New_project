# importing the required libraries
import pandas as pd 
import numpy as np 
from Remove_duplicates import *
from Convert_datatype import *
from Missing_values import *
from Outliers import * 
from stationarity import *


def Data_cleaning (read_df):
    # read_df = pd.read_json(dataframe)                          # reading Data 
    # #print(read_df)
    dr_df = remove_duplicates(read_df)                         # duplicate removal and setting time as index
    #print(dr_df)
    cd_df = convert_datatype(dr_df,method='one_hot_encoder')   # converting data type if any categorical feature 
    #print(cd_df)
    mv_df = imputation(cd_df,method='forward_fill')            # impute the missing value using suitable method 
    #print(mv_df)
    oh_df = handle_outliers(mv_df,method='median')             # outliers checking and handling
    #print(oh_df)
    sh_df = stationarity_adf(oh_df)                            # stationarity checking and handling 
    
    return sh_df



# this code is giving the error - (TypeError: argument of type 'method' is not iterable)

# def Data_cleaning (dataframe):
#     read_df = pd.read_json(dataframe)                          # reading Data 
#     #print(read_df)
#     dr_df = remove_duplicates(read_df)                         # duplicate removal and setting time as index
#     #print(dr_df)
#     cd_df = convert_datatype(dr_df,method='one_hot_encoder')   # converting data type if any categorical feature 
#     #print(cd_df)
#     mv_df = imputation(cd_df,method='forward_fill')            # impute the missing value using suitable method 
#     #print(mv_df)
#     oh_df = handle_outliers(mv_df,method='median')             # outliers checking and handling
#     #print(oh_df)
#     sh_df = stationarity_adf(oh_df)                            # stationarity checking and handling 
    
#     return sh_df                                               # return the cleaned dataframe





 