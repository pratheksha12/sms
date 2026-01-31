import pandas as pd

# Load dataset
df = pd.read_csv("/data/SMSSpam.csv")

print(df.head())
print(df['label'].value_counts())
print(df.isnull().sum())
