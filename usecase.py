from myexception import InvalidWholeSaleError
class Purchase:
    def __init__(self,purchase_id,purchase_date,user,total_amount):
        #self.__id=id #private if required
        self.purchase_id=purchase_id
        self.purchase_date=purchase_date
        self.user=user
        self.total_amount=total_amount
    def set_purchase_id(self,id):
        self.purchase_id=id
    def get_purchase_id(self):
        return self.purchase_id
    def set_purchase_date(self,purchase_date):
        self.purchase_date=purchase_date
    def get_purchase_date(self):
        return self.purchase_date
    def set_cost(self,cost):
        self.cost=cost
    def get_cost(self):
        return self.cost
    def set_quantity(self,quantity):
        self.quantity=quantity
    def get_quantity(self):
        return self.quantity
    def set_total_amount(self,total_amount):
        self.total_amount=total_amount
    def get_total_amount(self):
        return self.total_amount
    def set_user(self,user):
        self.user=user
    def get_user(self):
        return self.user
    @staticmethod
    def obtain_purchase_with_amount(kit_details):
        L=kit_details.split(",")
        L1=L[0:3]
        try:
            purchase_id=int(L1[0])
        except Exception:
            print("Please enter numerical value for purchase id")
            return
            
              #KeyboardInterrupt : for non integer
        purchase_date=L1[1]
        user=L1[2]
        L2=L[3:]
        count=0
        for x in L2:
            count+=1
        if count%3==0:
            no_of_items=0
            total_amount=0
            L3=[]
            index=0
            while index<len(L2):
                L3.append([L2[index],L2[index+1],L2[index+2]])
                total_amount+=float(L2[index+1])*int(L2[index+2])
                index+=3
                no_of_items+=1
            #print("Items are:",L3)
            #print("Number of items are:",no_of_items)
        else:
            print("Please enter sufficient details")
            return
        if no_of_items>=5:
            print("ID: {} USER: {} AMOUNT: {}".format(purchase_id,user,total_amount))
            return Purchase(purchase_id,purchase_date,user,total_amount)
        else:
            try:
                raise InvalidWholeSaleError("Purchase is not a wholesale /Items are less than 5")
            except InvalidWholeSaleError as e:
                print(e)
                
print("Format:Enter purchase id, purchase_date,user,item_name1,item_cost1,item_quantitiy1,item_name2,item_cost2,item_quantitiy2")
kit_details=input("Enter crickit kit details as above format")
Purchase.obtain_purchase_with_amount(kit_details)


#output:
#print("ID: {} USER: {} AMOUNT: {}".format(obj.get_purchase_id(),obj.get_user(),obj.get_total_amount()))

#input:
#101,2-3-2021,venu,bat,500.00,4,ball,200,2,guard,200.00,2,helmet,1500.00,4,vickets,1500.00,2





