from deck_total import Card, Deck

# Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”:

# 1. Создайте колоду из 52 карт. Перемешайте ее.
# 2. Первый игрок берет сверху 6 карт
# 3. Второй игрок берет сверху 6 карт.
# 4. Игрок-1 ходит:
#     1. игрок-1 выкладывает самую маленькую карту по значению
#     2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
#     3. Если игрок-2 не может побить карту, то он проигрывает.
#     4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
# 5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.

deck = Deck()
deck.shuffle()
player1 = deck.draw(6)
player2 = deck.draw(6)
player1.sort()
player2.sort()
print('Карты на руках 1-го игрока:', *player1)
print('Карты на руках 2-го игрока:', *player2)
cards_on_table = []
p1_min_card = player1.pop(0)
cards_on_table.append(p1_min_card)
print('Первый игрок кладет на стол карту', p1_min_card)
while True:
    beat = 0
    for card in player2:
        if card.suit == p1_min_card.suit and card > p1_min_card:
            player2.remove(card)
            cards_on_table.append(card)
            beat = 1
            print('Второй игрок бьет картой', card)
            break
    if beat == 1:
        values_on_table = [card.value for card in cards_on_table]
        for card in player1:
            if card.value in values_on_table:
                player1.remove(card)
                cards_on_table.append(card)
                print('Первый игрок подкидывает на стол карту', card)
                break
        else:
            print('Первому игроку нечего подкинуть')
            break
    else:
        print('Второй игрок не может побить карту')
        break
