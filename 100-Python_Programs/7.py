class Solution:
    def sor_arr(self,a):
        if sorted(a,reverse=True) == a:
            return True 
        else:
            return False

obj=Solution()
a=[10,20,30,40,50]
result=obj.sor_arr(a)
print(result)