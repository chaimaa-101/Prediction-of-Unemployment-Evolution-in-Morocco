import pandas as pd
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

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

# Create and fit the SVM regression model
svm_model = SVR(kernel='linear', C=1.0)
svm_model.fit(train[predictors], train[target])

# Make predictions on the testing set
predictions_svm = svm_model.predict(test[predictors])

# Calculate mean absolute error
mae_svm = mean_absolute_error(test[target], predictions_svm)
print(f"Mean Absolute Error (SVM): {mae_svm}")

# Evaluate and plot the results
combined_svm = pd.concat([test[target], pd.Series(predictions_svm, index=test.index)], 
                         axis=1)
combined_svm.columns = ['Actual', 'Prediction']
print(combined_svm)
combined_svm.plot(title='Actual and Predicted Values Over Time (SVM)')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.show()

# Calculate R-squared 
r2_svm = r2_score(test[target], predictions_svm)
print(f"R-squared (SVM): {r2_svm}")

# Now let's predict future values 
future_periods = pd.date_range(start='2023T4', end='2032T3', freq='Q')
predictors_future = chomage.loc['2023T3':][predictors]
predictions_future = svm_model.predict(predictors_future)
predictions_df = pd.DataFrame(predictions_future, index=future_periods, 
                              columns=['Predicted_masculin'])
# Specify the path where you want to save the Excel file
excel_file_path = 'predicted_values_svm.xlsx'
# Plotting
predictions_df.plot(title='Predicted masculin Values Over Time')
plt.show()
plt.plot(chomage.index, svm_model.predict(chomage[predictors]), 
         label='SVM Predictions', linestyle='--')
