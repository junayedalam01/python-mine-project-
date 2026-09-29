import streamlit as lit
import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plot
import time,requests
data ={"name":["junayed","alam",],
       "age":[23,44,]}

df =pd.DataFrame(data)
lit.title("hello ")
cart =plot.plot(df["age"])
plot.show()
lit.area_chart(cart)
