#we need to have the list broken up into sub lists 
# anagrams have the same number of the same letters order does not matter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we use a default dict b/c we need to create a new spot if we encounter a word with a comb of letters we have never seen before
        out = defaultdict(list)

        for word in strs:
        # Initialize count array of 26 zeroes
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1  # Count each character
            
            key = tuple(count)  # Use count tuple as hashable key
            
            out[key].append(word)
        
        return out.values()

    

            
        