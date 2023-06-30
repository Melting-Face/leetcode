class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for i in range(1, n + 1):
            value = str(i)
            if i % 3 == 0 and i % 5 == 0:
                value = "FizzBuzz"
            elif i % 3 == 0:
                value = "Fizz"
            elif i % 5 == 0:
                value = "Buzz"
            arr.append(value)
        return arr