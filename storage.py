#Storage Volume Estimation based on profit 
class item:
    
    def __init__(self,name,brand,MP,CP,discount,stock):
        self.name=name
        self.brand=brand
        self.CP=CP
        self.discount=discount
        self.MP=MP
        self.stock=stock
    
    def profit_percent(self):
        return(((self.MP*(1-(self.discount/100))-self.CP))/self.CP)
    
    def profit(self):
        return(round(self.MP*(1-self.discount/100)-self.CP,5))

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
# Greedy about profit percentage by stock approach to find 
# optimal cost price  and for maximum profits and optimal stock
class Rack_Maxim:
    
    @staticmethod
    def getMaxValue(rack,capacity):
        max_storage=capacity
        max_profit=0
        total_CP=0
        sort_rack(rack)
        index=len(rack)-1
        log={}
        while(max_storage>0):
            if rack[index][2]<=max_storage:
                log[rack[index][0]]=(rack[index][2],rack[index][4])
                total_CP+=rack[index][2]*rack[index][4]
                max_profit+=rack[index][2]*rack[index][3]
                max_storage-=rack[index][2]
            elif rack[index][2]>max_storage:
                log[rack[index][0]]=(max_storage,rack[index][4])
                total_CP+=max_storage*rack[index][4]
                max_profit+=max_storage*rack[index][3]
                max_storage-=max_storage
            index-=1
        print("Available stock capacity: ",capacity)
        for i in log.keys():
            print(i," stock: ",log[i][0]," cost price: ",log[i][1])
        print("Total cost price: ",total_CP)
        print("Maximum profit estimated: ",max_profit)

'''Some random test cases
Need to create a proper interface for input and connection with models.py for
stock predictions.'''
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
        rack_main.append((i.brand,round((i.profit_percent()/i.stock),8),i.stock,i.profit(),i.CP))
    Rack_Maxim.getMaxValue(rack_main,rice_rack.capacity)
    


    
    
