# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#df_temp = pd.read_csv('cex-volume.csv',names=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
df = pd.read_csv('cex-volume.csv').to_numpy()
print(df) 
# create data
x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y1 = df[1,:]
y2 = df[2,:]
y3 = df[3,:]
y4 = df[4,:]
# plot bars in stack manner
plt.ylim(0, 68)
plt.yticks(fontsize=12)
plt.xticks(fontsize=11)
plt.bar(x, y1, color='mediumblue')
plt.bar(x, y2, bottom=y1, color='limegreen')
plt.bar(x, y3, bottom=y1+y2, color='gold')
plt.bar(x, y4, bottom=y1+y2+y3, color='mediumorchid')
plt.xlabel("Months", size = 13)
plt.ylabel("Notional Volume (Billion dollars)", size = 13)
plt.legend(["Deribit", "OKX", "Binance", "Delta"], loc="upper left")
#plt.title("Option volume ")
plt.savefig("volume.pdf", bbox_inches="tight")
plt.show()
