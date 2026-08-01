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
        # half is the number of elements to the left of partition
        half = (m + n + 1) // 2 # adding plus one so our assumption is the last element of the left side of partition
                                # will be the median in case of odd — if even we add that element with the min element right of partition

        lo, hi = 0, m
        while lo <= hi:
            i_1 = (lo + hi) // 2
            i_2 = half - i_1

            left1 = nums1[i_1 - 1] if i_1 > 0 else float('-inf')
            right1 = nums1[i_1] if i_1 < m else float('inf')
            left2 = nums2[i_2 - 1] if i_2 > 0 else float('-inf')
            right2 = nums2[i_2] if i_2 < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    # return max element to left of partition if odd
                    return float(max(left1, left2))
                else:
                    # otherwise return avg of elements directly on each side of overall partition
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                
                
            if left1 > right2:
                hi = i_1 - 1
            else:
                lo = i_1 + 1
            