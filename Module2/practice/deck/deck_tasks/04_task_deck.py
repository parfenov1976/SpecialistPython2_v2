from deck_total import Card, Deck


# Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
# Вытягивайте карты парами - одну из первой колоды, вторую из второй.
# Если карта из первой колоды окажется больше(старше), то записываем 1:0(условно начисляем победное очко первой колоде),
# если карты одинаковые, то не учитываем очко никуда.
# Выведите итоговый счет, сравнив попарно все карты в колодах.

def deck52to36(deck):
    for crd in tuple(deck):
        if crd < Card('6', Card.SPADES):
            deck.cards.remove(crd)


deck1 = Deck()
deck52to36(deck1)
deck2 = Deck()
deck52to36(deck2)
deck1.shuffle()
deck2.shuffle()
deck1_points = 0
deck2_points = 0

while deck1.cards and deck1.cards:
    card1 = deck1.draw(1)
    card2 = deck2.draw(1)
    if card1 > card2:
        deck1_points += 1
    elif card1 < card2:
        deck2_points += 1

print(f'Итоговый счет: Колода 1 - {deck1_points}, Колода 2 - {deck2_points}')
