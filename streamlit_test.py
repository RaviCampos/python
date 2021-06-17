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


















