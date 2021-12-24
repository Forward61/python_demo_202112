class Card():
    """ A playing card."""
    RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]#牌面数字1~13
    SUITS=["梅","方","红","黑"]#梅花、方钻、红心、黑桃

    def __init__(self,rank,suit,face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up

    def __str__(self):
        if self.is_face_up:
            rep =self.suit+self.rank
        else:
            rep="XX"
        return rep

    def pic_order(self):
        if self.rank=="A":
            FaceNum=1
        elif self.rank=="J":
            FaceNum=11
        elif self.rank=="Q":
            FaceNum=12
        elif self.rank=="K":
            FaceNum=13

        else:
            FaceNum=int(self.rank)

        if self.suit=="梅":
            suit=1
        elif self.suit=="方":
            suit=2
        elif self.suit=="hs":
            suit=3
        else:
            suit=4
        return (suit-1)*13+FaceNum

    def flip(self):
        self.is_face_up=not self.is_face_up



class Hand():
    """A Hand of playing card"""
    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep+=str(card)+"\t"

        else:
            rep="无牌"
        return rep

    def clear(self):
        self.cards=[]

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Poke(Hand):
    """A deck of playing card"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self,hands,per_hand=13):
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # self.give(top_card,hand)
                else:
                    print("不能继续发牌了，牌已经发完了")


if __name__=="__main__":
    print("This is a module with classe for playing cards")
    players=[Hand(),Hand(),Hand(),Hand()]
    poke1=Poke()
    poke1.populate();

    poke1.shuffle()
    poke1.deal(players,13)
    n=1
    for hand in players:
        print("牌手：",n,end=":")
        print(hand)
        n=n+1

    input("\n press the enter key to exit")