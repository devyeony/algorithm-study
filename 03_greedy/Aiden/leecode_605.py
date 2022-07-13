class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       add_flowerbed = [0] + flowerbed + [0]
       s = len(flowerbed)
        
       for i in range(1, s+1):
           if add_flowerbed[i] == add_flowerbed[i-1] == add_flowerbed[i+1] == 0:
               print(i)
               add_flowerbed[i] = 1
               n -= 1
           if n <= 0:
               return True

       return False