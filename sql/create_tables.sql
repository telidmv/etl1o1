-- Meta Ads
CREATE TABLE meta_ads_insights (
    id SERIAL PRIMARY KEY,
    campaign_name TEXT,
    ad_name TEXT,
    impressions INTEGER,
    clicks INTEGER,
    spend NUMERIC(10,2),
    reach INTEGER,
    ctr NUMERIC(5,2),
    cpc NUMERIC(10,2),
    cpm NUMERIC(10,2),
    date_loaded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- GoHighLevel
CREATE TABLE ghl_leads (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    source TEXT,
    created_at TIMESTAMP
);

-- Stripe
CREATE TABLE stripe_payments (
    id SERIAL PRIMARY KEY,
    charge_id TEXT,
    email TEXT,
    amount NUMERIC(10,2),
    currency TEXT,
    created TIMESTAMP,
    status TEXT
);

-- Webinarfuel
CREATE TABLE webinarfuel_attendance (
    id SERIAL PRIMARY KEY,
    email TEXT,
    webinar_name TEXT,
    attended BOOLEAN,
    watch_time INTEGER,
    date TIMESTAMP
);
