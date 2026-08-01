class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m, n = len(nums1), len(nums2)
        # combined = []

        # target_idx = (m + n) // 2
        # i_1 = 0
        # i_2 = 0
        # count = 0
        # while count <= target_idx:
        #     if i_1 >= m:
        #         combined.extend(nums2[i_2:])
        #         break
        #     if i_2 >= n:
        #         combined.extend(nums1[i_1:])
        #         break

        #     if nums1[i_1] <= nums2[i_2]:
        #         combined.append(nums1[i_1])
        #         i_1 += 1
        #     else:
        #         combined.append(nums2[i_2])
        #         i_2 += 1
        #     count += 1
        
        # if (m + n) % 2 == 0:
        #     return (combined[target_idx] + combined[target_idx - 1]) / 2
        # else:
        #     return combined[target_idx]

        # Above Solution is O(m+n)
        if len(nums1) > len(nums2):    
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i]  if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j]  if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
                
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1

            