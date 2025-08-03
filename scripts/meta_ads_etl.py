"""
ETL script for Meta Ads
"""

import requests
import pandas as pd
import psycopg2
from datetime import datetime, timedelta

ACCESS_TOKEN = 'META_ACCESS_TOKEN'
AD_ACCOUNT_ID = 'act_XXXXXX'
API_VERSION = 'v18.0'

def get_meta_ads_data():
    url = f"https://graph.facebook.com/{API_VERSION}/{AD_ACCOUNT_ID}/insights"
    params = {
        'access_token': ACCESS_TOKEN,
        'level': 'ad',
        'fields': 'campaign_name,ad_name,impressions,clicks,spend,reach,ctr,cpc,cpm',
        'date_preset': 'last_7d',
        'limit': 500
    }

    response = requests.get(url, params=params)
    data = response.json()['data']
    df = pd.DataFrame(data)
    return df

def save_to_db(df, table_name):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (campaign_name, ad_name, impressions, clicks, spend, reach, ctr, cpc, cpm, date_loaded)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, now())
        """, tuple(row))
    conn.commit()
    conn.close()

df = get_meta_ads_data()
save_to_db(df, 'meta_ads_insights')
