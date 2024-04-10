class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = [0] + flowerbed + [0]
        flower_length = len(flowers)
        flowerbed_count = -1
        for idx, flower in enumerate(flowers):
            if flower == 0:
                flowerbed_count += 1

            if flower == 1 or idx == (flower_length - 1):
                if flowerbed_count > 0:
                    n -= flowerbed_count >> 1
                if n <= 0:
                    return True
                flowerbed_count = -1
        return False