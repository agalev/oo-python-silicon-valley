class FundingRound:
    all = []

    def __init__(self, startup, venture_capitalist, type, investment):
        self._startup = startup
        self._venture_capitalist = venture_capitalist
        self.type = type
        self.investment = investment
        # startup.sign_contract(self)
        # venture_capitalist.sign_contract(self)
        FundingRound.add_to_all(self)

    @classmethod
    def add_to_all(cls, fr):
        cls.all.append(fr)
    
    def get_startup(self):
        return self._startup
    def set_startup(self, startup):
        print('You cannot change the startup.')
    startup = property(get_startup, set_startup)

    def get_venture_capitalist(self):
        return self._venture_capitalist
    def set_venture_capitalist(self, venture_capitalist):
        print('You cannot change the venture capitalist.')
    venture_capitalist = property(get_venture_capitalist, set_venture_capitalist)

    def get_investment(self):
        return self._investment
    def set_investment(self, investment):
        if investment < 0:
            print('You cannot invest a negative amount.')
        else:
            self._investment = float(investment)
    investment = property(get_investment, set_investment)
    