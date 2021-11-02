from deck_total import Card, Deck

# Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт.
# Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?

deck1 = Deck()
deck2 = Deck()
deck1.cards.extend(deck2.cards)
deck1.shuffle()
deck1.draw(52)
list_suits = [card.suit for card in deck1]
list_count = []
suit = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Spades': '\u2660', 'Clubs': '\u2663'}
for el in set(list_suits):
    list_count.append((suit[el], list_suits.count(el)))
list_count.sort(key=lambda x: x[1], reverse=True)
if list_count[0][1] == list_count[1][1]:
    print(f'Масть {list_count[0][0]} и {list_count[1][0]} встречаются по {list_count[0][1]} раз')
else:
    print(f'Масть {list_count[0][0]} встречается {list_count[0][1]} раз')
