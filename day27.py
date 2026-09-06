import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import streamlit as st

df = pd.read_csv("social_media.csv")
print(df.head())

#top 5 hashtags
top = df["Hashtag"].value_counts().sort_values(ascending = False)
print(top.head(5))

#Analyze the most active users
active_users = df["User"].value_counts().sort_values(ascending=False)
print(active_users.head(5))

#Calculate engagement (Likes, Comments & Shares)
engagement = df.groupby("User")[["Likes","Comments","Shares"]].sum()
print(engagement)

#Detect the most popular posting time
df["Post_DateTime"] = pd.to_datetime(df["Post_DateTime"])
df["hour"] = df["Post_DateTime"].dt.hour
posting_time = df["hour"].value_counts().sort_values(ascending=False)
print(posting_time.head(1))

#Top Hashtags Chart
top_ = top.head(5)
plt.bar(top_.index , top_.values)
plt.title("Top Hashtags Chart")
plt.xlabel("hashtag")
plt.ylabel("value")
plt.show()

# Daily Engagement Trend
plt.plot(posting_time.index , posting_time.values)
plt.title("Daily Engagement Trend")
plt.xlabel("index")
plt.ylabel("value")
plt.show()

#Content Category Distribution
category = df["Content_Category"].value_counts()
plt.pie(category.values, labels=category.index)
plt.title("Content Category Distribution")
plt.show()

#Export the analytics report as a CSV
report = pd.DataFrame({
    "User": engagement.index,
    "Likes": engagement["Likes"].values,
    "Comments": engagement["Comments"].values,
    "Shares": engagement["Shares"].values,
})

report.to_csv("analytics_report.csv", index=False)

#sentiment analysis
def sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Post_Text"].apply(sentiment)

print(df[["Post_Text", "Sentiment"]].head())

#streamlit

st.title("📱 Social Media Trend Analyzer")

df = pd.read_csv("social_media.csv")

# Sidebar filters
st.sidebar.header("Filters")

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["Content_Category"].unique())
)

if category != "All":
    df = df[df["Content_Category"] == category]

# Search
search = st.text_input("🔍 Search Posts")

if search:
    df = df[
        df["Post_Text"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.subheader("Filtered Data")
st.dataframe(df)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Posts", len(df))
col2.metric("Total Likes", df["Likes"].sum())
col3.metric("Total Shares", df["Shares"].sum())

# Hashtags
st.subheader("🔥 Top Hashtags")

top_hashtags = df["Hashtag"].value_counts().head(5)

st.bar_chart(top_hashtags)

# Category
st.subheader("📊 Content Categories")

category_count = df["Content_Category"].value_counts()

st.bar_chart(category_count)