import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f'{self.value}{suit[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = [Card.SPADES, Card.CLUBS, Card.DIAMONDS, Card.HEARTS]
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        deck_string = f'deck[{len(self.cards)}]: '
        for card in self.cards:
            deck_string += card.to_str() + ", "
        return deck_string

    def draw(self, x):
        drowned_cards = []
        for _ in range(x):
            drowned_cards.append(self.cards.pop(0))
        return drowned_cards

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тасуем колоду
deck.shuffle()
print(deck.show())
# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(f'Hand[{len(hand)}]:', *[card.to_str() + ',' for card in hand])
