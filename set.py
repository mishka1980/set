from random import shuffle
class Card:
    """
    The Set Card Class
                 1      2         3
    colour->    Red,  Green,    Purple
    shape ->    Oval, Squiggle, Diamond
    filling->   Full, striped,  Open
    number->    1     2         3
    """
    colourlist=[[], "Red", "Green", "Purple"]
    shapelist=[[], "Oval", "Squiggle", "Diamond"]
    fillinglist=[[], "Full", "Striped","Open"]
    numberlist=[[],"1", "2", "3"]

    def __init__(self, colour, shape, filling, number):
        """Create a New Set Card"""
        self.colour=colour
        self.shape=shape
        self.filling=filling
        self.number=number

        if not (colour==1 or colour==2 or colour==3):
            raise Exception("Error: Colour. Red=1, Green=2, Purple=3")

        if not (shape==1 or shape==2 or shape==3):
            raise Exception("Error: shape. Oval=1, Squiggle=2, Diamond=3")

        if not (filling==1 or filling==2 or filling==3):
            raise Exception("Error: filling. Full=1, Striped=2, open=3")

        if not (number==1 or number==2 or number==3):
            raise Exception("Error: number. 1=1, 2=2, 3=3")

    def __str__(self):
        return (self.numberlist[self.number]+" of "+
                self.colourlist[self.colour]+" "+
                self.fillinglist[self.filling]+" "+
                self.shapelist[self.shape])

class Deck:
    """Deck class"""
    def __init__(self):
        self.cards=[]
        for colour in range(1,4):
            for shape in range(1,4):
                for filling in range(1,4):
                    for number in range(1,4):
                        self.cards.append(Card(colour, shape, filling, number))

    def __str__(self):
        s=""
        for i in range(len(self.cards)):
            s= s+ str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        """Shuffles the Deck"""
        shuffle(self.cards)

    def pop(self, number):
        for i in range(0, number):
            self.cards.pop(0)


class PlayingField():
    def __init__(self, deck):
        self.deck=deck
        self.play=[]
        self.play=deck.cards[0:12]
        deck.pop(12)

    def __str__(self):
        s=""
        for i in range(0,len(self.play)):
            if i<10:
                s= s+ str(i)+"  | "+ str(self.play[i])+"\n"
            if i>=10:
                s= s+ str(i)+" | "+ str(self.play[i])+"\n"

        return s

    def update(self,num1, num2, num3):
        if IsSet(self.play[num1], self.play[num2], self.play[num3]):
            print True

def IsSet(card1, card2, card3):
    """Checks if three cards form a set"""

    "colour= True if all the colours are the same or all different"
    colour= (card1.colour == card2.colour == card3.colour) or (card1.colour != card2.colour != card3.colour)
    "shape = True if all the shapes are the same or all different"
    shape= (card1.shape == card2.shape == card3.shape) or (card1.shape != card2.shape != card3.shape)

    "filling= True if all the fillngs are the same or all different"
    filling= (card1.filling == card2.filling == card3.filling) or (card1.filling != card2.filling != card3.filling)

    "number= True if all the numbers are the same or all different"
    number= (card1.number == card2.number == card3.number) or (card1.number != card2.number != card3.number)

    return colour and shape and filling and number

game=PlayingField(Deck())
