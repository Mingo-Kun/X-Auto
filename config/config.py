import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API Credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# Verify Twitter credentials are set
required_twitter_vars = [
    'TWITTER_API_KEY',
    'TWITTER_API_SECRET',
    'TWITTER_ACCESS_TOKEN',
    'TWITTER_ACCESS_TOKEN_SECRET',
    'TWITTER_BEARER_TOKEN'
]

missing_vars = [var for var in required_twitter_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required Twitter environment variables: {', '.join(missing_vars)}")

# OpenRouter API Credentials
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set")

# Bot Configuration
TWEET_INTERVAL = 6  # Hours between tweets
MAX_TWEETS_PER_DAY = 4
MAX_REPLIES_PER_DAY = 10