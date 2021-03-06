class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for num in range(1, n+1):
            
            divisible_by_3 = (num % 3) == 0
            divisible_by_5 = (num % 5) == 0
            
            if divisible_by_3 and divisible_by_5:
                answer.append("FizzBuzz")
            elif divisible_by_3:
                answer.append("Fizz")
            elif divisible_by_5:
                answer.append("Buzz")
            else:
                answer.append(str(num))
            
        
        return answer
