from models.Drink import Drink
from models.Main import Main
from models.Side import Side


class Meal(object):
    def __init__(self, main_id , side_id, drink_id):
        self.main=Main(main_id,"")
        self.side=Side(side_id,"")
        self.drink=Drink(drink_id,"")