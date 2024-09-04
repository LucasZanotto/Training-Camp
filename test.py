class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                empty_before = (i == 0) or (flowerbed[i-1] == 0)
                empty_after = (i == length - 1) or (flowerbed[i+1] == 0)
                
                if empty_before and empty_after:
                    flowerbed[i] = 1
                    count += 1
                    
                    if count >= n:
                        return True
    
        return count >= n