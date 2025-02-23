from pycoingecko import CoinGeckoAPI
import requests
from datetime import datetime
import time

class TrendTracker:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.cache_duration = 3600  # 1 hour cache
        self.last_update = 0
        self.cached_trends = None

    def get_trending_crypto(self):
        """Get trending cryptocurrencies from CoinGecko"""
        try:
            trending = self.cg.get_search_trending()
            return [coin['item']['name'] for coin in trending['coins'][:5]]
        except Exception as e:
            print(f"Error getting trending crypto: {str(e)}")
            return []

    def get_web3_trends(self):
        """Get trending Web3 topics from common sources"""
        try:
            # You might want to replace this URL with a more specific Web3 news API
            response = requests.get(
                "https://api.coingecko.com/api/v3/news",
                headers={"accept": "application/json"}
            )
            news = response.json()
            return [item['title'] for item in news[:5]]
        except Exception as e:
            print(f"Error getting Web3 trends: {str(e)}")
            return []

    def get_all_trends(self):
        """Get all trending topics with caching"""
        current_time = time.time()
        
        # Return cached results if they're still fresh
        if self.cached_trends and (current_time - self.last_update) < self.cache_duration:
            return self.cached_trends

        trends = {
            'crypto': self.get_trending_crypto(),
            'web3': self.get_web3_trends(),
        }
        
        self.cached_trends = trends
        self.last_update = current_time
        return trends