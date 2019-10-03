class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area=0
        first,last=0,len(height)-1
        while first<last:
            max_area=max(max_area,min(height[first],height[last])*(last-first))
            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        return max_area

if __name__ == '__main__':
    a=Solution()
    c=a.maxArea([1,8,6,2,5,4,8,3,7])
    print(c)