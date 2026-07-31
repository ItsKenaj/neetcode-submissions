class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        combined = []

        target_idx = (m + n) // 2
        i_1 = 0
        i_2 = 0
        count = 0
        while count <= target_idx:
            if i_1 >= m:
                combined.extend(nums2[i_2:])
                break
            if i_2 >= n:
                combined.extend(nums1[i_1:])
                break

            if nums1[i_1] <= nums2[i_2]:
                combined.append(nums1[i_1])
                i_1 += 1
            else:
                combined.append(nums2[i_2])
                i_2 += 1
            count += 1
        
        if (m + n) % 2 == 0:
            return (combined[target_idx] + combined[target_idx - 1]) / 2
        else:
            return combined[target_idx]
            
            