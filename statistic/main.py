import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Admin/Desktop/AImath/statistic/data.csv", encoding="UTF-8")
# lấy các cột từ dataframe
tv = df["TV"]
radio = df["radio"]
newspaper = df["newspaper"]
sales = df["sales"]

# tạo dataframe với 2 cột tv và radio
merge = pd.concat([tv, radio], axis="columns")
# tính hiệp phương sai
print(merge.cov())
print("")

# tính phương sai từng cột
print(tv.var())
print(radio.var())
print(newspaper.var())
print(sales.var())
print("")

# tính hệ số tương quan pearson giữa 2 cột tv và radio
print(merge.corr())
print("")

# tính góc giữa 2 cột
degrees = np.degrees(np.arccos((tv.dot(radio))/(np.linalg.norm(tv)*np.linalg.norm(radio))))
radian = np.deg2rad(degrees)
print(degrees)
print(radian)