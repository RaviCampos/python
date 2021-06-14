from numpy import int64
import pandas as pd

data = pd.read_csv("./kc_house_data.csv")

# data["date"] = pd.to_datetime( data["date"])
# data["bedrooms"] = data["bedrooms"].astype( float)
# data["bedrooms"] = data["bedrooms"].astype( int64 )
# print(data.dtypes)

data["level"] = "standard"

data.loc[data["price"] > 540000, "level"] = "high_standard"
data.loc[data["price"] <= 540000, "level"] = "low_standard"

print(data.head(10))
# water.shape[0]