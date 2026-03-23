# src/data_cleaning.py
import os
import pandas as pd

def clean_data(file_path):
    """
    Reads the Excel dataset, removes duplicates, converts date column,
    and adds useful columns for metrics calculation.
    """
    # Read Excel file
    df = pd.read_excel(file_path)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    # Add useful columns for metrics
    df['month'] = df['InvoiceDate'].dt.to_period('M')        # Month-wise
    df['week'] = df['InvoiceDate'].dt.isocalendar().week    # Week-wise
    df['day'] = df['InvoiceDate'].dt.date                    # Day-wise for DAU
    
    # Optional: remove rows with missing Customer ID
    df = df[df['Customer ID'].notna()]
    
    return df

if __name__ == "__main__":
    # Absolute paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # StartupMetricsDashboard folder
    raw_file = os.path.join(BASE_DIR, "data", "raw", "user_activity.xlsx")
    processed_file = os.path.join(BASE_DIR, "data", "processed", "processed_data.csv")
    
    # Make sure processed folder exists
    os.makedirs(os.path.dirname(processed_file), exist_ok=True)
    
    # Safety check
    if not os.path.exists(raw_file):
        raise FileNotFoundError(f"File not found: {raw_file}")
    
    # Clean the data
    df = clean_data(raw_file)
    
    # Save cleaned dataset
    df.to_csv(processed_file, index=False)
    print("✅ Data cleaned and saved to processed folder.")