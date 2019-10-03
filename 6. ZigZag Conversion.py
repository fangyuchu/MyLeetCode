class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        s_convert=str()
        for i in range(numRows):
            s_convert+=self.find_sub_string(s[i:],i+1,numRows)
        return s_convert

    def find_sub_string(self,s,rowth,numRows):
        sub_string=str()
        i=0
        zigzag=-1
        while i < len(s):
            sub_string+=s[i]
            zigzag+=1
            if (zigzag%2==0 or rowth==1) and rowth!=numRows:
                i+=(numRows-rowth)*2
            else:
                i+=(rowth-1)*2
        return sub_string


if __name__ == '__main__':
    a=Solution()
    c=a.convert('abcd',4)
    print(c)