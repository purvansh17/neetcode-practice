class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        sorted_list = sorted(count.items(), reverse=True, key=lambda item: item[1])
        # print(sorted_list)

        output = []
        for i in range(k):
            output.append(sorted_list[i][0])

        return output
