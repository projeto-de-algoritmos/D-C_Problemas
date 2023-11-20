class Solution:
    nbb = {
        "2": ["a", "b","c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p","q","r","s"], 
        "8": ["t", "u", "v"],
        "9": ["w","x","y","z"]
          }
		  
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
		
        n = len(digits)
        if n == 1 or digits in self.nbb:
            return self.nbb[digits]
        
        pivot = n//2
        left = self.letterCombinations(digits[:pivot])
        right = self.letterCombinations(digits[pivot:])
		
        self.nbb[digits] = [i + j for i in left for j in right]
		
        return self.nbb[digits]