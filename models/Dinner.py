from models.Dessert import Dessert
from models.Meal import Meal


class Dinner(Meal):
    def __init__(self, main_id , side_id, drink_id, desert_id):
        self.desert=Dessert(desert_id,"")
        super().__init__(main_id,side_id,drink_id)
