import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the dataset from a CSV file
file_name = 'dataset.csv'  # Replace with the name of your CSV file
df = pd.read_csv('dataset.csv')

# Identify and label encode non-numeric categorical columns
# label_encoder = LabelEncoder()
# categorical_columns = ['Label']  # Replace with the actual column names  #attch comment out kelay
# for column in categorical_columns:
#     df[column] = label_encoder.fit_transform(df[column])

# Split the dataset into features and labels
X = df.drop('Label', axis=1)
y = df['Label'].ravel()

# feature_names = [Choice1Weight,Choice2Weight,Choice3Weight,Choice4Weight,Choice5Weight,Choice6Weight,Choice7Weight,Choice8Weight,Choice9Weight,Choice10Weight,Choice11Weight,Choice12Weight,Choice13Weight,Choice14Weight,Choice15Weight,Choice16Weight,Choice17Weight,Choice18Weight]

#feature_names = list(X.columns)

X = X.to_numpy()
# Initialize and train a Random Forest classifier (you can try different models)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


with open('final_deploy.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)


# Function to recommend a career based on user choices and weights
# def recommend_career():
#     choice_weights = []
#     num_choices = 18  # Update this to the actual number of choices
#     for i in range(1, num_choices + 1):
#         weight = float(input(f"Enter weight for Choice{i}: "))
#         choice_weights.append(weight)
    
#     # Create feature names dynamically
#     feature_names = [f'Choice{i}Weight' for i in range(1, num_choices + 1)]
    
#     user_choices = pd.DataFrame({feature_names[i-1]: [choice_weights[i-1]] for i in range(1, num_choices + 1)})
    
#     predicted_career_numerical = model.predict(user_choices)
#     predicted_career = label_encoder.inverse_transform([predicted_career_numerical])
    
#     return predicted_career[0]

# # Get user input for choice weights
# print("Enter weights for each choice (1-18):")
# recommended_career = recommend_career()

#print(f"Based on your choices, we recommend a career in {recommended_career}.")
