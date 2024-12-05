class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def peri(self):
        return 2*(self.length+self.breadth)
    def is_square(self):
        if self.length==self.breadth:
            return True
        return False

length=int(input("Enter the length :"))
breadth=int(input("Enter the breadth :"))
if length<0 or breadth<0 :
    raise Exception("ValueError")
else:
    obj=Rectangle(length,breadth)
    print("Area:",obj.area())
    print("Perimeter:",obj.peri())
    print("Is_square:",obj.is_square())
    
        
        