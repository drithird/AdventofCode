import re
from dataclasses import dataclass

@dataclass
class Hand:
    cards: str
    bet: int
    matches: int
    powercard: str 
    rank: int

def count_matches(hand):
    cards = [card for card in hand]
    total_matches =[]
    for card in hand:
        current_count = 0
        for matching_card in cards:
            if matching_card == card:
                current_count += 1
        total_matches.append([card,current_count])
    ranked_matches = sorted(total_matches, key=lambda x: x[1],reverse=True)
    return ranked_matches[0][1]
                
def sort_hands(hands: list[Hand]):
    four = []
    three_of_a_kind = []
    pair = []
    one = []
    zero = []
    hand_power_converter = {'A':14,'K':13,'Q':12,'J':11,'10':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    for hand in hands:
        if hand.matches == 0:
            zero.append([hand,hand_power_converter[hand.powercard]])
        elif hand.matches == 1:
            one.append([hand,hand_power_converter[hand.powercard]])
        elif hand.matches == 2:
            pair.append([hand,hand_power_converter[hand.powercard]])
        elif hand.matches == 3:
            three_of_a_kind.append([hand,hand_power_converter[hand.powercard]])
        elif hand.matches == 4:
            four.append([hand,hand_power_converter[hand.powercard]])
       
    print(two)
            
pattern = r'(\w{5}) (\d+)'
hands = []
with open('adventofcode/day7/file.txt','r') as file:
    text = file.read()
hands_and_bets = re.findall(pattern,text)
for hand_and_bet in hands_and_bets:
    cards = hand_and_bet[0]
    bet = hand_and_bet[1]
    matches = count_matches(cards)
    powercard = cards[0]
    rank = 1001
    hands.append(Hand(cards,bet,matches,powercard,rank))
    break
print(hands)
sorted_hands = sort_hands(hands)
    

