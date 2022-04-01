# High Five

"""
思路: hashmap嵌套min heap (维持5个)
"""

import heapq

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

class Solution:
    # @param {Record[]} records a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, records):
        # Write your code here

        # build id-score mapping with top 5 scores
        id_to_scores = {}
        for record in records:
            if record.id not in id_to_scores:
                id_to_scores[record.id] = [record.score]
            else:
                min_heap = id_to_scores[record.id]
                heapq.heappush(min_heap, record.score)
                if len(min_heap) > 5:
                    heapq.heappop(min_heap)

        # build id-average mapping
        id_to_average = {}
        for id, scores in id_to_scores.items():
            id_to_average[id] = sum(scores) / 5
        
        return id_to_average
