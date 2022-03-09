# Substring With At Least K Distinct Characters

"""
思路：动态滑动窗口，hashmap记录窗口内不同字符的个数
循环
    若len(visited) < k，则fast前进，visited增加。
    若len(visited) == k，则添加count，visited减少，slow前进。
"""

class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        count = 0
        slow = fast = 0
        visited = {s[0]: 1}
        
        while fast < len(s):
            if len(visited) < k:
                fast += 1
                if fast == len(s):
                    break
                
                if s[fast] not in visited:
                    visited[s[fast]] = 1
                else:
                    visited[s[fast]] += 1
                
            else:
                count += (len(s) - fast)    # 因为求至少k个不同字符，如果是等于k个则 count += 1
                visited[s[slow]] -= 1
                if visited[s[slow]] == 0:
                    del visited[s[slow]]
                slow += 1
        
        return count