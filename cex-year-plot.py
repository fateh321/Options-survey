# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#df_temp = pd.read_csv('cex-volume.csv',names=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
df = pd.read_csv('cex-volume-year.csv').to_numpy()
#print(df) 
# create data
x = ['2020', '2021', '2022', '2023']
y1 = df[0,:]
y2 = df[1,:]
print(y1)
print(y2)
# plot bars in stack manner
plt.ylim(0, 520)
plt.yticks(fontsize=12)
plt.xticks(fontsize=11)
plt.bar(x, y1, color='mediumblue', width=0.4)
plt.bar(x, y2, bottom=y1, color='limegreen', width=0.4)
plt.xlabel("Years", size = 13)
plt.ylabel("Notional Volume (Billion dollars)", size = 13)
plt.legend(["BTC", "ETH"], loc="upper left")
#plt.title("Option volume ")
plt.savefig("volume-year.pdf", bbox_inches="tight")
plt.show()
