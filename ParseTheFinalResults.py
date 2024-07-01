class ParseTheFinalResults:
    def FinalResultsParser(self):
        cryptos = [
            "Bitcoin", "Ethereum", "Binance Coin", "BNB", "Cardano", "Ripple", "Solana", "Polkadot", "Dogecoin",
            "Avalanche", "Uniswap", "Chainlink", "Litecoin", "Bitcoin Cash", "Stellar", "USD Coin",
            "Wrapped Bitcoin", "Cosmos", "Tezos", "EOS", "Tron", "VeChain", "Monero", "Theta", "Filecoin",
            "Maker", "Tether"
        ]

        results_sent = {crypto: 0 for crypto in cryptos}
        results_received = {crypto: 0 for crypto in cryptos}

        with open("final_results.txt", "r") as file_read:
            lines = file_read.readlines()
            for line in lines:
                for crypto in cryptos:
                    if f"Sent from exchange {crypto}" in line:
                        amount = float(line.split(":")[1].strip())
                        results_sent[crypto] = amount
                    elif f"Received from exchange {crypto}" in line:
                        amount = float(line.split(":")[1].strip())
                        results_received[crypto] = amount

        return results_sent, results_received
