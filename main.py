import CryptoTransactionParser
import CryptoTransactionResults
import ConvertCrypto
import ParseTheFinalResults


def process_results(results_sent, results_received):
    dollar_sent = {}
    dollar_received = {}

    # Process results_sent
    for key, value in results_sent.items():
        if value != 0:
            dollarAmt = float(value) * ConvertCrypto.ConvertCrypto().GetPrice(key)
            dollar_sent[key] = dollarAmt

    # Print or use the dollar_sent dictionary as needed
    print("Dollar Sent:")
    for key, value in dollar_sent.items():
        print(f"{key}: ${value:.2f}")

    # Process results_received
    for key, value in results_received.items():
        if value != 0:
            dollarAmt = float(value) * ConvertCrypto.ConvertCrypto().GetPrice(key)
            dollar_received[key] = dollarAmt

    print("\nDollar Received:")
    for key, value in dollar_received.items():
        print(f"{key}: ${value:.2f}")


if __name__ == "__main__":
    parser = CryptoTransactionParser.CryptoTransactionParser()
    parser.parse_transactions("https://t.me/s/whale_alert_io")

    searcher = CryptoTransactionResults.CryptoCoinTransactionResults()
    with open('results.txt', 'r') as file:
        data = file.read()
    searcher.parse_data(data)
    searcher.write_results('final_results.txt')

    parser = ParseTheFinalResults.ParseTheFinalResults()
    results_sent, results_received = parser.FinalResultsParser()
    process_results(results_sent, results_received)
