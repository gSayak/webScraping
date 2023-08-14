import hashlib
import io
from pathlib import Path
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.pexels.com/search/mountains/")
SCROLL_DISTANCE = 1000  # Adjust this value as needed
for _ in range(5):  # Scroll 5 times (adjust as needed)
    driver.execute_script(f"window.scrollBy(0, {SCROLL_DISTANCE});")
    time.sleep(1)  # Add a small delay to allow content to load
results = []
content = driver.page_source
soup = BeautifulSoup(content)


def gets_url(classes, location, source):
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))
    return results


driver.quit()

if __name__ == "__main__":
    returned_results = gets_url("Link_link__mTUkz spacing_noMargin__Q_PsJ", "img", "src")
    for b in returned_results:
        image_content = requests.get(b).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert("RGB")
        file_path = Path("D:\\WebScraping\\mountains\\", hashlib.sha1(image_content).hexdigest()[:10] + ".png")
        image.save(file_path, "PNG", quality=80)