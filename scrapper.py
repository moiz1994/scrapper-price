from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# List of product URLs
urls = [
    'https://oopbuy.com/product/weidian/7255517580?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/849925026301?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7265090384?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/805053010175?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/1/753323697727?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/819771748420?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7434362118?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/1/833894638868?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/1/675239069484?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/1/802519933158?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7251487193?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7259969772?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/TAOBAO/790003048414?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/TAOBAO/560206808142?inviteCode=TMGW80OAE',
    'https://oopbuy.com/goods/details?id=36560583182&channel=TAOBAO&inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/5236528270?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/TAOBAO/606576860110?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/869338291686?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/892604396780?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7265104391?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/783905895843?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/0/890152897944?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/TAOBAO/809595578369?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7255850054?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7420326837?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7421955540?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7387175802?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7434329060?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7408189197?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7432470874?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7423350183?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7426692723?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7252533984?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7280200545?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7434776106?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7425169070?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7434735150?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/6139760496?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7434725136?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7434796192?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7258684534?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7251399421?inviteCode=TMGW80OAE',
    'https://oopbuy.com/product/weidian/7385256549?inviteCode=TMGW80OAE'
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
