class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create map of most nums and their frequency
        most_common = {}
        for num in nums:
            if num in most_common:
                most_common[num] += 1
            else:
                most_common[num] = 1
        # Pair them num and frequency into tupes and sort them from biggest to smallest
        pairs = []
        for num, count in most_common.items():
            pairs.append((count, num))
        pairs.sort(reverse=True)
        # Slice out the k number of pairs and append each key to the the output array
        output = []
        for count, num in pairs[:k]:
            output.append(num)
        return output