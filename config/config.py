import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API Credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Gemini API Credentials
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Bot Configuration
TWEET_INTERVAL = 4  # Hours between tweets
MAX_TWEETS_PER_DAY = 24
MAX_REPLIES_PER_DAY = 50