from const import *
from event import *



def init(self):
    self.typ = BUFF_DYNAMIC
    self.original = True
    self.visable = False
    self.name = "自动嘲讽"
    self.description = "在召唤出来时获得嘲讽。"

    def after_move(self, old_event):
        if (self.card in old_event.param[0]) and (old_event.param[1] == PLACE_FIELD):
            buff = Buff(self.system, "nature_000006", self.card, self.card)
            self.card.add_buff(buff)
        return True
    self.after_move = after_move
