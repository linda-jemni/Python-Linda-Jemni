class Calculette:

    def add(self,a,b):
        return a+b
        
    def multi(self,a,b):
        return a*b
        
    def div(self,a,b):
        if b==0:
            print("opp is not possible !!")
            raise ZeroDivisionError
        return a/b
        
    def sous(self,a,b):
        return a-b