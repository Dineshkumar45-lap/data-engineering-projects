import pandas as pd

# Extract
df = pd.read_csv('data/user_data.csv')

# Transform
df = df.dropna()
df['activity_time'] = pd.to_datetime(df['activity_time'])
df['activity_date'] = df['activity_time'].dt.date

# Load
df.to_csv('data/cleaned_user_data.csv', index=False)

print("ETL Completed")
