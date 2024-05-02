from pyparsing import Literal
from twikit import Client
from twikit import utils
import csv
from credentials import password, email, username

USERNAME = username
EMAIL = email
PASSWORD = password

# Initialize client
client = Client('en-US')
# Login to the service with provided user credentials
client.login(
    auth_info_1=USERNAME ,
    auth_info_2=EMAIL,
    password=PASSWORD
)

searchOptions = utils.SearchOptions(since='2023-10-07', until='2023-10-08')
searchQuery = utils.build_query(text='quds', options=searchOptions)

tweets = client.search_tweet(query='jerusalem',product='Top', count=50)

tweet_data = []
for tweet in tweets:
    tweet_info = {
        'id': tweet.id,
        'text': tweet.text,
        'created_at': tweet.created_at,
        'user': tweet.user,
        'lang': tweet.lang,
        'is_quote_status': tweet.is_quote_status,
        'possibly_sensitive': tweet.possibly_sensitive,
        'quote_count': tweet.quote_count,
        'reply_count': tweet.reply_count,
        'favorite_count': tweet.favorite_count,
        'favorited': tweet.favorited,
        'view_count': tweet.view_count,
        'retweet_count': tweet.retweet_count,
        'is_transatable': tweet.is_translatable,
        'state': tweet.state,
        'replies': tweet.replies,
        #'media': tweet.media,
    }
    tweet_data.append(tweet_info)


# Search more tweets
more_tweets = tweets.next()

# Save data to CSV file
csv_file_path = 'tweets_data.csv'
csv_columns = ['id', 'text', 'is_quote_status', 'favorite_count', 'retweet_count', 'is_transatable', 'lang', 'view_count', 'replies', 'reply_count', 'state', 'possibly_sensitive', 'created_at', 'quote_count', 'favorited', 'user']

with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)

 # Write header
    writer.writeheader()
    
    # Write data
    i=0
    for data in tweet_data:
        i = i + 1
        writer.writerow(data)

print(f'Tweet data has been saved to {csv_file_path}')
print('number of rows===============', i)


#trends = client.get_trends('trending')

#for trend in trends:

#    print(trend)




