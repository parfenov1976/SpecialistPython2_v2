# Возьмите классы Deck и Card с GIST'а второго занятия и доработайте их
from classes import Deck, Card

player_money = 100  # Деньги игрока
rate_value = 10  # Размер ставки

deck = Deck()


def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    sum_pts = 0
    for card in cards:
        sum_pts += card.points
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_pts > 21:
        sum_pts = 0
        for card in cards:
            if card.value == 'A':
                sum_pts += 1
            else:
                sum_pts += card.points
    return sum_pts


while True:
    # 0. Игрок делает ставку
    player_money -= rate_value
    # 1. В начале игры перемешиваем колоду
    deck.shuffle()
    # 2. Игроку выдаем две карты
    player_cards = deck.draw(2)
    # 3. Дилер берет одну карту
    dealer_cards = deck.draw(1)
    # 4. Отображаем в консоли карты игрока и дилера
    print(f'Игрок: ')
    print(*player_cards)
    print('Дилер: ')
    print(*dealer_cards)
    # 5. Проверяем нет ли у игрока блэкджека (21 очко)
    if sum_points(player_cards) == 21:
        # Выплачиваем выигрышь 3 и 2
        player_money += rate_value * 2.5
        print("Black Jack!!! Игрок победил")
        # Заканчиваем игру
        print(f'Ваш счет: {player_money}')
        player_cards.clear()
        dealer_cards.clear()
        print('====конец раунда====\n')
        continue
    # Если нет блэкджека, то
    while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
        player_choice = input("еще(1)/достаточно(0): ")
        if player_choice == "1":
            # Раздаем еще одну карту
            player_cards += deck.draw(1)
            print(f'Игрок: ')
            print(*player_cards)
            # Если перебор (>21), заканчиваем добор
            if sum_points(player_cards) > 21:
                print(f"Перебор: {sum_points(player_cards)} очков")
                print(f'Ваш счет: {player_money}')
                player_cards.clear()
                dealer_cards.clear()
                print('====конец раунда====\n')
                break
            elif sum_points(player_cards) == 21:
                print(f"Блэк Джэк: {sum_points(player_cards)} очко")
                player_money += rate_value * 2.5
                print(f'Ваш счет: {player_money}')
                player_cards.clear()
                dealer_cards.clear()
                print('====конец раунда====\n')
                break
            continue

        # Если у игрока не 21(блэкджек) и нет перебора, то
        if player_choice == "0":
            # Заканчиваем добирать карты
            print("Диллер добирает карты")
            while True:  # дилер начинает набирать карты.
                dealer_cards += deck.draw(1)
                print(f'Дилер: ')
                print(*dealer_cards)
                if sum_points(dealer_cards) >= 17:
                    break
        break

    # Выясняем кто набрал больше очков. Выплачиваем/забираем ставку

    if sum_points(player_cards) == sum_points(dealer_cards) \
            and sum_points(player_cards) > 0 \
            and sum_points(dealer_cards) > 0:
        print(f'Ничья с результатом {sum_points(player_cards)} очков и '
              f'{sum_points(dealer_cards)} очков у дилера')
        print(f'Ваш счет: {player_money}')
    elif sum_points(player_cards) > sum_points(dealer_cards):
        print(
            f'Вы выиграли с результатом {sum_points(player_cards)} очков против '
            f'{sum_points(dealer_cards)} очков у дилера')
        player_money += rate_value * 1.5
        print(f'Ваш счет: {player_money}')
    elif sum_points(dealer_cards) > 21:
        print(
            f'Вы выиграли с результатом {sum_points(player_cards)} очков против '
            f'{sum_points(dealer_cards)} очков, у дилера перебор')
        player_money += rate_value * 1.5
        print(f'Ваш счет: {player_money}')
    elif sum_points(player_cards) < sum_points(dealer_cards):
        print(
            f'Вы проиграли с результатом {sum_points(player_cards)} очков против '
            f'{sum_points(dealer_cards)} очков у дилера')
        print(f'Ваш счет: {player_money}')
    else:
        continue
    print('====конец раунда====\n')
