import os
import json
import requests
from bs4 import BeautifulSoup

# 1. Define the target URL
URL = "https://translations.python.org/#ta"

def fetch_and_save():
    # 2. Fetch the data (Use an API if available, otherwise scrape the HTML)
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return

    # 3. Parse the data (Example: Extracting a specific element)
    soup = BeautifulSoup(response.text, 'html.parser')
    target_element = soup.find('div', id='target-data-id')
    
    extracted_text = target_element.text.strip() if target_element else "No data found"

    # 4. Save the data to a file inside your repository
    data_to_save = {"latest_data": extracted_text}
    with open("data.json", "w") as f:
        json.dump(data_to_save, f, indent=4)
    print("Data successfully updated!")

if __name__ == "__main__":
    fetch_and_save()
