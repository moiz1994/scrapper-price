from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# List of product URLs
urls = [
    'https://oopbuy.com/product/weidian/7251487193?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7259969772?inviteCode=TMGW80OAE'
]

# Path to your downloaded ChromeDriver
chrome_driver_path = './chromedriver.exe'  # Adjust path if needed

# Set up Selenium driver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run browser in background
driver = webdriver.Chrome(service=service, options=options)

for url in urls:
    try:
        driver.get(url)
        time.sleep(3)  # Wait for JavaScript to load

        # Find the price in CNY (first .big-text inside .price)
        price_element = driver.find_element(By.CSS_SELECTOR, ".price .big-text")
        print(f'{price_element.text}')
    
    except Exception as e:
        print(f'Error fetching {url}: {e}')

driver.quit()
