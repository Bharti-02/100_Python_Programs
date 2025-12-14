class Solution:
    def duplicate(self,l1,l2):
        for i in l1:
            if i not in l2:
                l2.append(i)
        return l2
            
            
obj=Solution()       
l1=[10,20,30,40,40,40,50]
l2=[]
result=obj.duplicate(l1,l2)
print(result)