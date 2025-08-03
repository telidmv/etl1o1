"""
ETL script for Stripe
"""

import stripe
import pandas as pd
import psycopg2

stripe.api_key = "your_stripe_secret_key"

def get_payments():
    charges = stripe.Charge.list(limit=100)
    records = []
    for c in charges.auto_paging_iter():
        records.append({
            'charge_id': c.id,
            'email': c.billing_details.email,
            'amount': c.amount / 100,
            'currency': c.currency,
            'created': datetime.fromtimestamp(c.created),
            'status': c.status
        })
    return pd.DataFrame(records)

def save_to_db(df, table_name):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(f"""
            INSERT INTO {table_name} (charge_id, email, amount, currency, created, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, tuple(row))
    conn.commit()
    conn.close()

df = get_payments()
save_to_db(df, 'stripe_payments')
