from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        chars = list(corpus)
        merges = []
        for i in range(num_merges):
            freq = {}
            for i in range(len(chars) - 1):
                pair = (chars[i], chars[i + 1])
                freq[pair] = freq.get(pair, 0) + 1
            
            max_val = max(freq.values())
            all_maxes = [k for k, v in freq.items() if v == max_val]
            merge = sorted(all_maxes)[0]

            l = 0
            r = 1

            while r < len(chars):
                if chars[l] == merge[0] and chars[r] == merge[1]:
                    chars[l] = merge[0] + merge[1]
                    chars.pop(r)
                
                l += 1
                r += 1
            
            merges.append(merge)

        return merges
                

            


                


