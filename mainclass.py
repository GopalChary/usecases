
from usecase import Purchase
class MainClass:
    def read_data(self):
        print("Format:Enter purchase id, purchase_date,user,item_name1,item_cost1,item_quantitiy1,item_name2,item_cost2,item_quantitiy2")
        kit_details=input("Enter crickit kit details as above format")
        Purchase.obtain_purchase_with_amount(kit_details)

    # def get_data(self):
    #     print("ID\tDATE\tCOST\tQUANTITY\tTotal Amount\tUSER")
    #     print("{}\t{}\t{}\t{}\t{}\t{}".format(self.obj.get_id(),self.obj.get_purchase_date(),self.obj.get_cost(),self.obj.get_quantity(),self.obj.get_total_amount(),self.obj.get_user()))


        # print("ID",self.obj.get_id())
        # print("DATE",self.obj.get_purchase_date())
        # print("COST",self.obj.get_cost())
        # print("QUANTITY",self.obj.get_quantity())
        # print("Total Amount",self.obj.get_total_amount())
        # print("USER",self.obj.get_user())


if __name__=="__main__":
    mc=MainClass()
    mc.read_data()
    #mc.get_data()
