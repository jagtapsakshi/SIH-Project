import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import pickle


# Load the dataset from a CSV file
file_name = 'dataset.csv'  # Replace with the name of your CSV file
df = pd.read_csv('dataset.csv')

# Identify and label encode non-numeric categorical columns
label_encoder = LabelEncoder()
categorical_columns = ['Label']  # Replace with the actual column names
for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])

# Split the dataset into features and labels
X = df.drop('Label', axis=1)
y = df['Label']

# Initialize and train a Random Forest classifier (you can try different models)
model = RandomForestClassifier()
model.fit(X, y)

# Rest of your code for making recommendations


# Function to recommend a career based on user choices and weights
def recommend_career(choice1_weight, choice2_weight, choice3_weight,choice4_weight,choice5_weight,choice6_weight,choice7_weight,choice8_weight,choice9_weight,choice10_weight,choice11_weight,choice12_weight,choice13_weight,choice14_weight,choice15_weight,choice16_weight,choice17_weight,choice18_weight,):
    user_choices = pd.DataFrame({
        'Choice1Weight': [choice1_weight],
        'Choice2Weight': [choice2_weight],
        'Choice3Weight': [choice3_weight],
        'Choice4Weight': [choice4_weight],
        'Choice5Weight': [choice5_weight],
        'Choice6Weight': [choice6_weight],
        'Choice7Weight': [choice7_weight],
        'Choice8Weight': [choice8_weight],
        'Choice9Weight': [choice9_weight],
        'Choice10Weight': [choice10_weight],
        'Choice11Weight': [choice11_weight],
        'Choice12Weight': [choice12_weight],
        'Choice13Weight': [choice13_weight],
        'Choice14Weight': [choice14_weight],
        'Choice15Weight': [choice15_weight],
        'Choice16Weight': [choice16_weight],
        'Choice17Weight': [choice17_weight],
        'Choice18Weight': [choice18_weight],
    })
    
    predicted_career = model.predict(user_choices)
    print("Shape of arr:", user_choices.shape)
    print("Data type of arr:", user_choices.dtype)  
    return predicted_career[0]

# Example usage
choice1_weight = 18  # Replace with the user's actual choice weights
choice2_weight = 19
choice3_weight = 20
choice4_weight = 14
choice5_weight = 14
choice6_weight = 21
choice7_weight = 18
choice8_weight = 18
choice9_weight = 18
choice10_weight =11 
choice11_weight = 17
choice12_weight = 19
choice13_weight = 20
choice14_weight = 19
choice15_weight = 16
choice16_weight = 18
choice17_weight = 16
choice18_weight = 20


recommended_career_numerical = recommend_career(choice1_weight, choice2_weight, choice3_weight,choice4_weight,choice5_weight,choice6_weight,choice7_weight,choice8_weight,choice9_weight,choice10_weight,choice11_weight,choice12_weight,choice13_weight,choice14_weight,choice15_weight,choice16_weight,choice17_weight,choice18_weight)
recommended_career = label_encoder.inverse_transform([recommended_career_numerical])




print(f"Based on your choices, we recommend a career in {recommended_career[0]}.")
