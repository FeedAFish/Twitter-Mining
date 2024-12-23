import tweepy
import config
import json

# Replace with your credentials
BEARER_TOKEN = config.bearer_token
# Authenticate with the Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Define your search query and parameters
query = "Python programming"
max_results = 10  # Number of tweets to fetch (10-100)

# Call the search_recent_tweets method

response = client.search_recent_tweets(
    query=query,
    max_results=max_results,
    tweet_fields=["id", "text", "created_at"],  # Additional fields to include
)

# Process and print the response
if response.data:
    for tweet in response.data:
        print(
            f"Tweet ID: {tweet.id}, Created At: {tweet.created_at}, Text: {tweet.text}"
        )
        # json.dump(tweet, open("tweet.json", "w"))
else:
    print("No recent tweets found for the query.")
