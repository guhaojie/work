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


def deal_cards(deck_of_cards, player_num, num_of_cards):
    pass


b = new_deck_of_cards()
b = random_shuffle(b)
