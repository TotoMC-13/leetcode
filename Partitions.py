from typing import List, Dict, Tuple

class Solution:
    def __init__(self):
        self.res: List[int] = []

    def partitionLabels(self, s: str) -> List[int]:
        ...

    def get_intervals(self, s: str):
        intervals: Dict[Tuple[int, int]] = {}

        for letter in s:
            intervals[letter] = (0,0)

        for letter in intervals.keys():
            first: int = None
            last: int = None

            for i, l in enumerate(s):
                if l == letter:
                    if first is None:
                        first = i + 1
                    else:
                        last = i + 1
                
            if last is None:
                last = first
            
            intervals[letter] = (first, last)

        print(intervals)

x = "aabbssagf"

s = Solution()
s.get_intervals(x)
