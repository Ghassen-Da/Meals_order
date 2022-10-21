from models.Dessert import Dessert
from models.Drink import Drink
from models.Main import Main
from models.Side import Side


# putting them into arrays because of extensibility (an array of instances in the future)
main_breakfasts=[Main(1, "Eggs")]
side_breakfasts=[Side(2,"Toast")]
drink_breakfasts=[Drink(3,"Coffee")]

main_lunchs=[Main(1, "Sandwich")]
side_lunchs=[Side(2,"Chips")]
drink_lunchs=[Drink(3,"Soda")]

main_dinners=[Main(1, "Steak")]
side_dinners=[Side(2,"Potatoes")]
drink_dinners=[Drink(3,"Wine")]
dessert_dinners=[Dessert(4,"Cake")]


