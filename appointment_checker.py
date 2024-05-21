import requests
from bs4 import BeautifulSoup
import time
import subprocess

while True:
    print("\nFetching the webpage...")
    try:
        # Scraping the German Consulate in Islamabad
        url = 'https://service2.diplo.de/rktermin/extern/choose_categoryList.do?locationCode=isla&realmId=108'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        print("Parsing the webpage...")
        soup = BeautifulSoup(response.content, 'html.parser')
        text_elements = soup.find_all(text=True)
        all_text = ' '.join(filter(lambda text: text.strip(), text_elements))
        count = all_text.lower().count('termin-warteliste')

        # Check if the student applications have opened. If not, wait for 30 seconds and try again, else alert the user 30 times via whatsapp
        if ('stud' in all_text.lower() or count > 4):
            print(f"Appointment Found!")
            for i in range (0, 30):
                subprocess.run(['python', 'alert.py'])
            break  
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        time.sleep(60)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(60)

    time.sleep(30)