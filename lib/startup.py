from lib.venture_capitalist import *
from lib.funding_round import *

class Startup:
    all = []

    def __init__(self, name, founder, domain):
        self.name = name
        self._founder = founder
        self._domain = domain
        self.num_funding_rounds = 0
        self.total_funds = 0
        self.investors = []
        self.big_investors = []
        Startup.add_to_all(self)

    def get_founder(self):
        return self._founder
    def set_founder(self, founder):
        print('You cannot change the founder.')
    founder = property(get_founder, set_founder)

    def get_domain(self):
        return self._domain
    def set_domain(self, domain):
        print('You cannot change the domain.')
    domain = property(get_domain, set_domain)

    def pivot(self, domain, name):
        self._domain = domain
        self.name = name
    
    @classmethod
    def add_to_all(cls, startup):
        cls.all.append(startup)
    
    @classmethod
    def find_by_founder(cls, founder):
        for s in cls.all:
            if s.founder == founder:
                print(f"founder of:{s}")
                return f"founder of:{s}"
    
    @classmethod
    def domains(cls):
        return [s.domain for s in cls.all]
    
    def sign_contract(self, venture_capitalist, type, investment):
        self.num_funding_rounds += 1
        self.total_funds += investment
        if venture_capitalist.total_worth > 1000000000 and venture_capitalist not in self.big_investors:
            self.big_investors.append(venture_capitalist)
        if venture_capitalist not in self.investors:
            self.investors.append(venture_capitalist)
        
        FundingRound(self, venture_capitalist, type, investment)
