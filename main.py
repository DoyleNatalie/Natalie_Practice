# Example 1, do not modify!
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

today=pd.Timestamp
print(today)

index=pd.date_range(start='2020-1-1',periods=12, freq='M')
print(index)
