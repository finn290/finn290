#30/4/21
#This is a simple oop program to help me get it

class vehicle:
    def __init__(self,VEL,VIN,MILAGE,SEAT,PRICE):
        self._speed = int(VEL)
        self.plate = (VIN)
        self.milage = int(MILAGE)
        self.seat = int(SEAT)
    def returnspd(self):
     
        return(self.plate)

        
class lorry(vehicle):
    def __init__(self,VEL,VIN,MILAGE,SEAT,PRICE, kg,cargo,vehicle,tow):
        super().__init__(VEL,VIN,MILAGE,SEAT,PRICE)
        self.weight = int(kg)
        self.space = int(cargo)
        self.tow = bool(tow)
dafxf =lorry(3,'eu06 daf',12,2,500000,1300,500,6,False)
print(dafxf._speed)
print(dafxf.returnspd())
