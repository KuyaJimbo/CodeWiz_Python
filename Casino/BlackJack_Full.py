import random

def calculate_score(hand):
    score = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 1
        else:
            score += int(card)
    return score

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
random.shuffle(deck)

player_hand = []
dealer_hand = []

card = deck.pop()
player_hand.append(card)
card = deck.pop()
dealer_hand.append(card)
card = deck.pop()
player_hand.append(card)

player_score = 0
dealer_score = 0

player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)

print(f"Player hand: {player_hand} ({player_score})")
print(f"Dealer hand: {dealer_hand} ({dealer_score})")

while True:
    print("Do you want to hit or stand? (hit or stand)")
    choice = input()
    if choice == "hit":
        card = deck.pop()
        player_hand.append(card)
        player_score = calculate_score(player_hand)
    else:
        break

    print(f"Player hand: {player_hand} ({player_score})")
    print(f"Dealer hand: {dealer_hand} ({dealer_score})")

while dealer_score < 17:
    card = deck.pop()
    dealer_hand.append(card)
    dealer_score = calculate_score(dealer_hand)
    print(f"Dealer hand: {dealer_hand} ({dealer_score})")

print("Final hands:")
print(f"Player hand: {player_hand} ({player_score})")
print(f"Dealer hand: {dealer_hand} ({dealer_score})")
