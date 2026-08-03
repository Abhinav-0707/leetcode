class Solution(object):
    def power(self,x,n):
        if n==0:
            return 1
        a=self.power(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x
    def myPow(self, x, n):
        if n>0:
            return self.power(x,n)
        else:
            return 1/self.power(x,(n*-1))

