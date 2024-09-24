import random

# 定义扑克牌的花色和面值
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


# 创建一副牌
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    return deck


# 发牌
def deal_cards(deck, num_cards):
    hand = random.sample(deck, num_cards)
    for card in hand:
        deck.remove(card)
    return hand


# 确定手牌的等级
def hand_rank(hand, community_cards):
    all_cards = hand + community_cards
    values = [ranks.index(card[:-1]) for card in all_cards]
    values.sort()
    suits_set = set([card[-1] for card in all_cards])
    is_flush = len(suits_set) == 1
    is_straight = False
    consecutive_values = [values[0]]
    for value in values[1:]:
        if value - consecutive_values[-1] == 1:
            consecutive_values.append(value)
            if len(consecutive_values) == 5:
                is_straight = True
                break
        else:
            consecutive_values = [value]
    if values == [0, 1, 2, 3, 12]:
        is_straight = True
    if is_straight and is_flush:
        return 8  # 同花顺
    elif any([values.count(value) == 4 for value in values]):
        return 7  # 四条
    elif any([values.count(value) == 3 and values.count(other_value) == 2 for value in values for other_value in values
              if value != other_value]):
        return 6  # 葫芦
    elif is_flush:
        return 5  # 同花
    elif is_straight:
        return 4  # 顺子
    elif any([values.count(value) == 3 for value in values]):
        return 3  # 三条
    elif any([values.count(value) == 2 and values.count(other_value) == 2 for value in values for other_value in values
              if value != other_value]):
        return 2  # 两对
    elif any([values.count(value) == 2 for value in values]):
        return 1  # 一对
    else:
        return 0  # 高牌


# 比较两手牌的大小
def compare_hands(player_hand, computer_hand, community_cards):
    player_rank = hand_rank(player_hand, community_cards)
    computer_rank = hand_rank(computer_hand, community_cards)
    if player_rank > computer_rank:
        return 1
    elif player_rank < computer_rank:
        return 2
    else:
        player_values = [ranks.index(card[:-1]) for card in player_hand + community_cards]
        computer_values = [ranks.index(card[:-1]) for card in computer_hand + community_cards]
        while player_values and computer_values:
            high_card_player = max(player_values)
            high_card_computer = max(computer_values)
            if high_card_player > high_card_computer:
                return 1
            elif high_card_player < high_card_computer:
                return 2
            else:
                player_values.remove(high_card_player)
                computer_values.remove(high_card_computer)
        return 0


# 显示手牌
def show_hand(hand, community_cards=None):
    if community_cards:
        print(f"你的手牌和公共牌：{hand}, {community_cards}")
    else:
        print(f"你的手牌：{hand}")


# 下注环节
def betting_round(chips):
    bet = 0
    while True:
        try:
            print(f"你当前有 {chips} 个筹码。")
            bet_input = input("请输入你的下注金额：")
            bet = int(bet_input)
            if bet > chips:
                print("你的下注金额不能超过你拥有的筹码数量。")
            else:
                break
        except ValueError:
            print("请输入有效的数字。")
    return bet


# 游戏主逻辑
def play_poker():
    deck = create_deck()
    player_hand = deal_cards(deck, 2)
    computer_hand = deal_cards(deck, 2)
    community_cards = []
    chips = 1000
    print("欢迎来到德州扑克游戏！你的初始筹码为 1000。\n")

    show_hand(player_hand)
    # 第一轮下注
    player_bet = betting_round(chips)
    chips -= player_bet
    # 发三张公共牌
    community_cards.extend(deal_cards(deck, 3))
    show_hand(player_hand, community_cards)
    # 第二轮下注
    player_bet = betting_round(chips)
    chips -= player_bet
    # 发第四张公共牌
    community_cards.append(deal_cards(deck, 1)[0])
    show_hand(player_hand, community_cards)
    # 第三轮下注
    player_bet = betting_round(chips)
    chips -= player_bet
    # 发第五张公共牌
    community_cards.append(deal_cards(deck, 1)[0])
    show_hand(player_hand, community_cards)
    result = compare_hands(player_hand, computer_hand, community_cards)
    if result == 1:
        print("你赢了！")
        chips += player_bet * 2
    elif result == 2:
        print("电脑赢了！")
    else:
        print("平局！")
        chips += player_bet
    print(f"游戏结束，你现在有 {chips} 个筹码。")


if __name__ == '__main__':
    play_poker()
