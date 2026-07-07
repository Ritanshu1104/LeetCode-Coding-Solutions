class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Extract non-zero digits as a string
        digits = [d for d in str(n) if d != '0']
        
        # If no non-zero digits exist, x = 0
        if not digits:
            return 0
        
        # Form integer x and calculate the sum of its digits
        x = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)
        
        return x * digit_sum
