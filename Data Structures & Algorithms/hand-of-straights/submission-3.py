class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        s = sorted(freq.keys())

        for j in s:
            while freq[j] != 0:
                for i in range(groupSize):
                    if freq[j+i] > 0:
                        freq[j+i] -= 1
                    else:
                        return False

        return True