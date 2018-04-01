from MasterEquipment.Equipment import Equipment as Equipment


class TradeGoods(Equipment):
    goods = ""

    def __init__(self, inCategory, inCost, inWeight, inGoods):
        super().__init__(inCategory, inCost, inWeight)

        self.goods = inGoods

    def getGoods(self):
        return self.goods

    def setGoods(self, inGoods):
        self.goods = inGoods

    def toString(self):
        super().toString()
        print("Goods: " + self.getGoods())

    def botMessage(self):
        return super().botMessage() + "Goods: " + self.getGoods()