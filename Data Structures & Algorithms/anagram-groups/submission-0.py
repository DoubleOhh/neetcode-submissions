#we need to have the list broken up into sub lists 
# anagrams have the same number of the same letters order does not matter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we use a default dict b/c we need to create a new spot if we encounter a word with a comb of letters we have never seen before
        out = defaultdict(list)

        for word in strs:
            key = tuple(sorted(Counter(word).items()))

            out[key].append(word)
        
        return out.values()

    

            
        