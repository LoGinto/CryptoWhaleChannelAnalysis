import CryptoTransactionParser
import  CryptoTransactionResults


if __name__ == "__main__":
    parser = CryptoTransactionParser.CryptoTransactionParser()
    parser.parse_transactions("https://t.me/s/whale_alert_io")
    searcher = CryptoTransactionResults.CryptoCoinTransactionResults()
    # Read data from results.txt
    with open('results.txt', 'r') as file:
        data = file.read()
    searcher.parse_data(data)
    searcher.write_results('final_results.txt')


