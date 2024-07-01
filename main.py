import CryptoTransactionParser
import  CryptoTransactionResults
import ConvertCrypto
import ParseTheFinalResults


def process_results(results_sent, results_received):
    dollar_sent = {}
    dollar_received = {}

    # Process results_sent
    for key, value in results_sent.items():
        if value != 0:
            dollar_sent[key] = value

    # Print or use the dollar_sent dictionary as needed
    print("Dollar Sent:")
    for key, value in dollar_sent.items():
        print(f"{key}, :{value}")
        #print(f"{key} {ConvertCrypto.ConvertCrypto().GetPrice({key})} dollars")

    # Process results_received
    for key, value in results_received.items():
        if value != 0:
            dollar_received[key] = value

    ##print("Dollar Received:")
    for key, value in dollar_received.items():
        print(f"{key}, : {value}")
        #print(f"{key} {ConvertCrypto.ConvertCrypto().GetPrice({key})} dollars")


if __name__ == "__main__":
    parser = CryptoTransactionParser.CryptoTransactionParser()
    parser.parse_transactions("https://t.me/s/whale_alert_io")
    searcher = CryptoTransactionResults.CryptoCoinTransactionResults()
    # Read data from results.txt
    with open('results.txt', 'r') as file:
        data = file.read()
    searcher.parse_data(data)
    searcher.write_results('final_results.txt')
    #btcPrice = ConvertCrypto.ConvertCrypto().GetPrice("Bitcoin")
    #print(f"BTC {btcPrice}")

    parser = ParseTheFinalResults.ParseTheFinalResults()
    results_sent, results_received = parser.FinalResultsParser()
    process_results(results_sent, results_received)







