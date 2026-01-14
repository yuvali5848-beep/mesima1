class Security:
    def __init__(self, name, ticker, price):
        self.name = name
        self.ticker = ticker
        self.price = price

    def show_info(self):
        print(f"{self.name} ({self.ticker}) - מחיר: {self.price}")


class Stock(Security):
    def __init__(self, name, ticker, price, dividend):
        super().__init__(name, ticker, price)
        self.dividend = dividend

    def show_dividend(self):
        print(f"דיבידנד למניה: {self.dividend}")


class Bond(Security):
    def __init__(self, name, ticker, price, interest_rate):
        super().__init__(name, ticker, price)
        self.interest_rate = interest_rate

    def show_interest(self):
        print(f"ריבית לאג\"ח: {self.interest_rate}%")


class Option(Security):
    def __init__(self, name, ticker, price, strike_price):
        super().__init__(name, ticker, price)
        self.strike_price = strike_price

    def show_strike(self):
        print(f"מחיר מימוש לאופציה: {self.strike_price}")


def main():
    name = input("הכנס שם נייר ערך: ")
    ticker = input("הכנס טיקר: ")
    price = float(input("הכנס מחיר: "))

    dividend = float(input("הכנס דיבידנד למניה: "))
    stock = Stock(name, ticker, price, dividend)

    interest_rate = float(input("הכנס ריבית לאג\"ח: "))
    bond = Bond(name, ticker, price, interest_rate)

    strike_price = float(input("הכנס מחיר מימוש לאופציה: "))
    option = Option(name, ticker, price, strike_price)

    stock.show_info()
    stock.show_dividend()

    bond.show_info()
    bond.show_interest()

    option.show_info()
    option.show_strike()


if __name__ == "__main__":
    main()
