class Solution:
    def findKthSmallestElement(self, nums1: List[int], nums2: List[int], k:int) -> float:

        m = 0
        n = 0
        res = 0.0

        while k > 1 and m < len(nums1) and n < len(nums2):

            w1 = min(k//2, len(nums1) - m)
            w2 = min(k//2, len(nums2) - n)

            if nums1[m+w1-1] <= nums2[n+w2-1]:
                m = m + w1
                k -= w1
            else:
                n = n + w2  
                k -= w2  

        if k == 1:
            if m == len(nums1):
                res = nums2[n]
            elif n == len(nums2):
                res = nums1[m]
            else:
                res = min(nums1[m], nums2[n])    

        elif m < len(nums1):  
            res = nums1[m+k-1]
        else:
            res = nums2[n+k-1]

        return res        
                  
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = 0.0

        k = (len(nums1) + len(nums2)) // 2    # Median rank

        if (len(nums1)+len(nums2))%2 == 1:
            res = self.findKthSmallestElement(nums1,nums2,k+1)
        else:
            res = (self.findKthSmallestElement(nums1,nums2,k) + self.findKthSmallestElement(nums1,nums2,k+1)) / 2

        return res

        