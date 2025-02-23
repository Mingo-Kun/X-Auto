# X-Auto Bot

An AI-powered X (Twitter) bot that automatically generates and posts tweets and replies about cryptocurrency, blockchain, and Web3 topics using Google's Gemini AI.

## Features

- Automated tweet generation focused on crypto/Web3 trends
- AI-powered replies to relevant mentions
- Real-time tracking of trending cryptocurrencies and Web3 topics
- Smart engagement filtering for crypto-related content
- Rate limiting and daily limits
- Error handling and recovery

## Project Structure

```
X-Auto/
├── src/               # Source code
│   ├── bot/          # Bot components
│   │   ├── twitter_handler.py
│   │   ├── ai_handler.py
│   │   └── trend_tracker.py
│   └── main.py       # Main entry point
├── config/           # Configuration
│   └── config.py
├── tests/            # Test files
├── .env.example      # Example environment variables
├── requirements.txt  # Python dependencies
└── README.md        # Documentation
```

## Setup

1. Clone the repository
```bash
git clone https://github.com/Mingo-Kun/X-Auto.git
cd X-Auto
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example` and fill in your API keys:
```env
# Twitter API Credentials
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# Gemini API Credentials
GEMINI_API_KEY=your_gemini_api_key
```

5. Run the bot
```bash
python src/main.py
```

## Configuration

You can modify the bot's behavior by adjusting the following parameters in `config