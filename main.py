import CryptoTransactionParser
import CryptoTransactionResults
import ConvertCrypto
import ParseTheFinalResults


def process_results(results_sent, results_received):
    dollar_sent = {}
    dollar_received = {}
    withdrawal_total = 0  # Track the total withdrawal amount
    deposit_total = 0  # Track the total deposit amount
    prevailing_coin_sent = None  # Track the prevailing coin for sent transactions
    prevailing_coin_received = None  # Track the prevailing coin for received transactions

    # Process results_sent
    print("\nDollars that is sent from exchanges:")
    for coin, amount in results_sent.items():
        if amount != 0:  # Skip coins with zero value
            dollar_amount = float(amount) * ConvertCrypto.ConvertCrypto().GetPrice(coin)
            dollar_sent[coin] = dollar_amount
            withdrawal_total += dollar_amount
            if not prevailing_coin_sent or dollar_sent[coin] > dollar_sent.get(prevailing_coin_sent, 0):
                prevailing_coin_sent = coin
            print(f"{coin}: {amount:.2f} coins, ${dollar_amount:.2f}")

    # Process results_received
    print("\nDollars that exchanges received:")
    for coin, amount in results_received.items():
        if amount != 0:  # Skip coins with zero value
            dollar_amount = float(amount) * ConvertCrypto.ConvertCrypto().GetPrice(coin)
            dollar_received[coin] = dollar_amount
            deposit_total += dollar_amount
            if not prevailing_coin_received or dollar_received[coin] > dollar_received.get(prevailing_coin_received, 0):
                prevailing_coin_received = coin
            print(f"{coin}: {amount:.2f} coins, ${dollar_amount:.2f}")

    # Include withdrawal total in the output
    print(f"\nTotal withdrawal amount: ${withdrawal_total:.2f}")
    print(f"Total deposit amount: ${deposit_total:.2f}")

    # Determine whether withdrawals or deposits are prevailing
    if deposit_total > withdrawal_total:
        print("\nExchange received more than withdrawals.")
        print(f"Difference: ${deposit_total - withdrawal_total:.2f}")
        print(f"Prevailing coin (received): {prevailing_coin_received}")
    else:
        print("\nWithdrawals are prevailing.")
        print(f"Difference: ${withdrawal_total - deposit_total:.2f}")
        print(f"Prevailing coin (sent): {prevailing_coin_sent}")


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
