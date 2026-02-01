# Selenium Skill

Browser automation using Selenium WebDriver.

## Install

```bash
cd /root/clawd
uv venv .venv
source .venv/bin/activate
uv pip install selenium webdriver-manager
```

## Usage

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = Options()
options.add_argument("--headless")  # Run without GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Create driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Navigate
driver.get("https://example.com")
print(driver.title)

# Find elements
element = driver.find_element("id", "element-id")
element.click()
element.send_keys("text")

# Get page source
html = driver.page_source

# Close
driver.quit()
```

## Common Selectors

```python
# By ID
driver.find_element("id", "button-id")

# By CSS
driver.find_element("css selector", ".classname")

# By XPath
driver.find_element("xpath", "//div[@class='container']")

# By name
driver.find_element("name", "username")

# By link text
driver.find_element("link text", "Click Here")
```

## Wait Strategies

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(("id", "my-element"))
)
```

## Headless Browser

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")  # Modern headless
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
```

## Resources

- Docs: https://www.selenium.dev/documentation/
- PyPI: https://pypi.org/project/selenium/
