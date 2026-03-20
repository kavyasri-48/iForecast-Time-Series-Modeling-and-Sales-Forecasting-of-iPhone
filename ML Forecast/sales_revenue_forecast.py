import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATASET
# -------------------------
df = pd.read_csv("sales_revenue.csv")

# -------------------------
# SALES MODEL
# -------------------------
X = df[['Year']]
y_sales = df['Units_Sold_Millions']

sales_model = LinearRegression()
sales_model.fit(X, y_sales)

# -------------------------
# REVENUE MODEL
# -------------------------
y_revenue = df['Revenue_Billions']

revenue_model = LinearRegression()
revenue_model.fit(X, y_revenue)

# -------------------------
# FUTURE YEARS (2026–2036)
# -------------------------
future_years = pd.DataFrame({
    'Year': list(range(2026, 2037))
})

# Predict Sales
future_years['Predicted_Units_Sold_Millions'] = sales_model.predict(future_years[['Year']])

# Predict Revenue
future_years['Predicted_Revenue_Billions'] = revenue_model.predict(future_years[['Year']])

# -------------------------
# ADD STRUCTURE FOR TABLEAU
# -------------------------

# Add empty prediction columns to historical data
df['Predicted_Units_Sold_Millions'] = None
df['Predicted_Revenue_Billions'] = None
df['Type'] = 'Actual'

# Add empty actual columns to future data
future_years['Units_Sold_Millions'] = None
future_years['Revenue_Billions'] = None
future_years['Type'] = 'Predicted'

# Reorder columns properly
df = df[['Year',
         'Units_Sold_Millions',
         'Revenue_Billions',
         'Predicted_Units_Sold_Millions',
         'Predicted_Revenue_Billions',
         'Type']]

future_years = future_years[['Year',
                             'Units_Sold_Millions',
                             'Revenue_Billions',
                             'Predicted_Units_Sold_Millions',
                             'Predicted_Revenue_Billions',
                             'Type']]

# Combine historical and predicted data
final_df = pd.concat([df, future_years], ignore_index=True)

# Save forecast output
final_df.to_csv("final_sales_revenue_2036.csv", index=False)

print("Forecast and final combined dataset saved successfully!")

# -------------------------
# OPTIONAL GRAPH
# -------------------------
plt.figure(figsize=(8,5))

plt.plot(df['Year'], df['Units_Sold_Millions'], marker='o')
plt.plot(future_years['Year'], future_years['Predicted_Units_Sold_Millions'], marker='o')

plt.xlabel("Year")
plt.ylabel("Units Sold (Millions)")
plt.title("iPhone Sales Forecast Till 2036")

plt.show()
