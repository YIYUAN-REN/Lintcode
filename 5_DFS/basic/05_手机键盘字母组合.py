# Letter Combinations of a Phone Number

"""
每层代表的意义：n层，每层决定放当前数字对应的哪个字母
每层多少个状态：3-4个状态，放哪个字母

Time O(4^n)
"""

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
            
        results = []
        self.dfs(0, [], digits, results)
        return results
    
    
    def dfs(self, index, combination, digits, results):
        if index == len(digits):
            results.append(''.join(combination))
            return
        
        for letter in KEYBOARD[digits[index]]:
            combination.append(letter)
            self.dfs(index + 1, combination, digits, results)
            combination.pop()