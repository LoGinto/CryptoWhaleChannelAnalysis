from bs4 import BeautifulSoup
import requests
import lxml

class ConvertCrypto:


    def GetPrice(self,price):
        url = f"https://www.binance.com/en/price/{price.lower()}"
        HTML = requests.get(
            url,
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
            },
        )
        soup = BeautifulSoup(HTML.text, "lxml")
        text = soup.find("div", attrs={"class": "css-1bwgsh3"}).text
        clean_text = text.replace('$', '').replace(',', '').replace(' ', '').strip()

        # Convert to integer
        price_int = round(float(clean_text))

        return price_int