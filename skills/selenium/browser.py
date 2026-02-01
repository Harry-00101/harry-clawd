#!/usr/bin/env python3
"""
Selenium Browser Automation for Harry-001
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def create_driver(headless=True):
    """Create a Chrome driver instance."""
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

def get_page(url, headless=True):
    """Navigate to a URL and return page source."""
    driver = create_driver(headless)
    try:
        driver.get(url)
        time.sleep(2)  # Wait for JS to load
        return driver.page_source
    finally:
        driver.quit()

def find_element(url, selector, by="css"):
    """Find an element by selector."""
    driver = create_driver()
    try:
        driver.get(url)
        if by == "id":
            element = driver.find_element(By.ID, selector)
        elif by == "css":
            element = driver.find_element(By.CSS_SELECTOR, selector)
        elif by == "xpath":
            element = driver.find_element(By.XPATH, selector)
        else:
            element = driver.find_element(By.CSS_SELECTOR, selector)
        return element.text
    finally:
        driver.quit()

def main():
    """Demo usage."""
    import sys
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(f"Fetching {url}...")
        html = get_page(url)
        print(f"Page title: {driver.title if 'driver' in locals() else 'N/A'}")
        print(f"Content length: {len(html)} chars")
    else:
        print("Usage: python3 browser.py <url>")

if __name__ == "__main__":
    main()
