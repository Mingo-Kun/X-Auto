import openai
from config.config import OPENROUTER_API_KEY
from src.bot.trend_tracker import TrendTracker

class AIHandler:
    def __init__(self):
        # Configure the OpenRouter API
        try:
            self.client = openai.OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=OPENROUTER_API_KEY,
            )
            # Set the specific model to use
            self.model = "qwen/qwen3-30b-a3b:free"
        except Exception as e:
            print(f"Error initializing OpenRouter client: {str(e)}")
            self.client = None
            self.model = None
        
        self.trend_tracker = TrendTracker()

    def _trim_to_tweet_length(self, text):
        """Trim text to fit Twitter's character limit"""
        return text[:280] if text else ""

    def generate_tweet(self):
        """Generate a tweet using OpenRouter AI focused on crypto/Web3 trends"""
        if not self.client or not self.model:
            print("AI client not initialized")
            return None

        trends = self.trend_tracker.get_all_trends()
        
        prompt = f"""Generate an engaging tweet about one of these trending topics in cryptocurrency or Web3:
Trending Crypto: {', '.join(trends['crypto'])}
Trending Web3: {', '.join(trends['web3'])}

The tweet should:
- Be informative and insightful
- Include relevant facts or analysis
- Be under 280 characters
- Optionally include 1-2 relevant hashtags
- Focus on market analysis, technology developments, or industry impact
- Maintain a professional tone

Return only the tweet text without any additional formatting or quotes."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                # max_tokens=150, # Adjust based on typical tweet length
            )
            tweet = response.choices[0].message.content.strip()
            return self._trim_to_tweet_length(tweet)
        except Exception as e:
            print(f"Error generating tweet: {str(e)}")
            return None

    def generate_reply(self, tweet_content):
        """Generate a reply to a tweet using OpenRouter AI with crypto/Web3 focus"""
        if not self.client or not self.model:
            print("AI client not initialized")
            return None

        trends = self.trend_tracker.get_all_trends()
        
        prompt = f"""Generate a reply to this tweet: '{tweet_content}'

Consider these current trends while crafting your response:
Crypto Trends: {', '.join(trends['crypto'])}
Web3 Trends: {', '.join(trends['web3'])}

The reply should:
- Be under 280 characters
- Be relevant to both the original tweet and current trends
- Add value through insight or analysis
- Be professional and engaging
- Include market context if relevant
- Optionally include a relevant hashtag

Return only the reply text without any formatting or quotes."""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                # max_tokens=150, # Adjust based on typical reply length
            )
            reply = response.choices[0].message.content.strip()
            return self._trim_to_tweet_length(reply)
        except Exception as e:
            print(f"Error generating reply: {str(e)}")
            return None

    def should_engage(self, tweet_content):
        """Determine if we should engage with a tweet based on relevance to our topics"""
        if not self.client or not self.model:
            print("AI client not initialized")
            return False

        prompt = f"""Analyze this tweet: '{tweet_content}'

Determine if it's relevant to cryptocurrency, blockchain, or Web3.
Return only 'yes' or 'no' based on:
- Contains crypto/blockchain terminology
- Discusses Web3 technologies
- Mentions relevant projects or platforms
- Discusses market trends or technology developments
"""
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                     {"role": "user", "content": prompt}
                ],
                 # max_tokens=10, # Expecting a short answer
            )
            # OpenRouter might return more than just 'yes' or 'no', so we check if 'yes' is in the response
            return 'yes' in response.choices[0].message.content.strip().lower()
        except Exception as e:
            print(f"Error in engagement analysis: {str(e)}")
            return False