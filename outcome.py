class Outcome:

    def __init__(self,name,odds):
        self.name = name
        self.odds = odds
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self,other):
        if self.name == other.name:
            return True
        else:
            return False
    
    def __ne__(self,other):
        if self.name != other.name:
            return True
        else:
            return False
    
    def __str__(self):
        return "%s (%d:1)" % (self.name,self.odds)
    
    def winAmount(self,amount):
        return self.odds*amount
