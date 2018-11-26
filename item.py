class HouseItem():
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return  "%s占用%.2f"%(self.name,self.area)
        


class House():
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return  ("户型：%s\n面积%.2f\n剩余面积：%.2f\n家具列表：%s"
                %(self.house_type,self.area,self.free_area,self.item_list))
    def add_item(self,item):
        print ("add:%s"%item)
        if item.area> self.free_area:
            print("%s is too big!"%(item.name))
            return
        self.item_list.append(item.name)
        self.free_area -=item.area
bed = HouseItem('simmons',4)
chest = HouseItem('yigui',2)
table = HouseItem('canzhuo',1.5)

print(bed)
print(chest)
print(table)
my_home = House('两室一厅',100)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)