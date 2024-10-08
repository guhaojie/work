def new_deck_of_cards():
    suits = "♠♥♣♦"
    ranks = "23456789TJQKA"
    res = []
    for _i in suits:
        for _j in ranks:
            res.append(_i + _j)
    return res


def random_shuffle_cards(deck_of_cards):
    import random
    len_of_cards = len(deck_of_cards)
    res = []
    while len_of_cards:
        res.append(deck_of_cards.pop(random.randint(0, len_of_cards - 1)))
        len_of_cards = len(deck_of_cards)
    return res


def deal_player_cards(deck_of_cards, player_num, num_of_cards):
    res = []
    for _ in range(player_num):
        res.append([])
    for _ in range(num_of_cards):
        for _i in range(player_num):
            res[_i].append(deck_of_cards.pop())
    return res

def deal_flop_cards(deck_of_cards):
    deck_of_cards.pop()
    return [deck_of_cards.pop(), deck_of_cards.pop(), deck_of_cards.pop()]

def deal_turn_or_river_cards(deck_of_cards):
    deck_of_cards.pop()
    return [deck_of_cards.pop()]


deck = new_deck_of_cards()
deck = random_shuffle_cards(deck)
player_cards = deal_player_cards(deck, 5, 2)
flop_cards = deal_flop_cards(deck)
turn_card = deal_turn_or_river_cards(deck)
river_card = deal_turn_or_river_cards(deck)

print(flop_cards, turn_card, river_card)
for _ in player_cards:
    print(_)
