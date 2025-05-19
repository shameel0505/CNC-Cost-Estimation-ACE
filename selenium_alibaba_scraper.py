from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import traceback

# Set up Chrome driver
service = Service('./chromedriver')  # Update path if needed
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run without GUI
driver = webdriver.Chrome(service=service, options=options)

# Load page
url = "https://www.alibaba.com/trade/search?SearchText=cnc+machining+parts"
driver.get(url)
time.sleep(10)  # Wait for JS to load fully

data = []
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[data-spm-anchor-id^="a2700.galleryofferlist.d_title"]'))
    )
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.search-card-e-price-main"))
    )
    
    products = driver.find_elements(By.CSS_SELECTOR, 'span[data-spm-anchor-id^="a2700.galleryofferlist.d_title"]')
    prices = driver.find_elements(By.CSS_SELECTOR, "div.search-card-e-price-main")

    print(f"Found {len(products)} products and {len(prices)} prices.")

    for i in range(min(len(products), len(prices))):
        try:
            name = products[i].text.strip()
            price_text = prices[i].text.strip()
            import re
            cost_match = re.findall(r"[\d\.]+", price_text.replace(',', ''))
            if cost_match:
                cost_values = list(map(float, cost_match))
                quoted_cost = round(sum(cost_values)/len(cost_values), 2)
            else:
                quoted_cost = None

            material = "Aluminum" if "aluminum" in name.lower() else "Steel" if "steel" in name.lower() else "Other"
            estimated_volume = 50000
            feature_count = 5
            cycle_time_min = 10

            data.append({
                "Product": name,
                "Material": material,
                "Volume_mm3": estimated_volume,
                "Feature_Count": feature_count,
                "Cycle_Time_min": cycle_time_min,
                "Quoted_Cost": quoted_cost
            })
        except Exception as e_inner:
            print(f"Error on item {i}: {e_inner}")
            print(traceback.format_exc())
except Exception as e_outer:
    print(f"Error during scraping: {e_outer}")
    print(traceback.format_exc())
finally:
    driver.quit()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("alibaba_scraped_data.csv", index=False)
print("✅ Data saved to alibaba_scraped_data.csv")