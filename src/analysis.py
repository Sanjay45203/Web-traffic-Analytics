import pandas as pd

def load_data(path="data/web_traffic_sessions.csv"):
    return pd.read_csv(path, parse_dates=["date"])

def kpis(df):
    n=len(df)
    return {
        "sessions": n,
        "bounce_rate": df["bounce"].mean(),
        "engagement_rate": df["engaged"].mean(),
        "avg_pages_per_session": df["pages_viewed"].mean(),
        "avg_session_duration_sec": df["session_duration_sec"].mean(),
        "signup_conversion_rate": df["signup_complete"].mean(),
    }

def channel_summary(df):
    return df.groupby("channel").agg(
        sessions=("session_id","count"), bounce_rate=("bounce","mean"),
        engagement_rate=("engaged","mean"), avg_pages=("pages_viewed","mean"),
        avg_duration_sec=("session_duration_sec","mean"),
        signups=("signup_complete","sum"), conversion_rate=("signup_complete","mean")
    ).sort_values("sessions",ascending=False)

def landing_page_summary(df):
    return df.groupby("landing_page").agg(
        sessions=("session_id","count"), bounce_rate=("bounce","mean"),
        avg_pages=("pages_viewed","mean"), avg_duration_sec=("session_duration_sec","mean"),
        conversion_rate=("signup_complete","mean")
    ).sort_values("sessions",ascending=False)

def funnel(df):
    users=[len(df),df.product_view.sum(),df.pricing_view.sum(),
           df.signup_start.sum(),df.signup_complete.sum()]
    out=pd.DataFrame({"stage":["Sessions","Product View","Pricing View","Signup Started","Signup Completed"],
                      "users":users})
    out["dropoff_from_previous"]=1-out.users.div(out.users.shift(1))
    return out
