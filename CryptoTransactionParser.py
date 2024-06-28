import CryptoAmountExtractor
import requests
from bs4 import  BeautifulSoup
import re
import CryptoCoinSearcher

class CryptoTransactionParser:
    def __init__(self):
        self.crypto_exchanges = ["Kraken", "Binance", "Coinbase", "Bitfinex", "Huobi", "OKEx", "Bittrex", "Gemini", "KuCoin", "Bitstamp", "Gate.io", "BitMEX", "FTX", "Deribit", "HitBTC", "Upbit", "Liquid", "Exmo", "Yobit", "Probit"]
        self.amount_extractor = CryptoAmountExtractor.CryptoAmountExtractor()
        self.coin_searcher = CryptoCoinSearcher.CryptoCoinSearcher()

    def parse_transactions(self, url):
        contents = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"})
        soup = BeautifulSoup(contents.text, "html.parser")
        new_list = []

        open("results.txt", "w").close()

        with open('url.txt', 'w', encoding='utf-8') as f_out:
            f_out.write(soup.prettify())

        with open("url.txt", "r", encoding='utf-8') as file_read:
            lines = file_read.readlines()

            for line in lines:
                if "https://whale-alert.io/transaction/" in line:
                    new_list.append(line)

        if not new_list:
            print("Data not found")
        else:
            print("\n**** Extracted URLs ****\n")
            index = 0

            for url in [re.search(r'href="([^"]*)"', item).group(1) for item in new_list]:
                print(url)
                contents = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"})
                index += 1
                soup = BeautifulSoup(contents.text, "html.parser")
                from_addresses_element = soup.find(id="from-addresses")
                to_addresses_element = soup.find(id="to-addresses")

                if from_addresses_element:
                    detected_exchanges = [exchange for exchange in self.crypto_exchanges if exchange in from_addresses_element.get_text()]
                    if detected_exchanges:
                        print("Exchanges that sent the money: " + ", ".join(detected_exchanges))
                        amounts_sent = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b', from_addresses_element.get_text())
                        self.amount_extractor.extract_and_print_amounts("Amounts sent:", amounts_sent)
                        with open('results.txt','a') as f_sent:
                            f_sent.write(f"\nAmount sent by an exchange: {amounts_sent}")

                if to_addresses_element:
                    detected_to_exchanges = [exchange for exchange in self.crypto_exchanges if exchange in to_addresses_element.get_text()]
                    if detected_to_exchanges:
                        print("Exchanges that received the money: " + ", ".join(detected_to_exchanges))
                        amounts_received = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b', to_addresses_element.get_text())
                        self.amount_extractor.extract_and_print_amounts("Amounts received:", amounts_received)
                        with open('results.txt','a') as f_received:
                            f_received.write(f"\nAmount received by an exchange: {amounts_received}")

                self.coin_searcher.search_and_print_coins(soup.get_text())

