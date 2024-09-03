class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        hasGreatestCandies = 0
        greatestList = []
        for i in candies:
            if hasGreatestCandies <= i:
                hasGreatestCandies = i
        
        for j in candies:
            amount = j + extraCandies
            if hasGreatestCandies <= amount:
                greatestList.append(True)
            else:
                greatestList.append(False)

        return greatestList