import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
# Read the Excel file
chomage = pd.read_excel("dataset.xlsx", index_col="effectif de trimestre")

# Clean up column names by removing extra spaces
chomage.columns = chomage.columns.str.strip()

# Define the predictors and target variable
predictors = ["Urbain", "Rural",  "Féminin", "Sans diplôme",
              "Ayant un diplôme:  Niveau moyen",
              "Ayant un diplôme:  Niveau supérieur"
               ,"25 - 34",'35 - 44',"45 et plus"]
target = "Masculin" 

# Split the data into training and testing sets
train = chomage.loc["2021T4":]
test = chomage.loc[:"2022T1"]
# Create and fit the Ridge regression model
reg = Ridge(alpha=0.1)
reg.fit(train[predictors], train[target])

# Make predictions on the testing set
predictions = reg.predict(test[predictors])

# Calculate mean absolute error
mae = mean_absolute_error(test[target], predictions)
print(f"Mean Absolute Error: {mae}")

# Evaluating:
combined = pd.concat([test[target], pd.Series(predictions, index=test.index)], axis=1)
combined.columns = ['actual', 'prediction']
print(combined)
combined.plot()
plt.show()

print(reg.coef_)

# Calcul du R-squared 
r2 = reg.score(test[predictors], test[target])
print(r2)

# Now let's predict future values 
future_periods = pd.date_range(start='2023T4', end='2032T3', freq='Q')
predictors_future = chomage.loc['2023T3':][predictors]
predictions_future = reg.predict(predictors_future)
predictions_df = pd.DataFrame(predictions_future, index=future_periods, columns=['Predicted_masculin'])


# Specify the path where you want to save the Excel file
excel_file_path = 'predicted_values_masculin.xlsx'
# Save the DataFrame to an Excel file
predictions_df.to_excel(excel_file_path)
#plot
predictions_df.plot(title='Predicted masculin Values Over Time')
plt.show()
plt.plot(chomage.index, reg.predict(chomage[predictors]), 
         label='Regression Line', linestyle='--')