class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        word_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in word_dict.keys():
                word_dict[sorted_word].append(word)
            else:
                word_dict[sorted_word] = [word]
        
        for ag_lists in word_dict.values():
            output.append(ag_lists)
        
        return output

