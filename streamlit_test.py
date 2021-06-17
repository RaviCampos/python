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

# average metrics
df1 = filtered_data[["id", "zipcode"]].groupby("zipcode").count().reset_index()
df2 = filtered_data[["price", "zipcode"]].groupby("zipcode").mean().reset_index()
df3 = filtered_data[["sqft_living", "zipcode"]].groupby("zipcode").mean().reset_index()
df4 = data[["price/sqft", "zipcode"]].groupby("zipcode").mean().reset_index()



st.write(filtered_data.head())

















