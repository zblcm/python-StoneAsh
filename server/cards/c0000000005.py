from const import *
from event import *
from card import *

def init(self, mode = True):
    self.name = "占卜"
    self.description = "抽两张牌。"
    self.typ = CARD_SPELL
    self.subtype = [SUBTYPE_BASIC]
    self.originalcost = [0, 0, 3, 0, 0, 0] #White Fire Water Tree Light Death
    
    if mode:
        self.cost = self.originalcost.copy()
        self.needtarget = False
        buff = Buff(self.system, "b0000000005_000", self, self)
        self.add_buff(buff)



    
