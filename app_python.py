# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 11:39:27 2025

@author: HP
"""

import streamlit as st
import pandas as pd
import seaborn as sns 

st.title("Data Analysis")
st.subheader("Data Analysis using Python and Streamlit")

# uploading the dataset
upload = st.file_uploader("Upload your csv data file")
if upload is not None:
    df = pd.read_csv(upload)

# show dataset
if st.checkbox("Preview Dataset"):
    if st.button("Head"):
        st.write(df.head())
    if st.button("Tail"):
        st.write(df.tail())

# checking datatype of each coloumn 
if upload is not None :
    if st.checkbox("Data Type of each Coloumn"):
        st.text("Data Types")
        st.write(df.dtypes)
        
# find shape of the data
if upload is not None :
    df_shape = st.radio("What dimension do you wanna check?" ('Rows', 'Coloumns'))
    
    if df_shape == 'Rows':                 
        st.text("Number of Rows")
        st.write(df.shape[0])
    
    if df_shape == 'Coloumns':                 
        st.text("Number of Coloumns")
        st.write(df.shape[1])   
        
        
# finding null values in the dataset 
if upload is not None:
    test=df.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(df.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!!,No Missing Values")
        
# finding duplicate values
if upload is not None:
    test=df.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            df=df.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
            
# getting overall statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(df.describe(include='all'))


# cheeky additions
if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")
    
if st.checkbox("By"):
    st.success("Priyanshu Sethi")
       
        
        
        
        
        
        
        
        
        