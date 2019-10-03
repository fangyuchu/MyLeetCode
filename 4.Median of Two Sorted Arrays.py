class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1=len(nums1)
        len2=len(nums2)
        length=len1+len2
        

        print()


if __name__ == '__main__':
    a=Solution()
    c=a.findMedianSortedArrays([1,2,5],[3,4])
    print(c)