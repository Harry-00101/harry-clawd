#!/usr/bin/env python3
"""
Firecrawl Stock News Scraper
Scrapes financial websites for stock news and analysis.
"""

import requests
import json
from datetime import datetime

class StockNewsScraper:
    """Scrape stock news using Firecrawl API."""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://api.firecrawl.dev/v1"
    
    def scrape_url(self, url):
        """Scrape a URL and return markdown."""
        if not self.api_key:
            # Use mock for demo
            return self._mock_scrape(url)
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "url": url,
            "formats": ["markdown"]
        }
        
        response = requests.post(
            f"{self.base_url}/scrape",
            headers=headers,
            json=data
        )
        
        return response.json()
    
    def _mock_scrape(self, url):
        """Mock scrape for demo."""
        return {
            "success": True,
            "markdown": f"# Content from {url}\n\nScraped at {datetime.now().isoformat()}\n\n## Sample Content\n- Stock analysis\n- Price updates\n- Market news",
            "url": url
        }
    
    def get_yahoo_finance(self):
        """Get Yahoo Finance news."""
        return self.scrape_url("https://finance.yahoo.com/")
    
    def get_market_watch(self):
        """Get MarketWatch news."""
        return self.scrape_url("https://www.marketwatch.com/")
    
    def get_investing_com(self):
        """Get Investing.com news."""
        return self.scrape_url("https://www.investing.com/")


def main():
    """Test the scraper."""
    scraper = StockNewsScraper()
    
    print("=== Firecrawl Stock News Scraper ===")
    print(f"Time: {datetime.now().isoformat()}")
    print()
    
    # Test scrape
    result = scraper.get_yahoo_finance()
    
    if result.get("success"):
        print("✅ Successfully scraped Yahoo Finance")
        print(f"Content preview: {result['markdown'][:200]}...")
    else:
        print("⚠️ Using mock data")
        print(result)
    
    return result


if __name__ == "__main__":
    main()
