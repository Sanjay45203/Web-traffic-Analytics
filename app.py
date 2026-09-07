import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Web Traffic Analytics",page_icon="📊",layout="wide")
st.title("📊 Web Traffic Analytics Dashboard")
st.caption("Google Analytics-style sample data • sessions • page paths • funnel • engagement")

df=pd.read_csv(Path(__file__).parent/"data/web_traffic_sessions.csv",parse_dates=["date"])

with st.sidebar:
    st.header("Filters")
    channels=st.multiselect("Traffic source",sorted(df.channel.unique()),default=sorted(df.channel.unique()))
    devices=st.multiselect("Device",sorted(df.device.unique()),default=sorted(df.device.unique()))
    dr=st.date_input("Date range",(df.date.min().date(),df.date.max().date()),
                     min_value=df.date.min().date(),max_value=df.date.max().date())

d=df[df.channel.isin(channels)&df.device.isin(devices)&df.date.dt.date.between(dr[0],dr[1])]

c=st.columns(5)
c[0].metric("Sessions",f"{len(d):,}")
c[1].metric("Bounce rate",f"{d.bounce.mean():.1%}")
c[2].metric("Engagement rate",f"{d.engaged.mean():.1%}")
c[3].metric("Avg pages/session",f"{d.pages_viewed.mean():.2f}")
c[4].metric("Signup conversion",f"{d.signup_complete.mean():.1%}")

a,b=st.columns(2)
with a:
    x=d.groupby("channel").size().reset_index(name="sessions").sort_values("sessions",ascending=False)
    st.plotly_chart(px.bar(x,x="channel",y="sessions",text_auto=True,title="Sessions by Traffic Source"),use_container_width=True)
with b:
    x=d.groupby("landing_page").bounce.mean().reset_index(name="bounce_rate").sort_values("bounce_rate",ascending=False)
    fig=px.bar(x,x="landing_page",y="bounce_rate",text_auto=".1%",title="Bounce Rate by Landing Page")
    fig.update_yaxes(tickformat=".0%")
    st.plotly_chart(fig,use_container_width=True)

st.subheader("Funnel Analysis")
f=pd.DataFrame({"Stage":["Sessions","Product View","Pricing View","Signup Started","Signup Completed"],
                "Users":[len(d),d.product_view.sum(),d.pricing_view.sum(),d.signup_start.sum(),d.signup_complete.sum()]})
f["Drop-off"]=1-f.Users.div(f.Users.shift(1))
st.plotly_chart(px.funnel(f,y="Stage",x="Users",title="User Conversion Funnel"),use_container_width=True)
st.dataframe(f.style.format({"Drop-off":"{:.1%}"}),use_container_width=True)

a,b=st.columns(2)
with a:
    sample=d.sample(min(2000,len(d)),random_state=42)
    st.plotly_chart(px.scatter(sample,x="session_duration_sec",y="pages_viewed",color="channel",
        hover_data=["device","landing_page"],title="Session Duration vs Pages Viewed"),use_container_width=True)
with b:
    x=d.groupby("device").agg(bounce_rate=("bounce","mean"),conversion=("signup_complete","mean")).reset_index()
    fig=px.bar(x,x="device",y=["bounce_rate","conversion"],barmode="group",title="Device Performance")
    fig.update_yaxes(tickformat=".0%")
    st.plotly_chart(fig,use_container_width=True)

st.subheader("Top Landing Pages")
x=d.groupby("landing_page").agg(sessions=("session_id","count"),bounce_rate=("bounce","mean"),
    avg_pages=("pages_viewed","mean"),avg_duration_sec=("session_duration_sec","mean"),
    conversion=("signup_complete","mean")).reset_index().sort_values("sessions",ascending=False)
st.dataframe(x.style.format({"bounce_rate":"{:.1%}","avg_pages":"{:.2f}",
                             "avg_duration_sec":"{:.1f}","conversion":"{:.1%}"}),use_container_width=True)

st.subheader("Monthly Traffic Trend")
x=d.assign(month=d.date.dt.to_period("M").astype(str)).groupby("month").size().reset_index(name="sessions")
st.plotly_chart(px.line(x,x="month",y="sessions",markers=True,title="Sessions Over Time"),use_container_width=True)
