import pandas as pd

def load_data():
    return pd.read_csv('data/raw_sales.csv')

def clean_data(df):
    df = df[df['quantity'] > 0]
    df = df[df['price'] > 0]
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['quantity'] * df['price']
    return df

def save_data(df):
    df.to_csv('data/cleaned_sales.csv', index=False)

def main():
    df = load_data()
    cleaned_df = clean_data(df)
    save_data(cleaned_df)
    print("Pipeline executed successfully")

if __name__ == "__main__":
    main()
