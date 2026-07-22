class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cards = Counter(hand)

        while cards:
            m = min(cards)

            for i in range(groupSize):
                card = m + i

                if card not in cards:
                    return False
                else:
                    cards[card] -= 1
                
                if cards[card] == 0:
                    del cards[card]
        
        return True