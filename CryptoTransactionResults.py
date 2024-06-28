import re
from collections import defaultdict

class CryptoCoinTransactionResults:
    def __init__(self):
        self.sent_amounts = defaultdict(list)
        self.received_amounts = defaultdict(list)

    def parse_data(self, data):
        current_coin = None
        lines = data.strip().split('\n')
        for line in lines:
            if line.startswith('Coin:'):
                current_coin = line.split('Coin: ')[1].strip()
            elif line.startswith('Amount sent by an exchange:'):
                amounts = re.findall(r"'([^']*)'", line)
                if current_coin:
                    self.sent_amounts[current_coin].extend(amounts)
            elif line.startswith('Amount received by an exchange:'):
                amounts = re.findall(r"'([^']*)'", line)
                if current_coin:
                    self.received_amounts[current_coin].extend(amounts)

    def write_results(self, filename):
        with open(filename, 'w') as f_out:
            for coin in set(list(self.sent_amounts.keys()) + list(self.received_amounts.keys())):
                sent_sum = sum(float(amount.replace(',', '')) for amount in self.sent_amounts[coin])
                received_sum = sum(float(amount.replace(',', '')) for amount in self.received_amounts[coin])
                f_out.write(f"Sent from exchange {coin}: {sent_sum}\n")
                f_out.write(f"Received from exchange {coin}: {received_sum}\n")




