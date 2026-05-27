import pandas as pd
import matplotlib.pyplot as plt

# Dataset
movies = {
    "Movie": ["Avatar", "Bahubali", "Dangal", "Pushpa", "KGF"],
    "Rating": [8.1, 8.2, 8.4, 7.9, 8.3],
    "Genre": ["Sci-Fi", "Action", "Drama", "Thriller", "Action"],
    "Revenue": [2900, 650, 300, 350, 500]
}
df = pd.DataFrame(movies)

# Display Dataset
print("Movie Dataset:\n",df)

# Highest Rated Movies
print("\nHighest Rated Movies:")
highest_rated = df.sort_values(by="Rating", ascending=False)
print(highest_rated[["Movie", "Rating"]])

# Most Profitable Genres
genre_profit = df.groupby("Genre")["Revenue"].sum()

print("\nMost Profitable Genres:\n",genre_profit)

# Correlation Between Rating & Revenue
correlation = df["Rating"].corr(df["Revenue"])
print("\nCorrelation between Rating and Revenue:", correlation)

# Top 5 Movies
top_movies = df.sort_values(by="Revenue", ascending=False).head(5)

print("\nTop 5 Movies by Revenue:")
print(top_movies[["Movie", "Revenue"]])

# Genre vs Revenue Bar Chart
plt.figure(figsize=(7,5))
genre_profit.plot(kind="bar", color="purple")
plt.title("Genre vs Revenue")
plt.xlabel("Genre")
plt.ylabel("Revenue")
plt.show()

# Rating Distribution Histogram
plt.figure(figsize=(7,5))
plt.hist(df["Rating"], bins=5, color="cyan", edgecolor="black")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# Rating vs Revenue Scatter Plot
plt.figure(figsize=(7,5))
plt.scatter(df["Rating"], df["Revenue"], color="green", s=120)
plt.title("Correlation between Rating & Revenue")
plt.xlabel("Rating")
plt.ylabel("Revenue")
plt.show()