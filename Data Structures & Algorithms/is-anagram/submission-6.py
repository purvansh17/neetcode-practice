class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in s:
            # print(s_dict)
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        
        for j in t:
            # print(t_dict)  
            if j not in t_dict:
                t_dict[j] = 1
            else:
                t_dict[j] += 1

        return s_dict == t_dict 