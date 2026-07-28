class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # num_idxs = {numbers[i]: i+1 for i in range(len(numbers))}

        # for i in range(len(numbers)):
        #     want = num_idxs.get(target - numbers[i])
        #     if want:
        #         return [i + 1, want]

        start, end = 0, len(numbers) - 1

        numbers.sort()
        while start < end:
            curr = numbers[start] + numbers[end]
            if curr == target:
                return [start + 1, end + 1]
            
            elif curr < target:
                start += 1
            else:
                end -= 1
        
        return []