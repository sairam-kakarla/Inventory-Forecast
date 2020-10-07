import data
class item:
    
    def _init_(self,name,brand,SP,CP,discount,stock):
        self.name=name
        self.brand=brand
        self.CP=CP
        self.discount=discount
        self.SP=SP
        self.stock=stock

class space:
    def _init_(self,name,capacity):
        self.name=name
        self.capacity=capacity

rice_rack=space("rice",100)
rice1=item("rice","Pusa",4500,4200,5,25)
rice2=item("rice","Sella",4400,4000,3,20)
rice3=item("rice","Steam",4700,4500,3,25)
rice4=item("rice","Golden Sella",3600,3000,0,30)
rice5=item("rice","Golden Steam",2300,2000,10,30)
rack=[rice1,rice2,rice3,rice4,rice5]
rack_main=[]

for i in range(len(rack)):
     dis =0
     q = data.predictor(dis)
     prof  = float((rack[i].SP-rack[i].CP)*q)
     rack_main.append((0,rack[i].SP,(rack[i].SP-rack[i].CP)*q))
     for j in range(1,7):
         s = int(rack[i].SP)
         q = data.predictor(j)
         for k in range(s,s+100):
            dis = j/100
            SP = float((1-dis)*k*q)
            CP = float(rack[i].CP*q)
            p = float(SP - CP)
            if(prof<p):
                prof = p
                rack_main.pop(len(rack_main)-1)
                rack_main.append((dis,k,float(p)))

print(rack_main)