class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign=1
        sub_str=''
        num_found=False
        for c in str:
            if num_found is False:
                if c == ' ':
                    continue
                elif c =='+':
                    num_found=True
                elif c == '-':
                    num_found=True
                    sign=-1
                elif c.isdigit():
                    num_found=True
                    sub_str+=c
                else:
                    return 0
            else:
                if c.isdigit():
                    sub_str+=c
                else:
                    break
        return self.String_to_Int(sub_str,sign)

    def String_to_Int(self,s,sign):
        num=0
        INT_MIN=-2147483648
        INT_MAX=2147483647
        if sign==-1:
            max=-INT_MIN
        else:
            max=INT_MAX
        times=1
        for n in reversed(s):
            num+=int(n)*times
            times*=10
            if num>max:
                num=max
                break
        return num*sign

if __name__ == '__main__':
    a=Solution()
    c=a.myAtoi('       -3.8979789dfsfsdf')
    print(c)