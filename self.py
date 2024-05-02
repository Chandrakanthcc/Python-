class sqauare:
    def __init__(self,length) -> None:
        if type(length) not in [int,float]:
            raise TypeError('length must be an integer ornfloat')
        if length<0:
            raise ValueError("length must be not negative")
         
        self.length = length
    
    def area(self):
        return self.length + self.length
    