from models.MenuPart import MenuPart


class Drink(MenuPart):
    def __init__(self, id , name):
        super().__init__(id, name)
