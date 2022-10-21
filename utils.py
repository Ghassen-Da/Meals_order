from data import *

# Used to retrieve meals names from client's order by id
def get_name_from_id(array, id):
    for object in array:
        if object.id==id:
            return object.name

def view(orders, menu_part_choices):
    # choice_order is an array where the index is the meal id
    # and the value is the number of occurrences
    choice_orders=[0] * 100 # Initialized to 100 but we can go bigger if needed
    for order in orders:
        order_name=get_name_from_id(menu_part_choices, int(order))
        if order_name:
            choice_orders[int(order)]=choice_orders[int(order)]+1
    for idx, x in enumerate(choice_orders):
        if x!=0: #Print the meal
            print(get_name_from_id(menu_part_choices, idx),end="") 
            if x>1: #Print the number of occurrences if more than 1
                print("({0})".format(x),end="") 
            print(",", end=" ")

# return a boolean of the availability of the menu_part in the order
# exp: availability of drink in the order
def basic_availablity(orders, main_meal):
    for order in orders:
        for item in main_meal:
            if int(order)==item.id:
                return True
    return False

# Determine water is available in the dinner's order to add it if not
def water_availability_dinner(orders, drink_dinners):
    water_index=0
    for drink in drink_dinners:
        if drink.name=="Water":
            water_index=drink.id
    for order in orders:
        if order==water_index:
            return True
    return False


# Checks the availability of main, side, drink in the order
# returns a list of 3 booleans (main, side, drink) availability
def total_availability(orders, main, side, drink):
    main_available= basic_availablity(orders, main)
    if main_available==False:
        print("Unable to process: Main is missing",end="")
        return [False, None, None]
    side_available= basic_availablity(orders, side)
    if side_available==False:
        print("Unable to process: Side is missing",end="")
        return [True, False, None]
    drink_available= basic_availablity(orders, drink)
    return [main_available, side_available, drink_available]


# main business logic with a switch case on the order (Breakfast, Lunch, Dinner)
# Seperate implementation from the main function to be able to pass a param
# and test it with different inputs
def take_orders(order):
    ordered_meal=order.split(" ")[0]
    try:
        order.split(" ")[1]
        orders=order.split(" ")[1].split(",")
        match ordered_meal:
            case "Breakfast":
                total_availability_breakfast=total_availability(orders, main_breakfasts, side_breakfasts, drink_breakfasts)
                if total_availability_breakfast[0]==False: #Main not found
                    return
                if total_availability_breakfast[1]==False: #Side not found
                    return
                # Main
                view(orders, main_breakfasts)    
                # Side
                view(orders, side_breakfasts)  
                # Drink
                view(orders, drink_breakfasts)
                if total_availability_breakfast[2] == False: #Drink not found
                    print('Water',end="")

            case "Lunch":
                total_availability_lunch=total_availability(orders, main_lunchs, side_lunchs, drink_lunchs)
                if total_availability_lunch[0]==False: #Main not found
                    return
                if total_availability_lunch[1]==False: #Side not found
                    return
                # Main
                view(orders, main_lunchs)
                # Side
                view(orders, side_lunchs)
                # Drink
                view(orders, drink_lunchs)
                if total_availability_lunch[2] == False: #Drink not found
                    print('Water', end="")

            case "Dinner":
                total_availability_dinner=total_availability(orders, main_dinners, side_dinners, drink_dinners)
                if total_availability_dinner[0]==False: #Main not found
                    return
                if total_availability_dinner[1]==False: #Side not found
                    return
                dessert_availibility=basic_availablity(orders,dessert_dinners)
                if dessert_availibility==False:
                    print("Unable to process: Dessert is missing",end="")
                    return
                # Main
                view(orders, main_dinners)
                # Side
                view(orders, side_dinners)
                # Drink
                view(orders, drink_dinners)
                if not total_availability_dinner[2]: #Drink not found
                    print('Water')
                elif not water_availability_dinner(orders, drink_dinners): #Drink found but doesn't contain water
                    print('Water', end=", ")
                # Dessert
                view(orders, dessert_dinners)
    except IndexError:
        print("Unable to process: Main is missing, side is missing",end="")