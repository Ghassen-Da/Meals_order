from models.Meal import Meal


class Lunch(Meal):
    def __init__(self, main_id , side_id, drink_id):
        super().__init__(main_id,side_id,drink_id)
