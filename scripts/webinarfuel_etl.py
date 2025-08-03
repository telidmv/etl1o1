"""
ETL script for Webinarfuel
"""

import pandas as pd
import psycopg2

def load_webinar_csv(filepath):
    df = pd.read_csv(filepath)
    df.columns = [c.lower().replace(' ', '_') for c in df.columns]
    return df

def save_to_db(df, table_name):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (email, webinar_name, attended, watch_time, date)
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    conn.close()

df = load_webinar_csv("webinarfuel_attendance.csv")
save_to_db(df, 'webinarfuel_attendance')


