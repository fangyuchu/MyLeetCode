class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        two_sum=dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                key=nums[i]+nums[j]
                if two_sum.get(key) is None:
                    two_sum[key]=sum_pair(key)
                two_sum[key].add_pair([i,j])
        triplets=list()
        for i in range(len(nums)):
            key=0-nums[i]
            if two_sum.get(key) is None:
                continue
            for p in two_sum[key].pair:
                if i in p:
                    continue
                triplets.append([nums[i],nums[p[0]],nums[p[1]]])
        return triplets


class sum_pair(object):
    def __init__(self,key):
        self.key=key
        self.pair=list()
    def add_pair(self,pair):
        for p in self.pair:
            if (p>pair)-(p<pair)==0:        #p and pair are identical lists
                return
        self.pair.append(pair)

if __name__ == '__main__':
    a=Solution()
    a.threeSum([-1, 0, 1, 2, -1, -4])