
class DisposableIncome:
    def __init__ (self,rent,council_tax,utility,broadband,grocery,eatout,transport):
        self.rent = rent
        self.council_tax = council_tax
        self.utility = utility
        self.broadband = broadband
        self.grocery = grocery
        self.eatout = eatout
        self.transport = transport
    
    def disposable_income(self,combined_takehome):
        expend = self.rent + self.council_tax + self.utility + self.broadband + self.grocery + self.eatout  + self.transport
        remainder = 700 
        save_invest = combined_takehome - expend - remainder 
        return round(save_invest,2)


# glasgow = DisposableIncome(795,264,125,40,225,160,150)
# london = DisposableIncome(1400,264,180,40,350,200,350)
# print('Glasgow: £' + str(glasgow.disposable_income(6664.2333)))
# print('London: £'+ str(london.disposable_income(6664.2333)))
