# https://www.codingame.com/ide/puzzle/winamax-battle

cardp_1, cardp_2 = [], []
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2.append(input())  # the m cards of player 2

# initialization
is_war, game_rounds = False, 0
cards_to_win_1, cards_to_win_2 = [], []


def is_game_over(cardp_1, cardp_2):
    """ check if there is a winner or a draw 
        returns: -1 (no winner), 0 (draw), 1 or 2 """
    winner = -1
    if cardp_1 == cardp_2 == []:
        winner = 0
    elif cardp_1 == []:
        winner = 2
    elif cardp_2 == []:
        winner = 1
    return winner


def getCardIntValue(card):
    """ return card integer value (instead of J, Q, K, A """
    c0, _ = card[:-1], card[-1]
    if c0 == 'J':
        c0 = 11
    elif c0 == 'Q':
        c0 = 12
    elif c0 == 'K':
        c0 = 13
    elif c0 == 'A':
        c0 = 14
    return int(c0)


# algo start
while True:

    winner = is_game_over(cardp_1, cardp_2)
    if winner >= 0:
        break

    if not is_war:
        game_rounds += 1

    top_1 = cardp_1.pop(0)
    top_2 = cardp_2.pop(0)

    c10 = getCardIntValue(top_1)
    c20 = getCardIntValue(top_2)

    if c10 == c20:  # war starts
        cards_to_win_1 += [top_1] + cardp_1[:3]
        cards_to_win_2 += [top_1] + cardp_2[:3]
        cardp_1, cardp_2 = cardp_1[3:], cardp_2[3:]
        # If a player runs out of cards during a "war" (when giving up the three cards or when doing the battle),
        # then the game ends and both players are placed equally first.
        if cardp_1 == [] or cardp_2 == []:
            winner = 0
            break
        is_war = True
    elif is_war == True:  # war ends
        ctw = cards_to_win_1 + [top_1] + cards_to_win_2 + [top_2]
        if c10 > c20:
            cardp_1 += ctw
        elif c10 < c20:
            cardp_2 += ctw
        cards_to_win_1, cards_to_win_2 = [], []
        is_war = False
    else:  # regular battle
        if c10 > c20:
            cardp_1 += [top_1, top_2]
        else:
            cardp_2 += [top_1, top_2]

if winner == 0:
    print('PAT')
else:
    print(f'{winner} {game_rounds}')
