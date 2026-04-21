import requests
from datetime import datetime

class NewsSubscription:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def get_daily_news(self, country='us'):
        params = {
            'country': country,
            'apiKey': self.api_key
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            news_data = response.json()
            headlines = news_data.get('articles', [])
            return [article['title'] for article in headlines]
        else:
            return []

if __name__ == '__main__':
    API_KEY = 'YOUR_API_KEY'
    subscription = NewsSubscription(API_KEY)
    news = subscription.get_daily_news()
    print(f"Daily News Headlines ({datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC):")
    for title in news:
        print(f"- {title}")