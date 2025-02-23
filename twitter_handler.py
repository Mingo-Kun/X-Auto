import tweepy
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET
)

class TwitterHandler:
    def __init__(self):
        # Authenticate with Twitter
        self.auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
        )

    def post_tweet(self, content):
        """Post a tweet"""
        try:
            response = self.api.create_tweet(text=content)
            return response
        except Exception as e:
            print(f"Error posting tweet: {str(e)}")
            return None

    def post_reply(self, tweet_id, content):
        """Reply to a tweet"""
        try:
            response = self.api.create_tweet(
                text=content,
                in_reply_to_tweet_id=tweet_id
            )
            return response
        except Exception as e:
            print(f"Error posting reply: {str(e)}")
            return None

    def get_mentions(self, since_id=None):
        """Get mentions of the bot"""
        try:
            mentions = self.api.get_users_mentions(
                id=self.api.get_me()[0].id,
                since_id=since_id
            )
            return mentions.data if mentions.data else []
        except Exception as e:
            print(f"Error getting mentions: {str(e)}")
            return []