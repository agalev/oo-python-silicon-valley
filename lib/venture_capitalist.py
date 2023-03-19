from lib.funding_round import *
from lib.startup import *

class VentureCapitalist:
    all = []
    
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        self.portfolio = []
        self.biggest_investment = 0
        VentureCapitalist.add_to_all(self)
    
    @classmethod
    def add_to_all(cls, vc):
        cls.all.append(vc)
    
    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls.all if vc.total_worth > 1000000000]
    
    def offer_contract(self, startup, type, investment):
        if investment > self.total_worth:
            print('You cannot invest more than your total worth.')
        else:
            startup.sign_contract(self, type, investment)
            self.total_worth -= investment
            if startup not in self.portfolio:
                self.portfolio.append(startup)
            if investment > self.biggest_investment:
                self.biggest_investment = investment
    
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]
    
    def invested(self, domain):
        return sum([fr.investment for fr in FundingRound.all if fr.startup.domain == domain and fr.venture_capitalist == self])