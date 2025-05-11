import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run without opening browser
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.93 Safari/537.36")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Path to your ChromeDriver
service = Service('./chromedriver.exe')

# Initialize the browser
driver = webdriver.Chrome(service=service, options=chrome_options)

# Read links from CSV
with open('links.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    urls = [row[0] for row in reader if row]

results = []

for index, url in enumerate(urls, start=1):
    try:
        driver.get(url)
        time.sleep(2)  # wait for the page to load
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find the price span
        price_span = soup.find('span', class_='price')
        if price_span:
            cny_span = price_span.find('span', class_='big-text')
            if cny_span:
                cny_price = cny_span.text.strip()
                results.append([index, cny_price])
                print(f"{index}: CNY {cny_price}")
            else:
                results.append([index, 'CNY not found'])
                print(f"{index}: CNY not found")
        else:
            results.append([index, 'Price span not found'])
            print(f"{index}: Price span not found")

    except Exception as e:
        results.append([index, f'Error: {str(e)}'])
        print(f"{index}: Error: {str(e)}")

# Close the browser
driver.quit()

# Write results to CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['#', 'CNY Price'])
    writer.writerows(results)

print("\n✅ Done! Prices saved to output.csv")
