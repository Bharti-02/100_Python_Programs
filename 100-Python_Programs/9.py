class Solution:
    def Largest(self,a):
        lar=a[0]
        for i in a:
            if i > lar:
                lar=i
        return lar
                    
        
        
        
obj=Solution()
a=[12,3,4,5,6,7,8,99,43]
result=obj.Largest(a)
print(result)