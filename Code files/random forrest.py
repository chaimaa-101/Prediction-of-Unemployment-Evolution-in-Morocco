import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score
import matplotlib.pyplot as plt
# Read the Excel file
chomage = pd.read_excel("Dataset.xlsx", index_col="effectif de trimestre")
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

# Random Forest Regression
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(train[predictors], train[target])
predictions_rf = rf_model.predict(test[predictors])

# Calculate mean absolute error for Random Forest Regression
mae_rf = mean_absolute_error(test[target], predictions_rf)
print(f"Mean Absolute Error (Random Forest): {mae_rf}")

# Evaluate and plot the results for Random Forest Regression
combined_rf = pd.concat([
    test[target],
    pd.Series(predictions_rf, index=test.index, name="Prediction_RF"),
], axis=1)
print(combined_rf)
combined_rf.plot()
plt.show()

#R2 score 
r2_rf = r2_score(test[target], predictions_rf)
print(f"R-squared (Random Forest): {r2_rf}")

# Now let's predict future values 
future_periods = pd.date_range(start='2023T4', end='2032T3', freq='Q')
predictors_future = chomage.loc['2023T3':][predictors]
predictions_future = rf_model.predict(predictors_future)
predictions_df = pd.DataFrame(predictions_future, index=future_periods, columns=['Predicted_Masculin'])

# Specify the path where you want to save the Excel file
excel_file_path = 'predicted_values_Masculin.xlsx'

# Save the DataFrame to an Excel file
predictions_df.to_excel(excel_file_path)

# Plotting
predictions_df.plot(title='Predicted Masculin Values Over Time')
plt.show()