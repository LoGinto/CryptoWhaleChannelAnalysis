from bs4 import BeautifulSoup
import requests
import lxml
import re

class ConvertCrypto:


    def GetPrice(self,price):
        #print(price)
        url = f"https://www.binance.com/en/price/{price.lower()}"
        HTML = requests.get(
            url,
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
            },
        )
        soup = BeautifulSoup(HTML.text, "lxml")
        text = soup.find("span", attrs={"class": "t-subtitle2 text-textPrimary md:t-subtitle1 lg:t-headline5"}).text
        clean_text = text.replace('$', '').replace(',', '').replace(' ', '').strip()
        clean_text = re.sub(r'[^\d.]', '', text)
        # Convert to integer
        price_int = round(float(clean_text))

        return price_int