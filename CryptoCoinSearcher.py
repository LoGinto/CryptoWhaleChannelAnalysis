class CryptoCoinSearcher:

    def search_and_print_coins(self, text):
        cryptos = ["Bitcoin", "Ethereum", "Binance Coin", "BNB", "Cardano", "Ripple", "Solana", "Polkadot", "Dogecoin",
                   "Avalanche", "Uniswap", "Chainlink", "Litecoin", "Bitcoin Cash", "Stellar", "USD Coin",
                   "Wrapped Bitcoin", "Cosmos", "Tezos", "EOS", "Tron", "VeChain", "Monero", "Theta", "Filecoin",
                   "Maker", "Tether"]

        for crypto in cryptos:
            if crypto in text:
                print(f"Coin: {crypto}")
                with open("results.txt", 'a') as f_out:
                    f_out.write(f"\nCoin: {crypto}\n ")
