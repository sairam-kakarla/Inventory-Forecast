#Storage Volume Estimation based on profit 
class item:
    
    def __init__(self,name,brand,SP,CP,discount,stock):
        self.name=name
        self.brand=brand
        self.CP=CP
        self.discount=discount
        self.SP=SP
        self.stock=stock
    
    def profit_percent(self):
        return(((self.SP*(1-(self.discount/100))-self.CP))/self.CP)
    
    def profit(self):
        return(round(self.SP*(1-self.discount/100)-self.CP,5))

class space:
    def __init__(self,name,capacity):
        self.name=name
        self.capacity=capacity

def sort_rack(rack):
    for i in range(len(rack)-1):
        min=i
        for j in range(i+1,len(rack)):
            if rack[min][1] >rack[j][1]:
                min=j
        rack[min],rack[i]=rack[i],rack[min]

class Rack_Maxim:
    
    @staticmethod
    def getMaxValue(rack,capacity):
        max_storage=capacity
        total_CP=0
        sort_rack(rack)
        index=len(rack)-1
        while(capacity>0):
            pass


            


        




if __name__=='__main__':
    rice_rack=space("rice",100)
    rice1=item("rice","Pusa",4500,4200,5,25)
    rice2=item("rice","Sella",4400,4000,3,20)
    rice3=item("rice","Steam",4700,4500,3,25)
    rice4=item("rice","Golden Sella",3600,3000,0,30)
    rice5=item("rice","Golden Steam",2300,2000,10,30)
    rack=[rice1,rice2,rice3,rice4,rice5]
    rack_main=[]
    for i in rack:
        rack_main.append((i.brand,round(i.profit_percent()/i.stock,6),i.stock,i.profit(),i.CP))
    sort_rack(rack_main)
    for i in rack_main:
        print(i)
    
    


    
    
