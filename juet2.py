import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# 1. Tomar jute er last 3 bochor er data (tumi change korte paro)
data = {
    'Month': [1,2,3,4,5,6,7,8,9,10,11,12]*3,
    'Year': [2023]*12 + [2024]*12 + [2025]*12,
    'Rainfall': [5,10,30,80,150,300,350,300,200,80,20,5]*3, # mm
    'Price': [13500,14200,15000,14800,12000,11000,10500,10800,11500,10500,12000,13000,
              13800,14500,15500,15200,12500,11500,10800,11000,11800,10800,12300,13300,
              14000,14800,16000,15800,13000,11800,11200,11500,12000,11000,12500,13500]
}
df = pd.DataFrame(data)

# 2. Model train
X = df[['Month','Year','Rainfall']]
y = df['Price']
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 3. Next 6 month predict (Oct 2026 - Mar 2027)
future = pd.DataFrame({
    'Month': [10,11,12,1,2,3],
    'Year': [2026,2026,2026,2027,2027,2027],
    'Rainfall': [70,15,5,5,12,35]
})
future['Predicted_Price'] = model.predict(future[['Month','Year','Rainfall']])

print(future)
# Output dekhabe kobe dam beshi

# 4. Graph
plt.plot(future['Month'], future['Predicted_Price'], marker='o')
plt.title('Jute Price Prediction - Next 6 Months')
plt.xlabel('Month')
plt.ylabel('Price per Quintal (Rs)')
plt.grid()
plt.show()

# Best selling month
best = future.loc[future['Predicted_Price'].idxmax()]
print(f"\nBest time to sell: Month {best['Month']} at Rs {best['Predicted_Price']:.0f}/quintal")
print(f"Tomar 20 Quintal e profit: Rs {best['Predicted_Price']*20:.0f}")
