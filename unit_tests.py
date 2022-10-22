import unittest
from utils import *
from io import StringIO
import sys

class TestOrders(unittest.TestCase):
    # Implemengtation of the different test cases in the assignment
    def test1(self):
        order="Breakfast 1,2,3"
        captured_output = StringIO()         
        sys.stdout = captured_output  # Capture the output of the console           
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Eggs, Toast, Coffee, ")

    def test2(self):
        order="Breakfast 2,3,1"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Eggs, Toast, Coffee, ")

    def test3(self):
        order="Breakfast 1,2,3,3,3"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Eggs, Toast, Coffee(3), ")

    def test4(self):
        order="Breakfast 1"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Unable to process: Side is missing\n")

    def test6(self):
        order="Lunch 1,2,3"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Sandwich, Chips, Soda, ")

    def test7(self):
        order="Lunch 1,2"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Sandwich, Chips, Water")
    
    def test8(self):
        order="Lunch 1,2,2"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Sandwich, Chips(2), Water")
    
    def test9(self):
        order="Lunch"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Unable to process: Main is missing, side is missing\n")
    
    def test10(self):
        order="Dinner 1,2,3,4"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Steak, Potatoes, Wine, Water, Cake, ")
    
    def test11(self):
        order="Dinner 1,2,3"
        captured_output = StringIO()         
        sys.stdout = captured_output              
        take_orders(order)
        sys.stdout = sys.__stdout__            
        self.assertEqual(captured_output.getvalue(), "Unable to process: Dessert is missing\n")
    

        
if __name__ == '__main__':
    unittest.main()