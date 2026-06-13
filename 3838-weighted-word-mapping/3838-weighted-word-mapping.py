class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        result = []
        
        for word in words:
            # 1. Calculate the sum of weights for the current word
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # 2. Get the index modulo 26
            index = total_weight % 26
            
            # 3. Map to reverse alphabetical character (0='z', 1='y', ..., 25='a')
            mapped_char = chr(ord('z') - index)
            result.append(mapped_char)
            
        return "".join(result)