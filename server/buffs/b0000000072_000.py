from const import *
from event import *
from card import *


def init(self):
    self.typ = BUFF_DYNAMIC
    self.original = True
    self.visable = False
    self.name = "魔法图书馆员"
    self.description = "你每释放一个法术, 将一张魔导书置入你的手牌。"
    
    def after_usecard(self, old_event):
        card = old_event.param[0]
        if (self.card.place != PLACE_FIELD) or (card.typ != CARD_SPELL) or (card.player != self.card.player):
            return False

        self.system.yell(self.card, 0, True)
        sublists = ["tinystar"]
        self.system.playeffect("bluelight", sublists, self.card, self.card)
        self.system.yell(self.card, 1)

        import random

        numbers = []
        for cardtemp in self.system.allcards:
            if SUBTYPE_BOOK in cardtemp.subtype:
                numbers.append(cardtemp.number)
        number = numbers[random.randint(1, len(numbers)) - 1]
        
        group = []
        new_card = Card(self.system, number, True, self.card.player)
        new_card.source = None
        group.append(new_card)
        self.system.cards.append(new_card)
        
        param = [group, PLACE_HAND, True, False, False, False, False]
        event = Event(self.system, EVENT_MOVE, self, param)
        event.do()

        return False
    self.after_usecard = after_usecard
