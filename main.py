import time
import schedule
import asyncio
from datetime import datetime
from twitter_handler import TwitterHandler
from ai_handler import AIHandler
from config import TWEET_INTERVAL, MAX_TWEETS_PER_DAY, MAX_REPLIES_PER_DAY

class TwitterBot:
    def __init__(self):
        self.twitter = TwitterHandler()
        self.ai = AIHandler()
        self.tweet_count = 0
        self.reply_count = 0
        self.last_mention_id = None

    async def post_scheduled_tweet(self):
        """Post a scheduled tweet about crypto/Web3 trends"""
        if self.tweet_count >= MAX_TWEETS_PER_DAY:
            print("Maximum daily tweet limit reached")
            return

        tweet_content = await self.ai.generate_tweet()
        if tweet_content:
            response = self.twitter.post_tweet(tweet_content)
            if response:
                self.tweet_count += 1
                print(f"Tweet posted successfully: {tweet_content}")

    async def check_and_reply_to_mentions(self):
        """Check for mentions and reply if relevant to crypto/Web3"""
        if self.reply_count >= MAX_REPLIES_PER_DAY:
            print("Maximum daily reply limit reached")
            return

        mentions = self.twitter.get_mentions(self.last_mention_id)
        for mention in mentions:
            if self.reply_count >= MAX_REPLIES_PER_DAY:
                break

            # Check if the tweet is relevant to our topics
            should_reply = await self.ai.should_engage(mention.text)
            if should_reply:
                reply_content = await self.ai.generate_reply(mention.text)
                if reply_content:
                    response = self.twitter.post_reply(mention.id, reply_content)
                    if response:
                        self.reply_count += 1
                        self.last_mention_id = mention.id
                        print(f"Reply posted successfully: {reply_content}")
            else:
                print(f"Skipping irrelevant mention: {mention.text[:100]}...")

    def reset_daily_counts(self):
        """Reset daily tweet and reply counts"""
        self.tweet_count = 0
        self.reply_count = 0
        print("Daily counts reset")

    async def run_scheduled_task(self, task):
        """Run a scheduled task"""
        if task == "tweet":
            await self.post_scheduled_tweet()
        elif task == "check_mentions":
            await self.check_and_reply_to_mentions()
        elif task == "reset_counts":
            self.reset_daily_counts()

    def run(self):
        """Run the bot"""
        loop = asyncio.get_event_loop()
        
        def schedule_wrapper(task):
            asyncio.run_coroutine_threadsafe(self.run_scheduled_task(task), loop)

        # Schedule tweets
        schedule.every(TWEET_INTERVAL).hours.do(lambda: schedule_wrapper("tweet"))
        # Schedule mention checks
        schedule.every(15).minutes.do(lambda: schedule_wrapper("check_mentions"))
        # Schedule daily reset
        schedule.every().day.at("00:00").do(lambda: schedule_wrapper("reset_counts"))

        print("Bot started successfully!")
        print("Focusing on Cryptocurrency, Blockchain, and Web3 topics...")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except Exception as e:
            print(f"Error in main loop: {str(e)}")
            time.sleep(300)  # Wait 5 minutes before retrying
        finally:
            loop.close()

if __name__ == "__main__":
    bot = TwitterBot()
    bot.run()