# Example 1, do not modify!
import pandas as pd
import matplotlib.pyplot as plt

Stock_prices=pd.read_csv("HistoricalQuotes - Copy.csv",index_col=0)
print(Stock_prices.info())
Stock_top=Stock_prices.head(20)

fig,ax=plt.subplots()
ax.plot(Stock_top.index,Stock_top["close"])
fig.autofmt_xdate()
print(ax)
plt.show()
