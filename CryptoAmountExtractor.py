class CryptoAmountExtractor:
    def extract_and_print_amounts(self, title, amounts):
        if amounts:
            print(title)
            for amount in amounts:
                amount_without_commas = amount.replace(',', '')
                print(amount_without_commas)
        else:
            print(f"No amounts found in {title.lower()}.")