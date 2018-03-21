from MasterEquipment.Equipment import Equipment as Equipment

class TradeGoods(Equipment):
    goods = ""

    def _init_TradeGoods(self, inNaame, inCost, inWeight, inGoods):
        super().__init__(inName, inCost, inWeight)

        self.goods = inGoods

    def getGoods(self):
        return self.goods
  
    def setGoods(self, inGoods):
        self.goods = inGoods







    

