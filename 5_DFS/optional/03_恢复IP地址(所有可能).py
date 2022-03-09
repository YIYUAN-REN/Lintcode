# Restore IP Addresses

"""
思路：DFS，每个node最少1个数最多3个数，还要判断范围<=255且排除"01, 002, ..."
每层意义：4层，每层决定1部分IP
每层状态：当前部分保留几个数
"""

class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        self.dfs(0, [], s, results)
        return results
    
    
    def dfs(self, index, parts, s, results):
        if index == len(s):
            if len(parts) == 4:
                results.append('.'.join(parts))
            return
        
        if len(parts) == 4: # 剪枝
            return
        
        for i in range(1, 4):
            if index + i > len(s): # 越界, len(s)是右边界
                break

            part = s[index:index+i]
            if int(part) > 255 or len(part) > 1 and part[0] == '0':
                continue
            
            parts.append(part)
            self.dfs(index + i, parts, s, results)
            parts.pop()
