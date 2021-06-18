import numpy as np
import pandas as pd
import streamlit as st
import time

# ADD A LOADING BAR TO STREAMLIT
# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)     

# '...and now we\'re done!'

# auxiliary funcs
def display_avg_metrics(df):
    df1 = df[["id", "zipcode"]].groupby("zipcode").count().reset_index()
    df2 = df[["price", "zipcode"]].groupby("zipcode").mean().reset_index()
    df3 = df[["sqft_living", "zipcode"]].groupby("zipcode").mean().reset_index()
    df4 = data[["price/sqft", "zipcode"]].groupby("zipcode").mean().reset_index()

    m1 = df1.merge(df2, how='inner', on='zipcode')
    m2 = m1.merge(df3, how='inner', on='zipcode')
    m3 = m2.merge(df4, how='inner', on='zipcode')

    m3.columns = ["zipcode", "real states", "avg price", "avg sqft living", "avg price by sqft"]

    st.write(m3.round())

def display_desc_statistics(df):
    num_attributes = df.select_dtypes(['int64', 'float64']).drop(columns='id')
    mean = num_attributes.apply(np.mean)
    median = num_attributes.apply(np.median)
    std = num_attributes.apply(np.std)
    max_ = num_attributes.apply(np.max)
    min_ = num_attributes.apply(np.min)

    df1 = pd.concat([max_, min_, median, mean, std], axis='columns')
    df1.columns = ['max', 'min', "median", "mean", "std"]
    df1 = df1.transpose()

    st.write(df1.round())

# use a decorator to mantain the data in ram, not in hd
@st.cache(allow_output_mutation=True)
def load_data(path):
    return pd.read_csv(path)

data = load_data("./try_ds/kc_house_data.csv")

st.title("A new chapter begins")

# add new feature
data["price/sqft"] = data["price"] / data["sqft_lot"]


# =========================
# Data Overview
# =========================

# create sidebar filter options (just creating the element for now)
f_attributes = st.sidebar.multiselect("Pick an attribute", data.columns)
f_zip_code = st.sidebar.multiselect("Pick a zipcode", data["zipcode"].unique())

st.write("## Data Overview")

filtered_data = None

if (f_attributes != []) & (f_zip_code != []):
    filtered_data = data.loc[data["zipcode"].isin(f_zip_code), f_attributes]
elif (f_attributes != []) & (f_zip_code == []):
    filtered_data = data[f_attributes]
elif (f_attributes == []) & (f_zip_code != []):
    filtered_data = data.loc[data["zipcode"].isin(f_zip_code), :]
else:
    filtered_data = data.copy()

st.write(filtered_data)

# average metrics
st.write("### Average metrics")
try:
    display_avg_metrics(filtered_data)
except:
    display_avg_metrics(data)

# descriptive statistics
st.write("### Descriptive statistics")
try:
    display_desc_statistics(filtered_data)
except:
    display_desc_statistics(data)


















