
COINS = ['D', 'N', 'Q']


def coin_value(c):
    if c == 'D':
        return 10
    elif c == 'N':
        return 5
    elif c == 'Q':
        return 25


class Machine():
    def __init__(self):
        self.response = []
        self.coins_inserted = []

    def run(self, *commands):
        for command in commands:
            # print(self.coins_inserted, command)
            if command == 'COIN-RETURN':
                self.coin_return()
            elif command in ['BUY-A', 'BUY-B', 'BUY-C']:
                self.buy(command)
            elif command in COINS:
                self.coins_inserted.append(command)

    def coin_return(self):
        self.response += self.coins_inserted
        self.coins_inserted = []

    def get_current_sum(self):
        cents = 0
        for c in self.coins_inserted:
            cents += coin_value(c)
        return cents / 100

    def buy(self, command):
        if self.get_current_sum() == 1 and command == 'BUY-B':
            self.response.append('B')
