"""
ETL script for GoHighLevel
"""

import requests
import pandas as pd
import psycopg2

GHL_API_KEY = 'your_ghl_key'
BASE_URL = 'https://rest.gohighlevel.com/v1'

def get_leads():
    headers = {'Authorization': f'Bearer {GHL_API_KEY}'}
    response = requests.get(f"{BASE_URL}/contacts/", headers=headers)
    data = response.json()['contacts']
    df = pd.DataFrame(data)
    return df[['firstName', 'lastName', 'email', 'phone', 'source', 'createdAt']]

def save_to_db(df, table_name):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (first_name, last_name, email, phone, source, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    conn.close()

df = get_leads()
save_to_db(df, 'ghl_leads')
